# Generated from Poodle.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,17,95,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,
        2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,1,13,1,13,1,14,1,14,5,14,79,8,14,10,14,12,14,82,9,14,1,15,4,
        15,85,8,15,11,15,12,15,86,1,16,4,16,90,8,16,11,16,12,16,91,1,16,
        1,16,0,0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,25,13,27,14,29,15,31,16,33,17,1,0,4,2,0,65,90,97,122,3,0,48,
        57,65,90,97,122,1,0,48,57,2,0,10,10,13,13,97,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,
        0,1,35,1,0,0,0,3,40,1,0,0,0,5,42,1,0,0,0,7,44,1,0,0,0,9,46,1,0,0,
        0,11,48,1,0,0,0,13,50,1,0,0,0,15,52,1,0,0,0,17,54,1,0,0,0,19,56,
        1,0,0,0,21,66,1,0,0,0,23,68,1,0,0,0,25,70,1,0,0,0,27,74,1,0,0,0,
        29,76,1,0,0,0,31,84,1,0,0,0,33,89,1,0,0,0,35,36,5,118,0,0,36,37,
        5,97,0,0,37,38,5,114,0,0,38,39,5,32,0,0,39,2,1,0,0,0,40,41,5,61,
        0,0,41,4,1,0,0,0,42,43,5,59,0,0,43,6,1,0,0,0,44,45,5,40,0,0,45,8,
        1,0,0,0,46,47,5,41,0,0,47,10,1,0,0,0,48,49,5,42,0,0,49,12,1,0,0,
        0,50,51,5,47,0,0,51,14,1,0,0,0,52,53,5,43,0,0,53,16,1,0,0,0,54,55,
        5,45,0,0,55,18,1,0,0,0,56,57,5,102,0,0,57,58,5,117,0,0,58,59,5,110,
        0,0,59,60,5,99,0,0,60,61,5,116,0,0,61,62,5,105,0,0,62,63,5,111,0,
        0,63,64,5,110,0,0,64,65,5,32,0,0,65,20,1,0,0,0,66,67,5,123,0,0,67,
        22,1,0,0,0,68,69,5,125,0,0,69,24,1,0,0,0,70,71,5,32,0,0,71,72,1,
        0,0,0,72,73,6,12,0,0,73,26,1,0,0,0,74,75,5,44,0,0,75,28,1,0,0,0,
        76,80,7,0,0,0,77,79,7,1,0,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,
        0,0,0,80,81,1,0,0,0,81,30,1,0,0,0,82,80,1,0,0,0,83,85,7,2,0,0,84,
        83,1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,32,1,0,0,
        0,88,90,7,3,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,
        1,0,0,0,92,93,1,0,0,0,93,94,6,16,0,0,94,34,1,0,0,0,4,0,80,86,91,
        1,6,0,0
    ]

class PoodleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    SPACE = 13
    ARG_SEP = 14
    IDENTIFIER = 15
    INT = 16
    NEWLINE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var '", "'='", "';'", "'('", "')'", "'*'", "'/'", "'+'", "'-'", 
            "'function '", "'{'", "'}'", "' '", "','" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "ARG_SEP", "IDENTIFIER", "INT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "SPACE", "ARG_SEP", 
                  "IDENTIFIER", "INT", "NEWLINE" ]

    grammarFileName = "Poodle.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


