from typing import List, Optional
from bulang.enums.token_type_enum import TokenType
from bulang.models.ast_node import ASTNode
from bulang.models.block import Block
from bulang.models.operators.assignment import Assignment
from bulang.models.operators.binary_op import BinaryOp
from bulang.models.operators.identifier import Identifier
from bulang.models.operators.unray_op import UnaryOp
from bulang.models.program import Program
from bulang.models.statements.if_statement import IfStatement
from bulang.models.statements.print_statement import PrintStatement
from bulang.models.statements.while_statement import WhileStatement
from bulang.models.token import Token
from bulang.models.types.boolean import Boolean
from bulang.models.types.number import Number
from bulang.models.types.string import String
from bulang.models.var_declaration import VarDeclaration


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def error(self, message: str):
        token = self.current_token()
        raise Exception(f"Parser error at line {token.line}: {message}")

    def current_token(self) -> Token:
        if self.pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.pos]

    def peek_token(self, offset: int = 1) -> Token:
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]

    def advance(self) -> Token:
        token = self.current_token()
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token

    def match(self, *types: TokenType) -> bool:
        return self.current_token().type in types

    def consume(self, token_type: TokenType, message: str = "") -> Token:
        if self.current_token().type == token_type:
            return self.advance()
        self.error(message or f"Expected {token_type}")

    def skip_newlines(self):
        while self.match(TokenType.NEWLINE):
            self.advance()

    def parse(self) -> Program:
        statements = []
        self.skip_newlines()

        while not self.match(TokenType.EOF):
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()

        return Program(statements)

    def statement(self) -> Optional[ASTNode]:
        self.skip_newlines()

        if self.match(TokenType.INT, TokenType.STRING_TYPE, TokenType.BOOLEAN_TYPE):
            return self.var_declaration()
        elif self.match(TokenType.IF):
            return self.if_statement()
        elif self.match(TokenType.WHILE):
            return self.while_statement()
        elif self.match(TokenType.PRINT):
            return self.print_statement()
        elif self.match(TokenType.LBRACE):
            return self.block()
        elif self.match(TokenType.IDENTIFIER):
            return self.assignment()
        else:
            expr = self.expression()
            self.consume(TokenType.SEMICOLON, "Expected ';' after expression")
            return expr

    def var_declaration(self) -> VarDeclaration:
        var_type = self.advance().value
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name").value

        value = None
        if self.match(TokenType.ASSIGN):
            self.advance()
            value = self.expression()

        self.consume(TokenType.SEMICOLON, "Expected ';' after variable declaration")
        return VarDeclaration(var_type, name, value)

    def assignment(self) -> Assignment:
        name = self.advance().value
        self.consume(TokenType.ASSIGN, "Expected '=' in assignment")
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after assignment")
        return Assignment(name, value)

    def if_statement(self) -> IfStatement:
        self.advance()
        self.consume(TokenType.LPAREN, "Expected '(' after 'if'")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')' after if condition")

        then_branch = self.statement()
        else_branch = None

        if self.match(TokenType.ELSE):
            self.advance()
            else_branch = self.statement()

        return IfStatement(condition, then_branch, else_branch)

    def while_statement(self) -> WhileStatement:
        self.advance()
        self.consume(TokenType.LPAREN, "Expected '(' after 'while'")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')' after while condition")
        body = self.statement()
        return WhileStatement(condition, body)

    def print_statement(self) -> PrintStatement:
        self.advance()
        self.consume(TokenType.LPAREN, "Expected '(' after 'print'")
        expr = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')' after print expression")
        self.consume(TokenType.SEMICOLON, "Expected ';' after print statement")
        return PrintStatement(expr)

    def block(self) -> Block:
        self.advance()
        statements = []

        self.skip_newlines()
        while not self.match(TokenType.RBRACE) and not self.match(TokenType.EOF):
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()

        self.consume(TokenType.RBRACE, "Expected '}' to close block")
        return Block(statements)

    def expression(self) -> ASTNode:
        return self.logical_or()

    def logical_or(self) -> ASTNode:
        expr = self.logical_and()
        return expr

    def logical_and(self) -> ASTNode:
        expr = self.equality()
        return expr

    def equality(self) -> ASTNode:
        expr = self.comparison()

        while self.match(TokenType.EQUAL, TokenType.NOT_EQUAL):
            operator = self.advance()
            right = self.comparison()
            expr = BinaryOp(expr, operator, right)

        return expr

    def comparison(self) -> ASTNode:
        expr = self.term()

        while self.match(
            TokenType.GREATER_THAN,
            TokenType.GREATER_EQUAL,
            TokenType.LESS_THAN,
            TokenType.LESS_EQUAL,
        ):
            operator = self.advance()
            right = self.term()
            expr = BinaryOp(expr, operator, right)

        return expr

    def term(self) -> ASTNode:
        expr = self.factor()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.advance()
            right = self.factor()
            expr = BinaryOp(expr, operator, right)

        return expr

    def factor(self) -> ASTNode:
        expr = self.unary()

        while self.match(TokenType.MULTIPLY, TokenType.DIVIDE):
            operator = self.advance()
            right = self.unary()
            expr = BinaryOp(expr, operator, right)

        return expr

    def unary(self) -> ASTNode:
        if self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.advance()
            expr = self.unary()
            return UnaryOp(operator, expr)

        return self.primary()

    def primary(self) -> ASTNode:
        if self.match(TokenType.NUMBER):
            value = float(self.advance().value)
            return Number(value)

        if self.match(TokenType.STRING):
            value = self.advance().value
            return String(value)

        if self.match(TokenType.BOOLEAN):
            value = self.advance().value == "true"
            return Boolean(value)

        if self.match(TokenType.IDENTIFIER):
            name = self.advance().value
            return Identifier(name)

        if self.match(TokenType.LPAREN):
            self.advance()
            expr = self.expression()
            self.consume(TokenType.RPAREN, "Expected ')' after expression")
            return expr

        self.error(f"Unexpected token: {self.current_token()}")
