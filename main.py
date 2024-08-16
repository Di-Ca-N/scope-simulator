from antlr4 import *
from parser.PoodleParser import PoodleParser
from parser.PoodleLexer import PoodleLexer
from parser.PoodleVisitor import PoodleVisitor

import pathlib
import click
import copy
import pprint


class Scoper:
    def __init__(self):
        self.call_stack = [{"staticParent": None, "vars": {}, "name": "global"}] # Starts with the global scope

    def pushScope(self, staticParent, args, scopeName): 
        self.call_stack.append({"staticParent": staticParent, "vars": args, "name": scopeName})

    def popScope(self): 
        self.call_stack.pop()

    def getTopScope(self):
        return self.call_stack[-1]

    def getTopIdx(self):
        return len(self.call_stack) - 1


class DynamicScoping(Scoper):
    def get(self, var): 
        for scope in reversed(self.call_stack):
            if var in scope["vars"]:
                return scope["vars"][var]
        return None

    def assign(self, var, val): 
        for scope in reversed(self.call_stack):
            if var in scope["vars"]:
                scope["vars"][var] = val
                return
        return None 

    def declare(self, var, val):
        self.call_stack[-1]["vars"][var] = val


class StaticScoping(Scoper):
    def get(self, var): 
        current_scope = self.call_stack[-1]
        while current_scope is not None:
            if var in current_scope["vars"]:
                return current_scope["vars"][var]
            current_scope = self.call_stack[current_scope["staticParent"]]
        return None

    def assign(self, var, val): 
        current_scope = self.call_stack[-1]
        while current_scope is not None:
            if var in current_scope["vars"]:
                current_scope["vars"][var] = val
                return
            current_scope = self.call_stack[current_scope["staticParent"]]

    def declare(self, var, val):
        self.call_stack[-1]["vars"][var] = val


class PoodleInterpreter(PoodleVisitor):
    def __init__(self, scopingType):
        self.scoping = scopingType
        self.functions = {}

    def visitProgStmt(self, ctx: PoodleParser.ProgStmtContext):
        if ctx.varDeclaration():
            _, var, _, val, _ = ctx.varDeclaration().children
            evaluated_value = self.evalMathExpr(val)

            self.scoping.declare(var.getText(), evaluated_value)

        elif ctx.varAssignment():
            var, _, val, _ = ctx.varAssignment().children
            evaluated_value = self.evalMathExpr(val)

            self.scoping.assign(var.getText(), evaluated_value)
        
        elif ctx.funcDef():
            _, funcName, _, args, _, _, body, _ = ctx.funcDef().children
            self.functions[funcName.getText()] = {
                "args": args,
                "body": body,
                "staticParent": self.scoping.getTopIdx()
            }

        elif ctx.funcCall():
            funcName, _, args, _, _= ctx.funcCall().children
    
            if funcName.getText() == "print":
                for arg in args.children:
                    print(self.scoping.get(arg.getText()))
                return
            else:
                function = self.functions[funcName.getText()]
                funcArgs = {}
                if function["args"].children is not None:
                    for arg, parameter in zip(args.children, function["args"].children):
                        funcArgs[parameter.getText()] = self.eval(arg.getText())
                self.scoping.pushScope(function["staticParent"], funcArgs, funcName.getText())
                self.visit(self.functions[funcName.getText()]["body"])
            
            self.scoping.popScope()

    def evalMathExpr(self, ctx: PoodleParser.MathExprContext):
        match ctx.children:
            case [TerminalNode() as t]:
                return self.eval(t.getText())
            
            case [
                PoodleParser.MathExprContext() as left, 
                TerminalNode() as op, 
                PoodleParser.MathExprContext() as right
            ]:
                left_value = self.evalMathExpr(left)
                right_value = self.evalMathExpr(right)

                op = op.getText()
                if op == "+":
                    return left_value + right_value
                elif op == "-":
                    return left_value - right_value
                elif op == "*":
                    return left_value * right_value
                elif op == "/":
                    return left_value / right_value

            case [
                TerminalNode(),
                PoodleParser.MathExprContext() as expr,
                TerminalNode()
            ]:
                return self.evalMathExpr(expr)

    def eval(self, value):
        if value.isnumeric():
            return int(value)
        return self.scoping.get(value)

@click.command()
@click.argument("file", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option("--scoping", default="static", type=click.Choice(["dynamic", "static"]), help="Scoping type to be used")
def main(file, scoping):
    lexer = PoodleLexer(InputStream(file.read_text()))
    stream = CommonTokenStream(lexer)
    parser = PoodleParser(stream)

    tree = parser.parse()
    interpreter = PoodleInterpreter(scopingType=DynamicScoping() if scoping == "dynamic" else StaticScoping())
    interpreter.visit(tree)

main()

