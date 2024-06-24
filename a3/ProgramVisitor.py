from antlr4 import *
if "." in __name__:
    from .ProgramParser import ProgramParser
else:
    from ProgramParser import ProgramParser

class ProgramVisitor(ParseTreeVisitor):

    def __init__(self):
        self.memory = {}
        self.test = 0

    def visitProgram(self, ctx:ProgramParser.ProgramContext):
        for line in ctx.line():
            self.visitLine(line)
        return None

    def visitLine(self, ctx:ProgramParser.LineContext):
        if ctx.assignment():
            self.visitAssignment(ctx.assignment())
        elif ctx.condition():
            self.visitCondition(ctx.condition())
        elif ctx.increase():
            self.visitIncrease(ctx.increase())
        elif ctx.whileLoop():
            self.visitWhileLoop(ctx.whileLoop())
        elif ctx.returnStmt():
            self.visitReturnStmt(ctx.returnStmt())
        self.test += 1
        return None

    def visitCondition(self, ctx:ProgramParser.ConditionContext):
        self.visitBlock(ctx.block())
    def visitAssignment(self, ctx:ProgramParser.AssignmentContext):
        variable = ctx.VARIABLE().getText()
        value = self.visitVal(ctx.val())
        self.memory[variable] = value
        return None

    def visitIncrease(self, ctx:ProgramParser.IncreaseContext):
        variable = ctx.VARIABLE().getText()
        if variable in self.memory:
            self.memory[variable] += 1
        else:
            raise Exception(f"Undefined variable: {variable}")
        return None

    def visitWhileLoop(self, ctx:ProgramParser.WhileLoopContext):
        while self.visitLogicalExpression(ctx.logicalExpression()):
            self.visitBody(ctx.body())
        return None

    def visitReturnStmt(self, ctx:ProgramParser.ReturnStmtContext):
        value = self.visitVal(ctx.val())
        print('Return:', value)
        return value

    def visitVal(self, ctx:ProgramParser.ValContext):
        if ctx.INT():
            result = int(ctx.INT().getText())
        elif ctx.VARIABLE():
            variable_name = ctx.VARIABLE().getText()
            if variable_name in self.memory:
                result = self.memory[variable_name]
            else:
                raise Exception(f"Undefined variable: {variable_name}")
        return result

    def visitLogicalExpression(self, ctx:ProgramParser.LogicalExpressionContext):
        if ctx.BOOLEAN():
            result = ctx.BOOLEAN().getText() == 'True'
        else:
            left = self.visitVal(ctx.val(0))
            right = self.visitVal(ctx.val(1))
            op = ctx.LOGICAL().getText()
            if op == '>':
                result = left > right
            elif op == '<':
                result = left < right
            elif op == '>=':
                result = left >= right
            elif op == '<=':
                result = left <= right
            elif op == '==':
                result = left == right
        return result

    def visitBlock(self, ctx: ProgramParser.BlockContext):
        if self.visitLogicalExpression(ctx.ifBlock().logicalExpression()):
            self.visitBody(ctx.ifBlock().body())
            return None

        for elifBlock in ctx.elifBlock():
            if self.visitLogicalExpression(elifBlock.logicalExpression()):
                self.visitBody(elifBlock.body())
                return None

        if ctx.elseBlock():
            self.visitBody(ctx.elseBlock().body())

        return None


    def visitBody(self, ctx:ProgramParser.BodyContext):
        for line in ctx.line():
            self.visitLine(line)
        return None

    def visitIfBlock(self, ctx:ProgramParser.IfBlockContext):
        result = self.visitChildren(ctx)
        return result

    def visitElifBlock(self, ctx:ProgramParser.ElifBlockContext):
        result = self.visitChildren(ctx)
        return result

    def visitElseBlock(self, ctx:ProgramParser.ElseBlockContext):
        result = self.visitChildren(ctx)
        return result

    def get_memory(self):
        return self.test

del ProgramParser
