from antlr4 import *
if "." in __name__:
    from .htmlParser import htmlParser
else:
    from htmlParser import htmlParser

class HtmlVisitor(ParseTreeVisitor):
    def __init__(self):
        self.results = []

    def visitDocument(self, ctx:htmlParser.DocumentContext):
        print("Visiting document")
        self.visitHtml(ctx.html())
        return None

    def visitHtml(self, ctx:htmlParser.HtmlContext):
        print("Visiting html: " + self._getInnerHtml(ctx))
        self.visitHead(ctx.head())
        self.visitBody(ctx.body())
        return None

    def visitHead(self, ctx:htmlParser.HeadContext):
        print("Visiting head: " + self._getInnerHtml(ctx))
        for element in ctx.element():
            self.visitElement(element)
        return None

    def visitBody(self, ctx:htmlParser.BodyContext):
        print("Visiting body: " + self._getInnerHtml(ctx))
        for element in ctx.element():
            self.visitElement(element)
        return None

    def visitElement(self, ctx:htmlParser.ElementContext):
        print("Visiting element: " + self._getInnerHtml(ctx))
        if ctx.tag_open():
            self.visitTag_open(ctx.tag_open())
            for child in ctx.children:
                if isinstance(child, htmlParser.ElementContext):
                    self.visitElement(child)
                elif isinstance(child, htmlParser.ContentContext):
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
        print(f"Content: {self._getInnerHtml(ctx)}")
        return None

    def search(self, ctx:htmlParser.DocumentContext, search_term:str):
        self.results = []
        self._searchHelper(ctx, search_term)
        return self.results

    def _searchHelper(self, ctx, search_term):
        if isinstance(ctx, htmlParser.DocumentContext):
            self._searchHelper(ctx.html(), search_term)
        elif isinstance(ctx, htmlParser.HtmlContext):
            self._searchHelper(ctx.head(), search_term)
            self._searchHelper(ctx.body(), search_term)
        elif isinstance(ctx, htmlParser.HeadContext):
            for element in ctx.element():
                self._searchHelper(element, search_term)
        elif isinstance(ctx, htmlParser.BodyContext):
            for element in ctx.element():
                self._searchHelper(element, search_term)
        elif isinstance(ctx, htmlParser.ElementContext):
            if self._matches(ctx, search_term):
                self.results.append(self._getInnerHtml(ctx))
            for child in ctx.children:
                if isinstance(child, htmlParser.ElementContext):
                    self._searchHelper(child, search_term)
                else:
                    self._searchHelper(child, search_term)


    def _matches(self, ctx, search_term):
        if search_term.startswith('#'):
            return self._hasAttribute(ctx, 'id', search_term[1:])
        elif search_term.startswith('.'):
            return self._hasAttribute(ctx, 'class', search_term[1:])
        else:
            return self._isTag(ctx, search_term)

    def _hasAttribute(self, ctx, attr_name, attr_value):
        for attr in ctx.tag_open().attribute():
            name = attr.TEXT().getText()
            value = attr.VALUE().getText().strip('"')
            if name == attr_name and value == attr_value:
                return True
        return False

    def _isTag(self, ctx, tag_name):
        return ctx.tag_open().tag_name().getText() == tag_name

    def _getInnerHtml(self, ctx):
        content = []
        for child in ctx.children:
            if isinstance(child, htmlParser.ElementContext):
                content.append(self._getInnerHtml(child))
            elif isinstance(child, htmlParser.ContentContext):
                seq = []
                for text in child.children:
                    seq.append(text.getText())
                content.extend(seq)
            elif isinstance(child, htmlParser.Tag_openContext):
                tag_str =' '.join([text.getText() for text in child.children])
                content.append(tag_str)
            elif isinstance(child, htmlParser.Tag_closeContext):
                tag_str = ''.join([text.getText() for text in child.children])
                content.append(tag_str)
            else:
                content.append(child.getText())

        final_content = ' '.join(content)
        return final_content