from antlr4 import *
from htmlLexer import htmlLexer
from htmlParser import htmlParser
from htmlVisitor import HtmlVisitor

def main():
    with open("page.html", 'r') as file:
        program = file.read()

    input_stream = InputStream(program)

    lexer = htmlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = htmlParser(stream)
    tree = parser.document()

    visitor = HtmlVisitor()

    # visitor.visitDocument(tree)

    search_term = '.main'
    results = visitor.search(tree, search_term)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
