# Generated from Poodle.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PoodleParser import PoodleParser
else:
    from PoodleParser import PoodleParser

# This class defines a complete listener for a parse tree produced by PoodleParser.
class PoodleListener(ParseTreeListener):

    # Enter a parse tree produced by PoodleParser#parse.
    def enterParse(self, ctx:PoodleParser.ParseContext):
        pass

    # Exit a parse tree produced by PoodleParser#parse.
    def exitParse(self, ctx:PoodleParser.ParseContext):
        pass


    # Enter a parse tree produced by PoodleParser#progStmts.
    def enterProgStmts(self, ctx:PoodleParser.ProgStmtsContext):
        pass

    # Exit a parse tree produced by PoodleParser#progStmts.
    def exitProgStmts(self, ctx:PoodleParser.ProgStmtsContext):
        pass


    # Enter a parse tree produced by PoodleParser#progStmt.
    def enterProgStmt(self, ctx:PoodleParser.ProgStmtContext):
        pass

    # Exit a parse tree produced by PoodleParser#progStmt.
    def exitProgStmt(self, ctx:PoodleParser.ProgStmtContext):
        pass


    # Enter a parse tree produced by PoodleParser#varDeclaration.
    def enterVarDeclaration(self, ctx:PoodleParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by PoodleParser#varDeclaration.
    def exitVarDeclaration(self, ctx:PoodleParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by PoodleParser#varAssignment.
    def enterVarAssignment(self, ctx:PoodleParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by PoodleParser#varAssignment.
    def exitVarAssignment(self, ctx:PoodleParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by PoodleParser#mathExpr.
    def enterMathExpr(self, ctx:PoodleParser.MathExprContext):
        pass

    # Exit a parse tree produced by PoodleParser#mathExpr.
    def exitMathExpr(self, ctx:PoodleParser.MathExprContext):
        pass


    # Enter a parse tree produced by PoodleParser#funcDef.
    def enterFuncDef(self, ctx:PoodleParser.FuncDefContext):
        pass

    # Exit a parse tree produced by PoodleParser#funcDef.
    def exitFuncDef(self, ctx:PoodleParser.FuncDefContext):
        pass


    # Enter a parse tree produced by PoodleParser#funcArgs.
    def enterFuncArgs(self, ctx:PoodleParser.FuncArgsContext):
        pass

    # Exit a parse tree produced by PoodleParser#funcArgs.
    def exitFuncArgs(self, ctx:PoodleParser.FuncArgsContext):
        pass


    # Enter a parse tree produced by PoodleParser#funcCall.
    def enterFuncCall(self, ctx:PoodleParser.FuncCallContext):
        pass

    # Exit a parse tree produced by PoodleParser#funcCall.
    def exitFuncCall(self, ctx:PoodleParser.FuncCallContext):
        pass


    # Enter a parse tree produced by PoodleParser#funcBody.
    def enterFuncBody(self, ctx:PoodleParser.FuncBodyContext):
        pass

    # Exit a parse tree produced by PoodleParser#funcBody.
    def exitFuncBody(self, ctx:PoodleParser.FuncBodyContext):
        pass



del PoodleParser