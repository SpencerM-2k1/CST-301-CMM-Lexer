# Generated from CMM.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CMMParser import CMMParser
else:
    from CMMParser import CMMParser

# This class defines a complete listener for a parse tree produced by CMMParser.
class CMMListener(ParseTreeListener):

    # Enter a parse tree produced by CMMParser#program.
    def enterProgram(self, ctx:CMMParser.ProgramContext):
        pass

    # Exit a parse tree produced by CMMParser#program.
    def exitProgram(self, ctx:CMMParser.ProgramContext):
        pass


    # Enter a parse tree produced by CMMParser#varDeclList.
    def enterVarDeclList(self, ctx:CMMParser.VarDeclListContext):
        pass

    # Exit a parse tree produced by CMMParser#varDeclList.
    def exitVarDeclList(self, ctx:CMMParser.VarDeclListContext):
        pass


    # Enter a parse tree produced by CMMParser#varDecl.
    def enterVarDecl(self, ctx:CMMParser.VarDeclContext):
        pass

    # Exit a parse tree produced by CMMParser#varDecl.
    def exitVarDecl(self, ctx:CMMParser.VarDeclContext):
        pass


    # Enter a parse tree produced by CMMParser#funDeclList.
    def enterFunDeclList(self, ctx:CMMParser.FunDeclListContext):
        pass

    # Exit a parse tree produced by CMMParser#funDeclList.
    def exitFunDeclList(self, ctx:CMMParser.FunDeclListContext):
        pass


    # Enter a parse tree produced by CMMParser#funDecl.
    def enterFunDecl(self, ctx:CMMParser.FunDeclContext):
        pass

    # Exit a parse tree produced by CMMParser#funDecl.
    def exitFunDecl(self, ctx:CMMParser.FunDeclContext):
        pass


    # Enter a parse tree produced by CMMParser#paramDeclList.
    def enterParamDeclList(self, ctx:CMMParser.ParamDeclListContext):
        pass

    # Exit a parse tree produced by CMMParser#paramDeclList.
    def exitParamDeclList(self, ctx:CMMParser.ParamDeclListContext):
        pass


    # Enter a parse tree produced by CMMParser#paramDecl.
    def enterParamDecl(self, ctx:CMMParser.ParamDeclContext):
        pass

    # Exit a parse tree produced by CMMParser#paramDecl.
    def exitParamDecl(self, ctx:CMMParser.ParamDeclContext):
        pass


    # Enter a parse tree produced by CMMParser#block.
    def enterBlock(self, ctx:CMMParser.BlockContext):
        pass

    # Exit a parse tree produced by CMMParser#block.
    def exitBlock(self, ctx:CMMParser.BlockContext):
        pass


    # Enter a parse tree produced by CMMParser#type.
    def enterType(self, ctx:CMMParser.TypeContext):
        pass

    # Exit a parse tree produced by CMMParser#type.
    def exitType(self, ctx:CMMParser.TypeContext):
        pass


    # Enter a parse tree produced by CMMParser#stmtList.
    def enterStmtList(self, ctx:CMMParser.StmtListContext):
        pass

    # Exit a parse tree produced by CMMParser#stmtList.
    def exitStmtList(self, ctx:CMMParser.StmtListContext):
        pass


    # Enter a parse tree produced by CMMParser#stmt.
    def enterStmt(self, ctx:CMMParser.StmtContext):
        pass

    # Exit a parse tree produced by CMMParser#stmt.
    def exitStmt(self, ctx:CMMParser.StmtContext):
        pass


    # Enter a parse tree produced by CMMParser#expr.
    def enterExpr(self, ctx:CMMParser.ExprContext):
        pass

    # Exit a parse tree produced by CMMParser#expr.
    def exitExpr(self, ctx:CMMParser.ExprContext):
        pass


    # Enter a parse tree produced by CMMParser#primary.
    def enterPrimary(self, ctx:CMMParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CMMParser#primary.
    def exitPrimary(self, ctx:CMMParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CMMParser#exprList.
    def enterExprList(self, ctx:CMMParser.ExprListContext):
        pass

    # Exit a parse tree produced by CMMParser#exprList.
    def exitExprList(self, ctx:CMMParser.ExprListContext):
        pass


    # Enter a parse tree produced by CMMParser#unaryOp.
    def enterUnaryOp(self, ctx:CMMParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by CMMParser#unaryOp.
    def exitUnaryOp(self, ctx:CMMParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by CMMParser#binOp.
    def enterBinOp(self, ctx:CMMParser.BinOpContext):
        pass

    # Exit a parse tree produced by CMMParser#binOp.
    def exitBinOp(self, ctx:CMMParser.BinOpContext):
        pass



del CMMParser