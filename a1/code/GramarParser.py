# Generated from Gramar.g4 by ANTLR 4.13.1
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
        4,1,8,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,12,
        0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,50,0,22,1,0,0,0,2,32,
        1,0,0,0,4,35,1,0,0,0,6,42,1,0,0,0,8,45,1,0,0,0,10,48,1,0,0,0,12,
        50,1,0,0,0,14,52,1,0,0,0,16,54,1,0,0,0,18,56,1,0,0,0,20,58,1,0,0,
        0,22,27,3,2,1,0,23,24,5,1,0,0,24,26,3,2,1,0,25,23,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,
        30,31,5,0,0,1,31,1,1,0,0,0,32,33,3,4,2,0,33,34,3,8,4,0,34,3,1,0,
        0,0,35,36,3,6,3,0,36,37,5,2,0,0,37,38,3,18,9,0,38,39,5,3,0,0,39,
        40,3,20,10,0,40,41,5,4,0,0,41,5,1,0,0,0,42,43,3,10,5,0,43,44,3,12,
        6,0,44,7,1,0,0,0,45,46,3,14,7,0,46,47,3,16,8,0,47,9,1,0,0,0,48,49,
        5,6,0,0,49,11,1,0,0,0,50,51,5,6,0,0,51,13,1,0,0,0,52,53,5,6,0,0,
        53,15,1,0,0,0,54,55,5,5,0,0,55,17,1,0,0,0,56,57,5,5,0,0,57,19,1,
        0,0,0,58,59,5,7,0,0,59,21,1,0,0,0,1,27
    ]

class GramarParser ( Parser ):

    grammarFileName = "Gramar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DIGITS", "STRING", "PHONE", "WS" ]

    RULE_names = 0
    RULE_transaction = 1
    RULE_person = 2
    RULE_name = 3
    RULE_operation = 4
    RULE_firstName = 5
    RULE_lastName = 6
    RULE_type = 7
    RULE_ammount = 8
    RULE_age = 9
    RULE_phone = 10

    ruleNames =  [ "names", "transaction", "person", "name", "operation", 
                   "firstName", "lastName", "type", "ammount", "age", "phone" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    DIGITS=5
    STRING=6
    PHONE=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NamesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GramarParser.EOF, 0)

        def transaction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramarParser.TransactionContext)
            else:
                return self.getTypedRuleContext(GramarParser.TransactionContext,i)


        def getRuleIndex(self):
            return GramarParser.RULE_names

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNames" ):
                listener.enterNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNames" ):
                listener.exitNames(self)




    def names(self):

        localctx = GramarParser.NamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.transaction()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 23
                self.match(GramarParser.T__0)
                self.state = 24
                self.transaction()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(GramarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def person(self):
            return self.getTypedRuleContext(GramarParser.PersonContext,0)


        def operation(self):
            return self.getTypedRuleContext(GramarParser.OperationContext,0)


        def getRuleIndex(self):
            return GramarParser.RULE_transaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransaction" ):
                listener.enterTransaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransaction" ):
                listener.exitTransaction(self)




    def transaction(self):

        localctx = GramarParser.TransactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_transaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.person()
            self.state = 33
            self.operation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PersonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(GramarParser.NameContext,0)


        def age(self):
            return self.getTypedRuleContext(GramarParser.AgeContext,0)


        def phone(self):
            return self.getTypedRuleContext(GramarParser.PhoneContext,0)


        def getRuleIndex(self):
            return GramarParser.RULE_person

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerson" ):
                listener.enterPerson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerson" ):
                listener.exitPerson(self)




    def person(self):

        localctx = GramarParser.PersonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_person)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.name()
            self.state = 36
            self.match(GramarParser.T__1)
            self.state = 37
            self.age()
            self.state = 38
            self.match(GramarParser.T__2)
            self.state = 39
            self.phone()
            self.state = 40
            self.match(GramarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def firstName(self):
            return self.getTypedRuleContext(GramarParser.FirstNameContext,0)


        def lastName(self):
            return self.getTypedRuleContext(GramarParser.LastNameContext,0)


        def getRuleIndex(self):
            return GramarParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = GramarParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.firstName()
            self.state = 43
            self.lastName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GramarParser.TypeContext,0)


        def ammount(self):
            return self.getTypedRuleContext(GramarParser.AmmountContext,0)


        def getRuleIndex(self):
            return GramarParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = GramarParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.type_()
            self.state = 46
            self.ammount()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FirstNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GramarParser.STRING, 0)

        def getRuleIndex(self):
            return GramarParser.RULE_firstName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirstName" ):
                listener.enterFirstName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirstName" ):
                listener.exitFirstName(self)




    def firstName(self):

        localctx = GramarParser.FirstNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_firstName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(GramarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GramarParser.STRING, 0)

        def getRuleIndex(self):
            return GramarParser.RULE_lastName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastName" ):
                listener.enterLastName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastName" ):
                listener.exitLastName(self)




    def lastName(self):

        localctx = GramarParser.LastNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lastName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(GramarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GramarParser.STRING, 0)

        def getRuleIndex(self):
            return GramarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = GramarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GramarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AmmountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(GramarParser.DIGITS, 0)

        def getRuleIndex(self):
            return GramarParser.RULE_ammount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmmount" ):
                listener.enterAmmount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmmount" ):
                listener.exitAmmount(self)




    def ammount(self):

        localctx = GramarParser.AmmountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ammount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(GramarParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(GramarParser.DIGITS, 0)

        def getRuleIndex(self):
            return GramarParser.RULE_age

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAge" ):
                listener.enterAge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAge" ):
                listener.exitAge(self)




    def age(self):

        localctx = GramarParser.AgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_age)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(GramarParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhoneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PHONE(self):
            return self.getToken(GramarParser.PHONE, 0)

        def getRuleIndex(self):
            return GramarParser.RULE_phone

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhone" ):
                listener.enterPhone(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhone" ):
                listener.exitPhone(self)




    def phone(self):

        localctx = GramarParser.PhoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_phone)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(GramarParser.PHONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





