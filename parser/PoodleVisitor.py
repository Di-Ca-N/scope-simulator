# Generated from Poodle.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PoodleParser import PoodleParser
else:
    from PoodleParser import PoodleParser

# This class defines a complete generic visitor for a parse tree produced by PoodleParser.

class PoodleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PoodleParser#parse.
    def visitParse(self, ctx:PoodleParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#progStmts.
    def visitProgStmts(self, ctx:PoodleParser.ProgStmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#progStmt.
    def visitProgStmt(self, ctx:PoodleParser.ProgStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#varDeclaration.
    def visitVarDeclaration(self, ctx:PoodleParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#varAssignment.
    def visitVarAssignment(self, ctx:PoodleParser.VarAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#mathExpr.
    def visitMathExpr(self, ctx:PoodleParser.MathExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#funcDef.
    def visitFuncDef(self, ctx:PoodleParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#funcArgs.
    def visitFuncArgs(self, ctx:PoodleParser.FuncArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#funcCall.
    def visitFuncCall(self, ctx:PoodleParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PoodleParser#funcBody.
    def visitFuncBody(self, ctx:PoodleParser.FuncBodyContext):
        return self.visitChildren(ctx)



del PoodleParser