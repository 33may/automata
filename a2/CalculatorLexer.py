# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,4,2,25,8,2,11,2,12,2,26,
        1,3,4,3,30,8,3,11,3,12,3,31,1,3,1,3,4,3,36,8,3,11,3,12,3,37,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,49,8,8,11,8,12,8,50,1,8,1,8,
        0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,2,1,0,48,57,3,
        0,9,10,13,13,32,32,57,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,24,1,0,0,0,7,29,1,0,0,0,9,39,1,
        0,0,0,11,41,1,0,0,0,13,43,1,0,0,0,15,45,1,0,0,0,17,48,1,0,0,0,19,
        20,5,40,0,0,20,2,1,0,0,0,21,22,5,41,0,0,22,4,1,0,0,0,23,25,7,0,0,
        0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,6,1,
        0,0,0,28,30,7,0,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,33,1,0,0,0,33,35,5,46,0,0,34,36,7,0,0,0,35,34,1,0,
        0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,8,1,0,0,0,39,40,
        5,43,0,0,40,10,1,0,0,0,41,42,5,45,0,0,42,12,1,0,0,0,43,44,5,42,0,
        0,44,14,1,0,0,0,45,46,5,47,0,0,46,16,1,0,0,0,47,49,7,1,0,0,48,47,
        1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,
        52,53,6,8,0,0,53,18,1,0,0,0,5,0,26,31,37,50,1,6,0,0
    ]

class CalculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INT = 3
    FLOAT = 4
    PLUS = 5
    MINUS = 6
    MULT = 7
    DIV = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "PLUS", "MINUS", "MULT", "DIV", "WS" ]

    ruleNames = [ "T__0", "T__1", "INT", "FLOAT", "PLUS", "MINUS", "MULT", 
                  "DIV", "WS" ]

    grammarFileName = "Calculator.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


