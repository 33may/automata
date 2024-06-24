from antlr4 import *
from ProgramLexer import ProgramLexer
from ProgramParser import ProgramParser
from ProgramVisitor import ProgramVisitor


def evaluateProgram(file_path):
    print(f"Reading program from {file_path}")
    with open(file_path, 'r') as file:
        program = file.read()

    print("Program read successfully:")
    print(program)

    input_stream = InputStream(program.strip())
    lexer = ProgramLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ProgramParser(tokens)
    tree = parser.program()

    visitor = ProgramVisitor()
    visitor.visitProgram(tree)


if __name__ == "__main__":
    # Specify the path to your input file
    file_path = 'code.txt'
    evaluateProgram(file_path)
