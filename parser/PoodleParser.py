# Generated from Poodle.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,132,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,3,2,37,8,2,1,2,1,2,3,2,41,8,
        2,1,2,1,2,3,2,45,8,2,1,2,1,2,3,2,49,8,2,3,2,51,8,2,1,3,1,3,1,3,3,
        3,56,8,3,1,3,1,3,3,3,60,8,3,1,3,1,3,1,3,1,4,1,4,3,4,67,8,4,1,4,1,
        4,3,4,71,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,83,8,5,
        1,5,1,5,1,5,1,5,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,1,6,1,6,1,6,
        1,6,1,6,1,6,5,6,102,8,6,10,6,12,6,105,9,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,7,3,7,122,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,0,1,10,10,0,2,4,6,8,10,12,14,16,
        18,0,3,1,0,6,7,1,0,8,9,1,0,15,16,142,0,23,1,0,0,0,2,32,1,0,0,0,4,
        50,1,0,0,0,6,52,1,0,0,0,8,64,1,0,0,0,10,82,1,0,0,0,12,95,1,0,0,0,
        14,121,1,0,0,0,16,123,1,0,0,0,18,129,1,0,0,0,20,22,3,2,1,0,21,20,
        1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,
        25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,33,3,4,2,0,29,30,3,4,
        2,0,30,31,3,2,1,0,31,33,1,0,0,0,32,28,1,0,0,0,32,29,1,0,0,0,33,3,
        1,0,0,0,34,36,3,6,3,0,35,37,5,17,0,0,36,35,1,0,0,0,36,37,1,0,0,0,
        37,51,1,0,0,0,38,40,3,8,4,0,39,41,5,17,0,0,40,39,1,0,0,0,40,41,1,
        0,0,0,41,51,1,0,0,0,42,44,3,12,6,0,43,45,5,17,0,0,44,43,1,0,0,0,
        44,45,1,0,0,0,45,51,1,0,0,0,46,48,3,16,8,0,47,49,5,17,0,0,48,47,
        1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,34,1,0,0,0,50,38,1,0,0,0,
        50,42,1,0,0,0,50,46,1,0,0,0,51,5,1,0,0,0,52,53,5,1,0,0,53,55,5,15,
        0,0,54,56,5,13,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,
        59,5,2,0,0,58,60,5,13,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,
        0,0,61,62,3,10,5,0,62,63,5,3,0,0,63,7,1,0,0,0,64,66,5,15,0,0,65,
        67,5,13,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,70,5,2,
        0,0,69,71,5,13,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,
        73,3,10,5,0,73,74,5,3,0,0,74,9,1,0,0,0,75,76,6,5,-1,0,76,83,5,16,
        0,0,77,83,5,15,0,0,78,79,5,4,0,0,79,80,3,10,5,0,80,81,5,5,0,0,81,
        83,1,0,0,0,82,75,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,83,92,1,0,0,
        0,84,85,10,2,0,0,85,86,7,0,0,0,86,91,3,10,5,3,87,88,10,1,0,0,88,
        89,7,1,0,0,89,91,3,10,5,2,90,84,1,0,0,0,90,87,1,0,0,0,91,94,1,0,
        0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,11,1,0,0,0,94,92,1,0,0,0,95,96,
        5,10,0,0,96,97,5,15,0,0,97,98,5,4,0,0,98,99,3,14,7,0,99,103,5,5,
        0,0,100,102,5,17,0,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,11,
        0,0,107,108,3,2,1,0,108,109,5,12,0,0,109,13,1,0,0,0,110,122,1,0,
        0,0,111,122,7,2,0,0,112,113,7,2,0,0,113,117,5,14,0,0,114,116,5,13,
        0,0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,120,1,0,0,0,119,117,1,0,0,0,120,122,3,14,7,0,121,110,1,0,
        0,0,121,111,1,0,0,0,121,112,1,0,0,0,122,15,1,0,0,0,123,124,5,15,
        0,0,124,125,5,4,0,0,125,126,3,14,7,0,126,127,5,5,0,0,127,128,5,3,
        0,0,128,17,1,0,0,0,129,130,3,2,1,0,130,19,1,0,0,0,17,23,32,36,40,
        44,48,50,55,59,66,70,82,90,92,103,117,121
    ]

class PoodleParser ( Parser ):

    grammarFileName = "Poodle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var '", "'='", "';'", "'('", "')'", 
                     "'*'", "'/'", "'+'", "'-'", "'function '", "'{'", "'}'", 
                     "' '", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SPACE", "ARG_SEP", "IDENTIFIER", "INT", 
                      "NEWLINE" ]

    RULE_parse = 0
    RULE_progStmts = 1
    RULE_progStmt = 2
    RULE_varDeclaration = 3
    RULE_varAssignment = 4
    RULE_mathExpr = 5
    RULE_funcDef = 6
    RULE_funcArgs = 7
    RULE_funcCall = 8
    RULE_funcBody = 9

    ruleNames =  [ "parse", "progStmts", "progStmt", "varDeclaration", "varAssignment", 
                   "mathExpr", "funcDef", "funcArgs", "funcCall", "funcBody" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    SPACE=13
    ARG_SEP=14
    IDENTIFIER=15
    INT=16
    NEWLINE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PoodleParser.EOF, 0)

        def progStmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PoodleParser.ProgStmtsContext)
            else:
                return self.getTypedRuleContext(PoodleParser.ProgStmtsContext,i)


        def getRuleIndex(self):
            return PoodleParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = PoodleParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33794) != 0):
                self.state = 20
                self.progStmts()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(PoodleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgStmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def progStmt(self):
            return self.getTypedRuleContext(PoodleParser.ProgStmtContext,0)


        def progStmts(self):
            return self.getTypedRuleContext(PoodleParser.ProgStmtsContext,0)


        def getRuleIndex(self):
            return PoodleParser.RULE_progStmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgStmts" ):
                listener.enterProgStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgStmts" ):
                listener.exitProgStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgStmts" ):
                return visitor.visitProgStmts(self)
            else:
                return visitor.visitChildren(self)




    def progStmts(self):

        localctx = PoodleParser.ProgStmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_progStmts)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.progStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.progStmt()
                self.state = 30
                self.progStmts()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(PoodleParser.VarDeclarationContext,0)


        def NEWLINE(self):
            return self.getToken(PoodleParser.NEWLINE, 0)

        def varAssignment(self):
            return self.getTypedRuleContext(PoodleParser.VarAssignmentContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(PoodleParser.FuncDefContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(PoodleParser.FuncCallContext,0)


        def getRuleIndex(self):
            return PoodleParser.RULE_progStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgStmt" ):
                listener.enterProgStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgStmt" ):
                listener.exitProgStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgStmt" ):
                return visitor.visitProgStmt(self)
            else:
                return visitor.visitChildren(self)




    def progStmt(self):

        localctx = PoodleParser.ProgStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_progStmt)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.varDeclaration()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 35
                    self.match(PoodleParser.NEWLINE)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.varAssignment()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 39
                    self.match(PoodleParser.NEWLINE)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.funcDef()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 43
                    self.match(PoodleParser.NEWLINE)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.funcCall()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 47
                    self.match(PoodleParser.NEWLINE)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PoodleParser.IDENTIFIER, 0)

        def mathExpr(self):
            return self.getTypedRuleContext(PoodleParser.MathExprContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(PoodleParser.SPACE)
            else:
                return self.getToken(PoodleParser.SPACE, i)

        def getRuleIndex(self):
            return PoodleParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = PoodleParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PoodleParser.T__0)
            self.state = 53
            self.match(PoodleParser.IDENTIFIER)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 54
                self.match(PoodleParser.SPACE)


            self.state = 57
            self.match(PoodleParser.T__1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 58
                self.match(PoodleParser.SPACE)


            self.state = 61
            self.mathExpr(0)
            self.state = 62
            self.match(PoodleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PoodleParser.IDENTIFIER, 0)

        def mathExpr(self):
            return self.getTypedRuleContext(PoodleParser.MathExprContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(PoodleParser.SPACE)
            else:
                return self.getToken(PoodleParser.SPACE, i)

        def getRuleIndex(self):
            return PoodleParser.RULE_varAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarAssignment" ):
                listener.enterVarAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarAssignment" ):
                listener.exitVarAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssignment" ):
                return visitor.visitVarAssignment(self)
            else:
                return visitor.visitChildren(self)




    def varAssignment(self):

        localctx = PoodleParser.VarAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(PoodleParser.IDENTIFIER)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 65
                self.match(PoodleParser.SPACE)


            self.state = 68
            self.match(PoodleParser.T__1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 69
                self.match(PoodleParser.SPACE)


            self.state = 72
            self.mathExpr(0)
            self.state = 73
            self.match(PoodleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # MathExprContext
            self.op = None # Token
            self.right = None # MathExprContext

        def INT(self):
            return self.getToken(PoodleParser.INT, 0)

        def IDENTIFIER(self):
            return self.getToken(PoodleParser.IDENTIFIER, 0)

        def mathExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PoodleParser.MathExprContext)
            else:
                return self.getTypedRuleContext(PoodleParser.MathExprContext,i)


        def getRuleIndex(self):
            return PoodleParser.RULE_mathExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpr" ):
                listener.enterMathExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpr" ):
                listener.exitMathExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathExpr" ):
                return visitor.visitMathExpr(self)
            else:
                return visitor.visitChildren(self)



    def mathExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PoodleParser.MathExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_mathExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 76
                self.match(PoodleParser.INT)
                pass
            elif token in [15]:
                self.state = 77
                self.match(PoodleParser.IDENTIFIER)
                pass
            elif token in [4]:
                self.state = 78
                self.match(PoodleParser.T__3)
                self.state = 79
                self.mathExpr(0)
                self.state = 80
                self.match(PoodleParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = PoodleParser.MathExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mathExpr)
                        self.state = 84
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        localctx.right = self.mathExpr(3)
                        pass

                    elif la_ == 2:
                        localctx = PoodleParser.MathExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mathExpr)
                        self.state = 87
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 88
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        localctx.left = self.mathExpr(2)
                        pass

             
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PoodleParser.IDENTIFIER, 0)

        def funcArgs(self):
            return self.getTypedRuleContext(PoodleParser.FuncArgsContext,0)


        def progStmts(self):
            return self.getTypedRuleContext(PoodleParser.ProgStmtsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PoodleParser.NEWLINE)
            else:
                return self.getToken(PoodleParser.NEWLINE, i)

        def getRuleIndex(self):
            return PoodleParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = PoodleParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PoodleParser.T__9)
            self.state = 96
            self.match(PoodleParser.IDENTIFIER)
            self.state = 97
            self.match(PoodleParser.T__3)
            self.state = 98
            self.funcArgs()
            self.state = 99
            self.match(PoodleParser.T__4)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 100
                self.match(PoodleParser.NEWLINE)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(PoodleParser.T__10)
            self.state = 107
            self.progStmts()
            self.state = 108
            self.match(PoodleParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PoodleParser.INT, 0)

        def IDENTIFIER(self):
            return self.getToken(PoodleParser.IDENTIFIER, 0)

        def ARG_SEP(self):
            return self.getToken(PoodleParser.ARG_SEP, 0)

        def funcArgs(self):
            return self.getTypedRuleContext(PoodleParser.FuncArgsContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(PoodleParser.SPACE)
            else:
                return self.getToken(PoodleParser.SPACE, i)

        def getRuleIndex(self):
            return PoodleParser.RULE_funcArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncArgs" ):
                listener.enterFuncArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncArgs" ):
                listener.exitFuncArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncArgs" ):
                return visitor.visitFuncArgs(self)
            else:
                return visitor.visitChildren(self)




    def funcArgs(self):

        localctx = PoodleParser.FuncArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcArgs)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 113
                self.match(PoodleParser.ARG_SEP)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 114
                    self.match(PoodleParser.SPACE)
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 120
                self.funcArgs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PoodleParser.IDENTIFIER, 0)

        def funcArgs(self):
            return self.getTypedRuleContext(PoodleParser.FuncArgsContext,0)


        def getRuleIndex(self):
            return PoodleParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = PoodleParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(PoodleParser.IDENTIFIER)
            self.state = 124
            self.match(PoodleParser.T__3)
            self.state = 125
            self.funcArgs()
            self.state = 126
            self.match(PoodleParser.T__4)
            self.state = 127
            self.match(PoodleParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def progStmts(self):
            return self.getTypedRuleContext(PoodleParser.ProgStmtsContext,0)


        def getRuleIndex(self):
            return PoodleParser.RULE_funcBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncBody" ):
                listener.enterFuncBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncBody" ):
                listener.exitFuncBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncBody" ):
                return visitor.visitFuncBody(self)
            else:
                return visitor.visitChildren(self)




    def funcBody(self):

        localctx = PoodleParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.progStmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.mathExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def mathExpr_sempred(self, localctx:MathExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




