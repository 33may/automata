import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from GramarLexer import GramarLexer
from GramarParser import GramarParser
from antlr4.tree.Tree import TerminalNodeImpl
import graphviz

def to_dot(tree, parser):
    def node_id(node):
        return f"node{id(node)}"

    def escape(s):
        return s.replace('"', '\\"')

    def node_label(node):
        if isinstance(node, TerminalNodeImpl):
            return escape(f"'{node.getText()}'")
        else:
            rule_name = parser.ruleNames[node.getRuleIndex()]
            return escape(rule_name)

    def visit_node(node, dot):
        dot.node(node_id(node), node_label(node))
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            dot.edge(node_id(node), node_id(child))
            visit_node(child, dot)

    dot = graphviz.Digraph()
    visit_node(tree, dot)
    return dot

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = GramarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GramarParser(stream)
    tree = parser.names()

    dot = to_dot(tree, parser)
    dot.render('parse_tree', format='png')
    print("Parse tree saved as 'parse_tree.png'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    main(sys.argv)
