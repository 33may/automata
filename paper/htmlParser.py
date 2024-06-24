# Generated from html.g4 by ANTLR 4.13.1
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
        4,1,16,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,3,0,
        28,8,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,5,3,42,8,
        3,10,3,12,3,45,9,3,1,3,1,3,1,4,1,4,5,4,51,8,4,10,4,12,4,54,9,4,1,
        4,1,4,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,5,1,5,1,5,1,5,3,
        5,70,8,5,1,6,1,6,1,6,5,6,75,8,6,10,6,12,6,78,9,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,5,8,89,8,8,10,8,12,8,92,9,8,1,8,1,8,1,9,1,9,
        1,9,5,9,99,8,9,10,9,12,9,102,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,
        4,11,111,8,11,11,11,12,11,112,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,
        12,14,16,18,20,22,24,0,1,1,0,13,14,114,0,27,1,0,0,0,2,32,1,0,0,0,
        4,34,1,0,0,0,6,39,1,0,0,0,8,48,1,0,0,0,10,69,1,0,0,0,12,71,1,0,0,
        0,14,81,1,0,0,0,16,85,1,0,0,0,18,95,1,0,0,0,20,105,1,0,0,0,22,110,
        1,0,0,0,24,114,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,27,28,1,0,0,0,
        28,29,1,0,0,0,29,30,3,4,2,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,
        0,0,33,3,1,0,0,0,34,35,5,2,0,0,35,36,3,6,3,0,36,37,3,8,4,0,37,38,
        5,3,0,0,38,5,1,0,0,0,39,43,5,4,0,0,40,42,3,10,5,0,41,40,1,0,0,0,
        42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,
        0,0,0,46,47,5,5,0,0,47,7,1,0,0,0,48,52,5,6,0,0,49,51,3,10,5,0,50,
        49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,
        0,54,52,1,0,0,0,55,56,5,7,0,0,56,9,1,0,0,0,57,62,3,12,6,0,58,61,
        3,22,11,0,59,61,3,10,5,0,60,58,1,0,0,0,60,59,1,0,0,0,61,64,1,0,0,
        0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,
        3,14,7,0,66,70,1,0,0,0,67,70,3,16,8,0,68,70,3,18,9,0,69,57,1,0,0,
        0,69,67,1,0,0,0,69,68,1,0,0,0,70,11,1,0,0,0,71,72,5,8,0,0,72,76,
        3,24,12,0,73,75,3,20,10,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,
        0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,9,0,0,80,13,
        1,0,0,0,81,82,5,10,0,0,82,83,3,24,12,0,83,84,5,9,0,0,84,15,1,0,0,
        0,85,86,5,8,0,0,86,90,3,24,12,0,87,89,3,20,10,0,88,87,1,0,0,0,89,
        92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,
        0,93,94,5,11,0,0,94,17,1,0,0,0,95,96,5,8,0,0,96,100,3,24,12,0,97,
        99,3,20,10,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,
        1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,9,0,0,104,19,1,
        0,0,0,105,106,5,14,0,0,106,107,5,12,0,0,107,108,5,15,0,0,108,21,
        1,0,0,0,109,111,7,0,0,0,110,109,1,0,0,0,111,112,1,0,0,0,112,110,
        1,0,0,0,112,113,1,0,0,0,113,23,1,0,0,0,114,115,7,0,0,0,115,25,1,
        0,0,0,10,27,43,52,60,62,69,76,90,100,112
    ]

class htmlParser ( Parser ):

    grammarFileName = "html.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<!DOCTYPE html>'", "'<html>'", "'</html>'", 
                     "'<head>'", "'</head>'", "'<body>'", "'</body>'", "'<'", 
                     "'>'", "'</'", "'/>'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "KNOWN_TAG", "TEXT", "VALUE", "WS" ]

    RULE_document = 0
    RULE_doctype = 1
    RULE_html = 2
    RULE_head = 3
    RULE_body = 4
    RULE_element = 5
    RULE_tag_open = 6
    RULE_tag_close = 7
    RULE_self_closing_tag = 8
    RULE_single_tag = 9
    RULE_attribute = 10
    RULE_content = 11
    RULE_tag_name = 12

    ruleNames =  [ "document", "doctype", "html", "head", "body", "element", 
                   "tag_open", "tag_close", "self_closing_tag", "single_tag", 
                   "attribute", "content", "tag_name" ]

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
    KNOWN_TAG=13
    TEXT=14
    VALUE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def html(self):
            return self.getTypedRuleContext(htmlParser.HtmlContext,0)


        def EOF(self):
            return self.getToken(htmlParser.EOF, 0)

        def doctype(self):
            return self.getTypedRuleContext(htmlParser.DoctypeContext,0)


        def getRuleIndex(self):
            return htmlParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = htmlParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 26
                self.doctype()


            self.state = 29
            self.html()
            self.state = 30
            self.match(htmlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return htmlParser.RULE_doctype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoctype" ):
                listener.enterDoctype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoctype" ):
                listener.exitDoctype(self)




    def doctype(self):

        localctx = htmlParser.DoctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_doctype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(htmlParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(htmlParser.HeadContext,0)


        def body(self):
            return self.getTypedRuleContext(htmlParser.BodyContext,0)


        def getRuleIndex(self):
            return htmlParser.RULE_html

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtml" ):
                listener.enterHtml(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtml" ):
                listener.exitHtml(self)




    def html(self):

        localctx = htmlParser.HtmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(htmlParser.T__1)
            self.state = 35
            self.head()
            self.state = 36
            self.body()
            self.state = 37
            self.match(htmlParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.ElementContext)
            else:
                return self.getTypedRuleContext(htmlParser.ElementContext,i)


        def getRuleIndex(self):
            return htmlParser.RULE_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)




    def head(self):

        localctx = htmlParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(htmlParser.T__3)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 40
                self.element()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(htmlParser.T__4)
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

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.ElementContext)
            else:
                return self.getTypedRuleContext(htmlParser.ElementContext,i)


        def getRuleIndex(self):
            return htmlParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = htmlParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(htmlParser.T__5)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 49
                self.element()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(htmlParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_open(self):
            return self.getTypedRuleContext(htmlParser.Tag_openContext,0)


        def tag_close(self):
            return self.getTypedRuleContext(htmlParser.Tag_closeContext,0)


        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.ContentContext)
            else:
                return self.getTypedRuleContext(htmlParser.ContentContext,i)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.ElementContext)
            else:
                return self.getTypedRuleContext(htmlParser.ElementContext,i)


        def self_closing_tag(self):
            return self.getTypedRuleContext(htmlParser.Self_closing_tagContext,0)


        def single_tag(self):
            return self.getTypedRuleContext(htmlParser.Single_tagContext,0)


        def getRuleIndex(self):
            return htmlParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = htmlParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.tag_open()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24832) != 0):
                    self.state = 60
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [13, 14]:
                        self.state = 58
                        self.content()
                        pass
                    elif token in [8]:
                        self.state = 59
                        self.element()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.tag_close()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.self_closing_tag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.single_tag()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_openContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_name(self):
            return self.getTypedRuleContext(htmlParser.Tag_nameContext,0)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(htmlParser.AttributeContext,i)


        def getRuleIndex(self):
            return htmlParser.RULE_tag_open

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_open" ):
                listener.enterTag_open(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_open" ):
                listener.exitTag_open(self)




    def tag_open(self):

        localctx = htmlParser.Tag_openContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tag_open)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(htmlParser.T__7)
            self.state = 72
            self.tag_name()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 73
                self.attribute()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(htmlParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_closeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_name(self):
            return self.getTypedRuleContext(htmlParser.Tag_nameContext,0)


        def getRuleIndex(self):
            return htmlParser.RULE_tag_close

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_close" ):
                listener.enterTag_close(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_close" ):
                listener.exitTag_close(self)




    def tag_close(self):

        localctx = htmlParser.Tag_closeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tag_close)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(htmlParser.T__9)
            self.state = 82
            self.tag_name()
            self.state = 83
            self.match(htmlParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Self_closing_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_name(self):
            return self.getTypedRuleContext(htmlParser.Tag_nameContext,0)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(htmlParser.AttributeContext,i)


        def getRuleIndex(self):
            return htmlParser.RULE_self_closing_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelf_closing_tag" ):
                listener.enterSelf_closing_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelf_closing_tag" ):
                listener.exitSelf_closing_tag(self)




    def self_closing_tag(self):

        localctx = htmlParser.Self_closing_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_self_closing_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(htmlParser.T__7)
            self.state = 86
            self.tag_name()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 87
                self.attribute()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(htmlParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_name(self):
            return self.getTypedRuleContext(htmlParser.Tag_nameContext,0)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(htmlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(htmlParser.AttributeContext,i)


        def getRuleIndex(self):
            return htmlParser.RULE_single_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_tag" ):
                listener.enterSingle_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_tag" ):
                listener.exitSingle_tag(self)




    def single_tag(self):

        localctx = htmlParser.Single_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_single_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(htmlParser.T__7)
            self.state = 96
            self.tag_name()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 97
                self.attribute()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(htmlParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(htmlParser.TEXT, 0)

        def VALUE(self):
            return self.getToken(htmlParser.VALUE, 0)

        def getRuleIndex(self):
            return htmlParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = htmlParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(htmlParser.TEXT)
            self.state = 106
            self.match(htmlParser.T__11)
            self.state = 107
            self.match(htmlParser.VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(htmlParser.TEXT)
            else:
                return self.getToken(htmlParser.TEXT, i)

        def KNOWN_TAG(self, i:int=None):
            if i is None:
                return self.getTokens(htmlParser.KNOWN_TAG)
            else:
                return self.getToken(htmlParser.KNOWN_TAG, i)

        def getRuleIndex(self):
            return htmlParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = htmlParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 109
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 112 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KNOWN_TAG(self):
            return self.getToken(htmlParser.KNOWN_TAG, 0)

        def TEXT(self):
            return self.getToken(htmlParser.TEXT, 0)

        def getRuleIndex(self):
            return htmlParser.RULE_tag_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_name" ):
                listener.enterTag_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_name" ):
                listener.exitTag_name(self)




    def tag_name(self):

        localctx = htmlParser.Tag_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tag_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
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





