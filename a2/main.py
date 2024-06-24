from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from CalculatorListener import CalculatorListener

def calculate(equation):
    input_stream = InputStream(equation.strip())
    lexer = CalculatorLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CalculatorParser(tokens)
    tree = parser.instance()

    listener = CalculatorListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    result = listener.get_result()
    return result

def calculateEquations(url):
    with open(url, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                try:
                    result = calculate(line)
                    print(f"equation: {line.strip()}, result: {result}")
                except Exception as e:
                    print(f"equation: {line.strip()}, error: {e}")

url = 'test.txt'
calculateEquations(url)
