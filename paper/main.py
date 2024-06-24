from antlr4 import *
from htmlLexer import htmlLexer
from htmlParser import htmlParser
from htmlVisitor import HtmlVisitor

def main():
    print("Reading program from page.html")
    with open("page.html", 'r') as file:
        program = file.read()

    input_stream = InputStream(program)

    lexer = htmlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = htmlParser(stream)
    tree = parser.document()

    print("Parsed tree:")
    print(tree.toStringTree(recog=parser))

    visitor = HtmlVisitor()
    visitor.visitDocument(tree)

if __name__ == "__main__":
    main()
