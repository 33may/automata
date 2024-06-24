# Generated from Calculator.g4 by ANTLR 4.13.1
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
        4,1,9,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,34,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,
        5,6,1,0,7,8,35,0,8,1,0,0,0,2,11,1,0,0,0,4,19,1,0,0,0,6,33,1,0,0,
        0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,16,3,4,2,0,12,13,7,0,
        0,0,13,15,3,4,2,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,
        1,0,0,0,17,3,1,0,0,0,18,16,1,0,0,0,19,24,3,6,3,0,20,21,7,1,0,0,21,
        23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,5,1,0,0,0,26,24,1,0,0,0,27,34,5,3,0,0,28,34,5,4,0,0,29,30,5,
        1,0,0,30,31,3,2,1,0,31,32,5,2,0,0,32,34,1,0,0,0,33,27,1,0,0,0,33,
        28,1,0,0,0,33,29,1,0,0,0,34,7,1,0,0,0,3,16,24,33
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INT", "FLOAT", 
                      "PLUS", "MINUS", "MULT", "DIV", "WS" ]

    RULE_instance = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "instance", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT=3
    FLOAT=4
    PLUS=5
    MINUS=6
    MULT=7
    DIV=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def EOF(self):
            return self.getToken(CalculatorParser.EOF, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_instance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance" ):
                listener.enterInstance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance" ):
                listener.exitInstance(self)




    def instance(self):

        localctx = CalculatorParser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(CalculatorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.TermContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.PLUS)
            else:
                return self.getToken(CalculatorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.MINUS)
            else:
                return self.getToken(CalculatorParser.MINUS, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CalculatorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.term()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 12
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.term()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.FactorContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.MULT)
            else:
                return self.getToken(CalculatorParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.DIV)
            else:
                return self.getToken(CalculatorParser.DIV, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = CalculatorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.factor()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.factor()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CalculatorParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CalculatorParser.FLOAT, 0)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = CalculatorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(CalculatorParser.INT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(CalculatorParser.FLOAT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(CalculatorParser.T__0)
                self.state = 30
                self.expr()
                self.state = 31
                self.match(CalculatorParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





