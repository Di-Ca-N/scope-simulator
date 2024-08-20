from antlr4 import *
from parser.PoodleLexer import PoodleLexer
from parser.PoodleParser import PoodleParser
from parser.PoodleVisitor import PoodleVisitor

from scoping import Scoper, StackFrame

class PoodleInterpreter(PoodleVisitor):
    def __init__(self, scopingType, stepCallback=None):
        self.scoping: Scoper = scopingType
        self.functions = {}
        self.step_callback = stepCallback or (lambda _stack, _ctx, _line_text: None)

    def visitProgStmt(self, ctx: PoodleParser.ProgStmtContext):
        self.step_callback(self.scoping.call_stack, ctx, ctx.getText())

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
                "name": funcName.getText(),
                "args": args,
                "body": body,
                "staticParent": self.scoping.getTopScope(),
            }

        elif ctx.funcCall():
            funcName, _, args, _, _ = ctx.funcCall().children

            if funcName.getText() == "print":
                for arg in args.children:
                    print(self.scoping.get(arg.getText()))

            else:
                function = self.functions[funcName.getText()]
                funcArgs = {}
                if function["args"].children is not None:
                    for arg, parameter in zip(args.children, function["args"].children):
                        funcArgs[parameter.getText()] = self.eval(arg.getText())
                self.scoping.pushScope(StackFrame(funcName.getText(), staticLink=function["staticParent"], vars=funcArgs))

                self.step_callback(self.scoping.call_stack, ctx, f"{function['name']}({function['args'].getText()}) {{")
                self.visit(self.functions[funcName.getText()]["body"])
                self.step_callback(self.scoping.call_stack, ctx, "}")

                self.scoping.popScope()

    def evalMathExpr(self, ctx: PoodleParser.MathExprContext):
        match ctx.children:
            case [TerminalNode() as t]:
                return self.eval(t.getText())

            case [
                PoodleParser.MathExprContext() as left,
                TerminalNode() as op,
                PoodleParser.MathExprContext() as right,
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
                TerminalNode(),
            ]:
                return self.evalMathExpr(expr)

    def eval(self, value):
        if value.isnumeric():
            return int(value)
        return self.scoping.get(value)
