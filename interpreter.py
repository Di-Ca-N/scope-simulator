from dataclasses import dataclass

from antlr4 import *
from parser.PoodleLexer import PoodleLexer
from parser.PoodleParser import PoodleParser
from parser.PoodleVisitor import PoodleVisitor

from scoping import Scoper, StackFrame


@dataclass
class Function:
    name: str
    args: PoodleParser.FuncArgsContext
    body: PoodleParser.FuncBodyContext
    staticParent: StackFrame
    interpreter: 'PoodleInterpreter'

    def getArgNames(self):
        if self.args.children is None:
            return []
        return [arg.getText() for arg in self.args.children]

    def run(self, params: list[int], callback=None, callbackCtx=None):
        self.interpreter.scoping.pushScope(StackFrame(self.name, staticLink=self.staticParent))

        for paramName, paramValue in zip(self.getArgNames(), params):
            self.interpreter.scoping.declare(paramName, paramValue)

        if callback:
            callback(self.interpreter.scoping.call_stack, callbackCtx, f"{self.name}({self.args.getText()}) {{")

        self.interpreter.visit(self.body)

        if callback:
            callback(self.interpreter.scoping.call_stack, callbackCtx, "}")
        self.interpreter.scoping.popScope()


class PoodleInterpreter(PoodleVisitor):
    def __init__(self, scopingType, stepCallback=None):
        self.scoping: Scoper = scopingType
        self.functions: dict[str, Function] = {}
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
            self.functions[funcName.getText()] = Function(name=funcName.getText(), args=args, body=body, staticParent=self.scoping.getTopScope(), interpreter=self)
        elif ctx.funcCall():
            funcName, _, args, _, _ = ctx.funcCall().children

            if funcName.getText() == "print":
                for arg in args.children:
                    print(self.scoping.get(arg.getText()))

            else:
                function = self.functions[funcName.getText()]
                funcParams = []
                if args.children is not None:
                    funcParams = [self.eval(arg.getText()) for arg in args.children]

                function.run(funcParams, self.step_callback, ctx)

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

    def eval(self, value: str) -> int:
        if value.isnumeric():
            return int(value)
        return self.scoping.get(value)
