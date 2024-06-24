# Generated from Program.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ProgramParser import ProgramParser
else:
    from ProgramParser import ProgramParser

# This class defines a complete listener for a parse tree produced by ProgramParser.
class ProgramListener(ParseTreeListener):

    # Enter a parse tree produced by ProgramParser#program.
    def enterProgram(self, ctx:ProgramParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProgramParser#program.
    def exitProgram(self, ctx:ProgramParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProgramParser#line.
    def enterLine(self, ctx:ProgramParser.LineContext):
        pass

    # Exit a parse tree produced by ProgramParser#line.
    def exitLine(self, ctx:ProgramParser.LineContext):
        pass


    # Enter a parse tree produced by ProgramParser#assignment.
    def enterAssignment(self, ctx:ProgramParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProgramParser#assignment.
    def exitAssignment(self, ctx:ProgramParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProgramParser#condition.
    def enterCondition(self, ctx:ProgramParser.ConditionContext):
        pass

    # Exit a parse tree produced by ProgramParser#condition.
    def exitCondition(self, ctx:ProgramParser.ConditionContext):
        pass


    # Enter a parse tree produced by ProgramParser#increase.
    def enterIncrease(self, ctx:ProgramParser.IncreaseContext):
        pass

    # Exit a parse tree produced by ProgramParser#increase.
    def exitIncrease(self, ctx:ProgramParser.IncreaseContext):
        pass


    # Enter a parse tree produced by ProgramParser#block.
    def enterBlock(self, ctx:ProgramParser.BlockContext):
        pass

    # Exit a parse tree produced by ProgramParser#block.
    def exitBlock(self, ctx:ProgramParser.BlockContext):
        pass


    # Enter a parse tree produced by ProgramParser#ifBlock.
    def enterIfBlock(self, ctx:ProgramParser.IfBlockContext):
        pass

    # Exit a parse tree produced by ProgramParser#ifBlock.
    def exitIfBlock(self, ctx:ProgramParser.IfBlockContext):
        pass


    # Enter a parse tree produced by ProgramParser#elifBlock.
    def enterElifBlock(self, ctx:ProgramParser.ElifBlockContext):
        pass

    # Exit a parse tree produced by ProgramParser#elifBlock.
    def exitElifBlock(self, ctx:ProgramParser.ElifBlockContext):
        pass


    # Enter a parse tree produced by ProgramParser#elseBlock.
    def enterElseBlock(self, ctx:ProgramParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ProgramParser#elseBlock.
    def exitElseBlock(self, ctx:ProgramParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ProgramParser#whileLoop.
    def enterWhileLoop(self, ctx:ProgramParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by ProgramParser#whileLoop.
    def exitWhileLoop(self, ctx:ProgramParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by ProgramParser#body.
    def enterBody(self, ctx:ProgramParser.BodyContext):
        pass

    # Exit a parse tree produced by ProgramParser#body.
    def exitBody(self, ctx:ProgramParser.BodyContext):
        pass


    # Enter a parse tree produced by ProgramParser#returnStmt.
    def enterReturnStmt(self, ctx:ProgramParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ProgramParser#returnStmt.
    def exitReturnStmt(self, ctx:ProgramParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ProgramParser#logicalExpression.
    def enterLogicalExpression(self, ctx:ProgramParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by ProgramParser#logicalExpression.
    def exitLogicalExpression(self, ctx:ProgramParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by ProgramParser#val.
    def enterVal(self, ctx:ProgramParser.ValContext):
        pass

    # Exit a parse tree produced by ProgramParser#val.
    def exitVal(self, ctx:ProgramParser.ValContext):
        pass



del ProgramParser