from antlr4 import *
if "." in __name__:
    from .htmlParser import htmlParser
else:
    from htmlParser import htmlParser

class HtmlVisitor(ParseTreeVisitor):
    def __init__(self):
        self.a = 33

    def visitDocument(self, ctx:htmlParser.DocumentContext):
        print("Visiting document")
        if ctx.doctype():
            self.visitDoctype(ctx.doctype())
        if ctx.html():
            self.visitHtml(ctx.html())
        return None

    def visitDoctype(self, ctx:htmlParser.DoctypeContext):
        print("Visiting doctype: " + ctx.getText())
        return None

    def visitHtml(self, ctx:htmlParser.HtmlContext):
        print("Visiting html: " + ctx.getText())
        self.visitHead(ctx.head())
        self.visitBody(ctx.body())
        return None

    def visitHead(self, ctx:htmlParser.HeadContext):
        print("Visiting head: " + ctx.getText())
        for element in ctx.element():
            self.visitElement(element)
        return None

    def visitBody(self, ctx:htmlParser.BodyContext):
        print("Visiting body: " + ctx.getText())
        for element in ctx.element():
            self.visitElement(element)
        return None

    def visitElement(self, ctx:htmlParser.ElementContext):
        print("Visiting element: " + ctx.getText())
        if ctx.tag_open():
            self.visitTag_open(ctx.tag_open())
            for child in ctx.content():
                if isinstance(child, htmlParser.ElementContext):
                    self.visitElement(child)
                else:
                    self.visitContent(child)
            self.visitTag_close(ctx.tag_close())
        elif ctx.self_closing_tag():
            self.visitSelf_closing_tag(ctx.self_closing_tag())
        elif ctx.single_tag():
            self.visitSingle_tag(ctx.single_tag())
        return None

    def visitTag_open(self, ctx:htmlParser.Tag_openContext):
        tag_name = ctx.tag_name().getText()
        print(f"Opening tag: {tag_name}")
        for attr in ctx.attribute():
            self.visitAttribute(attr)
        return None

    def visitTag_close(self, ctx:htmlParser.Tag_closeContext):
        tag_name = ctx.tag_name().getText()
        print(f"Closing tag: {tag_name}")
        return None

    def visitSelf_closing_tag(self, ctx:htmlParser.Self_closing_tagContext):
        tag_name = ctx.tag_name().getText()
        print(f"Self-closing tag: {tag_name}")
        for attr in ctx.attribute():
            self.visitAttribute(attr)
        return None

    def visitSingle_tag(self, ctx:htmlParser.Single_tagContext):
        tag_name = ctx.tag_name().getText()
        print(f"Single tag: {tag_name}")
        for attr in ctx.attribute():
            self.visitAttribute(attr)
        return None

    def visitAttribute(self, ctx:htmlParser.AttributeContext):
        attr_name = ctx.TEXT().getText()
        attr_value = ctx.VALUE().getText()
        print(f"Attribute: {attr_name} = {attr_value}")
        return None

    def visitContent(self, ctx:htmlParser.ContentContext):
        text = ctx.getText()
        print(f"Content: {text}")
        return None
