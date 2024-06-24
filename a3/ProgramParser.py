# Generated from Program.g4 by ANTLR 4.13.1
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
        4,1,18,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,5,5,59,8,5,10,5,12,5,62,9,5,1,5,3,5,65,8,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,5,10,97,8,10,10,10,12,10,100,
        9,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,110,8,12,1,13,
        1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,1,2,0,14,
        14,16,16,108,0,31,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,51,1,0,0,0,
        8,53,1,0,0,0,10,56,1,0,0,0,12,66,1,0,0,0,14,74,1,0,0,0,16,82,1,0,
        0,0,18,87,1,0,0,0,20,98,1,0,0,0,22,101,1,0,0,0,24,109,1,0,0,0,26,
        111,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,
        0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,
        1,0,0,0,36,37,3,4,2,0,37,38,5,1,0,0,38,46,1,0,0,0,39,46,3,6,3,0,
        40,41,3,8,4,0,41,42,5,1,0,0,42,46,1,0,0,0,43,46,3,18,9,0,44,46,3,
        22,11,0,45,36,1,0,0,0,45,39,1,0,0,0,45,40,1,0,0,0,45,43,1,0,0,0,
        45,44,1,0,0,0,46,3,1,0,0,0,47,48,5,14,0,0,48,49,5,2,0,0,49,50,3,
        26,13,0,50,5,1,0,0,0,51,52,3,10,5,0,52,7,1,0,0,0,53,54,5,14,0,0,
        54,55,5,3,0,0,55,9,1,0,0,0,56,60,3,12,6,0,57,59,3,14,7,0,58,57,1,
        0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,64,1,0,0,0,62,
        60,1,0,0,0,63,65,3,16,8,0,64,63,1,0,0,0,64,65,1,0,0,0,65,11,1,0,
        0,0,66,67,5,4,0,0,67,68,5,5,0,0,68,69,3,24,12,0,69,70,5,6,0,0,70,
        71,5,7,0,0,71,72,3,20,10,0,72,73,5,8,0,0,73,13,1,0,0,0,74,75,5,9,
        0,0,75,76,5,5,0,0,76,77,3,24,12,0,77,78,5,6,0,0,78,79,5,7,0,0,79,
        80,3,20,10,0,80,81,5,8,0,0,81,15,1,0,0,0,82,83,5,10,0,0,83,84,5,
        7,0,0,84,85,3,20,10,0,85,86,5,8,0,0,86,17,1,0,0,0,87,88,5,11,0,0,
        88,89,5,5,0,0,89,90,3,24,12,0,90,91,5,6,0,0,91,92,5,7,0,0,92,93,
        3,20,10,0,93,94,5,8,0,0,94,19,1,0,0,0,95,97,3,2,1,0,96,95,1,0,0,
        0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,21,1,0,0,0,100,98,
        1,0,0,0,101,102,5,12,0,0,102,103,3,26,13,0,103,23,1,0,0,0,104,105,
        3,26,13,0,105,106,5,15,0,0,106,107,3,26,13,0,107,110,1,0,0,0,108,
        110,5,13,0,0,109,104,1,0,0,0,109,108,1,0,0,0,110,25,1,0,0,0,111,
        112,7,0,0,0,112,27,1,0,0,0,6,31,45,60,64,98,109
    ]

class ProgramParser ( Parser ):

    grammarFileName = "Program.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'++'", "'if'", "'('", "')'", 
                     "'{'", "'}'", "'elif'", "'else'", "'while'", "'return '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOLEAN", "VARIABLE", "LOGICAL", "INT", 
                      "FLOAT", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_assignment = 2
    RULE_condition = 3
    RULE_increase = 4
    RULE_block = 5
    RULE_ifBlock = 6
    RULE_elifBlock = 7
    RULE_elseBlock = 8
    RULE_whileLoop = 9
    RULE_body = 10
    RULE_returnStmt = 11
    RULE_logicalExpression = 12
    RULE_val = 13

    ruleNames =  [ "program", "line", "assignment", "condition", "increase", 
                   "block", "ifBlock", "elifBlock", "elseBlock", "whileLoop", 
                   "body", "returnStmt", "logicalExpression", "val" ]

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
    BOOLEAN=13
    VARIABLE=14
    LOGICAL=15
    INT=16
    FLOAT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProgramParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.LineContext)
            else:
                return self.getTypedRuleContext(ProgramParser.LineContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ProgramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22544) != 0):
                self.state = 28
                self.line()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(ProgramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ProgramParser.ConditionContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(ProgramParser.WhileLoopContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(ProgramParser.ReturnStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ProgramParser.AssignmentContext,0)


        def increase(self):
            return self.getTypedRuleContext(ProgramParser.IncreaseContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = ProgramParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 36
                self.assignment()
                self.state = 37
                self.match(ProgramParser.T__0)
                pass

            elif la_ == 2:
                self.state = 39
                self.condition()
                pass

            elif la_ == 3:
                self.state = 40
                self.increase()
                self.state = 41
                self.match(ProgramParser.T__0)
                pass

            elif la_ == 4:
                self.state = 43
                self.whileLoop()
                pass

            elif la_ == 5:
                self.state = 44
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ProgramParser.VARIABLE, 0)

        def val(self):
            return self.getTypedRuleContext(ProgramParser.ValContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ProgramParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ProgramParser.VARIABLE)
            self.state = 48
            self.match(ProgramParser.T__1)
            self.state = 49
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ProgramParser.BlockContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ProgramParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncreaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ProgramParser.VARIABLE, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_increase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrease" ):
                listener.enterIncrease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrease" ):
                listener.exitIncrease(self)




    def increase(self):

        localctx = ProgramParser.IncreaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ProgramParser.VARIABLE)
            self.state = 54
            self.match(ProgramParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifBlock(self):
            return self.getTypedRuleContext(ProgramParser.IfBlockContext,0)


        def elifBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.ElifBlockContext)
            else:
                return self.getTypedRuleContext(ProgramParser.ElifBlockContext,i)


        def elseBlock(self):
            return self.getTypedRuleContext(ProgramParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ProgramParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.ifBlock()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 57
                self.elifBlock()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 63
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self):
            return self.getTypedRuleContext(ProgramParser.LogicalExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(ProgramParser.BodyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)




    def ifBlock(self):

        localctx = ProgramParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ProgramParser.T__3)
            self.state = 67
            self.match(ProgramParser.T__4)
            self.state = 68
            self.logicalExpression()
            self.state = 69
            self.match(ProgramParser.T__5)
            self.state = 70
            self.match(ProgramParser.T__6)
            self.state = 71
            self.body()
            self.state = 72
            self.match(ProgramParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self):
            return self.getTypedRuleContext(ProgramParser.LogicalExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(ProgramParser.BodyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_elifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifBlock" ):
                listener.enterElifBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifBlock" ):
                listener.exitElifBlock(self)




    def elifBlock(self):

        localctx = ProgramParser.ElifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ProgramParser.T__8)
            self.state = 75
            self.match(ProgramParser.T__4)
            self.state = 76
            self.logicalExpression()
            self.state = 77
            self.match(ProgramParser.T__5)
            self.state = 78
            self.match(ProgramParser.T__6)
            self.state = 79
            self.body()
            self.state = 80
            self.match(ProgramParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(ProgramParser.BodyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)




    def elseBlock(self):

        localctx = ProgramParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ProgramParser.T__9)
            self.state = 83
            self.match(ProgramParser.T__6)
            self.state = 84
            self.body()
            self.state = 85
            self.match(ProgramParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self):
            return self.getTypedRuleContext(ProgramParser.LogicalExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(ProgramParser.BodyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = ProgramParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ProgramParser.T__10)
            self.state = 88
            self.match(ProgramParser.T__4)
            self.state = 89
            self.logicalExpression()
            self.state = 90
            self.match(ProgramParser.T__5)
            self.state = 91
            self.match(ProgramParser.T__6)
            self.state = 92
            self.body()
            self.state = 93
            self.match(ProgramParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.LineContext)
            else:
                return self.getTypedRuleContext(ProgramParser.LineContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = ProgramParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22544) != 0):
                self.state = 95
                self.line()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self):
            return self.getTypedRuleContext(ProgramParser.ValContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = ProgramParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ProgramParser.T__11)
            self.state = 102
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.ValContext)
            else:
                return self.getTypedRuleContext(ProgramParser.ValContext,i)


        def LOGICAL(self):
            return self.getToken(ProgramParser.LOGICAL, 0)

        def BOOLEAN(self):
            return self.getToken(ProgramParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)




    def logicalExpression(self):

        localctx = ProgramParser.LogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalExpression)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.val()
                self.state = 105
                self.match(ProgramParser.LOGICAL)
                self.state = 106
                self.val()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(ProgramParser.BOOLEAN)
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


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ProgramParser.VARIABLE, 0)

        def INT(self):
            return self.getToken(ProgramParser.INT, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal" ):
                listener.enterVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal" ):
                listener.exitVal(self)




    def val(self):

        localctx = ProgramParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not(_la==14 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





