# Generated from html.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .htmlParser import htmlParser
else:
    from htmlParser import htmlParser

# This class defines a complete listener for a parse tree produced by htmlParser.
class htmlListener(ParseTreeListener):

    # Enter a parse tree produced by htmlParser#document.
    def enterDocument(self, ctx:htmlParser.DocumentContext):
        pass

    # Exit a parse tree produced by htmlParser#document.
    def exitDocument(self, ctx:htmlParser.DocumentContext):
        pass


    # Enter a parse tree produced by htmlParser#doctype.
    def enterDoctype(self, ctx:htmlParser.DoctypeContext):
        pass

    # Exit a parse tree produced by htmlParser#doctype.
    def exitDoctype(self, ctx:htmlParser.DoctypeContext):
        pass


    # Enter a parse tree produced by htmlParser#html.
    def enterHtml(self, ctx:htmlParser.HtmlContext):
        pass

    # Exit a parse tree produced by htmlParser#html.
    def exitHtml(self, ctx:htmlParser.HtmlContext):
        pass


    # Enter a parse tree produced by htmlParser#head.
    def enterHead(self, ctx:htmlParser.HeadContext):
        pass

    # Exit a parse tree produced by htmlParser#head.
    def exitHead(self, ctx:htmlParser.HeadContext):
        pass


    # Enter a parse tree produced by htmlParser#body.
    def enterBody(self, ctx:htmlParser.BodyContext):
        pass

    # Exit a parse tree produced by htmlParser#body.
    def exitBody(self, ctx:htmlParser.BodyContext):
        pass


    # Enter a parse tree produced by htmlParser#element.
    def enterElement(self, ctx:htmlParser.ElementContext):
        pass

    # Exit a parse tree produced by htmlParser#element.
    def exitElement(self, ctx:htmlParser.ElementContext):
        pass


    # Enter a parse tree produced by htmlParser#tag_open.
    def enterTag_open(self, ctx:htmlParser.Tag_openContext):
        pass

    # Exit a parse tree produced by htmlParser#tag_open.
    def exitTag_open(self, ctx:htmlParser.Tag_openContext):
        pass


    # Enter a parse tree produced by htmlParser#tag_close.
    def enterTag_close(self, ctx:htmlParser.Tag_closeContext):
        pass

    # Exit a parse tree produced by htmlParser#tag_close.
    def exitTag_close(self, ctx:htmlParser.Tag_closeContext):
        pass


    # Enter a parse tree produced by htmlParser#self_closing_tag.
    def enterSelf_closing_tag(self, ctx:htmlParser.Self_closing_tagContext):
        pass

    # Exit a parse tree produced by htmlParser#self_closing_tag.
    def exitSelf_closing_tag(self, ctx:htmlParser.Self_closing_tagContext):
        pass


    # Enter a parse tree produced by htmlParser#single_tag.
    def enterSingle_tag(self, ctx:htmlParser.Single_tagContext):
        pass

    # Exit a parse tree produced by htmlParser#single_tag.
    def exitSingle_tag(self, ctx:htmlParser.Single_tagContext):
        pass


    # Enter a parse tree produced by htmlParser#attribute.
    def enterAttribute(self, ctx:htmlParser.AttributeContext):
        pass

    # Exit a parse tree produced by htmlParser#attribute.
    def exitAttribute(self, ctx:htmlParser.AttributeContext):
        pass


    # Enter a parse tree produced by htmlParser#content.
    def enterContent(self, ctx:htmlParser.ContentContext):
        pass

    # Exit a parse tree produced by htmlParser#content.
    def exitContent(self, ctx:htmlParser.ContentContext):
        pass


    # Enter a parse tree produced by htmlParser#tag_name.
    def enterTag_name(self, ctx:htmlParser.Tag_nameContext):
        pass

    # Exit a parse tree produced by htmlParser#tag_name.
    def exitTag_name(self, ctx:htmlParser.Tag_nameContext):
        pass



del htmlParser