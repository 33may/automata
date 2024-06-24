# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

class CalculatorListener(ParseTreeListener):

    def __init__(self):
        self.stack = []
    def enterInstance(self, ctx:CalculatorParser.InstanceContext):
        pass

    def exitInstance(self, ctx:CalculatorParser.InstanceContext):
        pass


    def enterExpr(self, ctx:CalculatorParser.ExprContext):
        pass

    def exitExpr(self, ctx:CalculatorParser.ExprContext):
        if ctx.getChildCount() == 1:
            return
        else:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '+':
                self.stack.append(left + right)
            elif op == '-':
                self.stack.append(left - right)


    def enterTerm(self, ctx:CalculatorParser.TermContext):
        pass

    def exitTerm(self, ctx:CalculatorParser.TermContext):
        if ctx.getChildCount() == 1:
            return
        else:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '*':
                self.stack.append(left * right)
            elif op == '/':
                self.stack.append(left / right)


    def enterFactor(self, ctx:CalculatorParser.FactorContext):
        pass

    def exitFactor(self, ctx:CalculatorParser.FactorContext):
        if ctx.getChildCount() == 1:
            if ctx.INT():
                val = int(ctx.INT().getText())
                self.stack.append(val)
            elif ctx.FLOAT():
                val = float(ctx.FLOAT().getText())
                self.stack.append(val)
        elif ctx.getChildCount() == 3:
            return

    def get_result(self):
        return self.stack.pop()

del CalculatorParser