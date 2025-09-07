from typing import List

from bulang.enums.token_type_enum import TokenType
from bulang.models.token import Token


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.tokens = []

    def error(self, message: str):
        raise Exception(f"Lexer error at line {self.line}: {message}")

    def peek(self, offset: int = 0) -> str:
        pos = self.pos + offset
        if pos >= len(self.text):
            return "\0"
        return self.text[pos]

    def advance(self) -> str:
        if self.pos >= len(self.text):
            return "\0"
        char = self.text[self.pos]
        self.pos += 1
        if char == "\n":
            self.line += 1
        return char

    def skip_whitespace(self):
        while self.peek() in " \t\r":
            self.advance()

    def read_number(self) -> str:
        result = ""
        while self.peek().isdigit() or self.peek() == ".":
            result += self.advance()
        return result

    def read_string(self) -> str:
        result = ""
        self.advance()
        while self.peek() != '"' and self.peek() != "\0":
            result += self.advance()
        if self.peek() == '"':
            self.advance()
        return result

    def read_identifier(self) -> str:
        result = ""
        while self.peek().isalnum() or self.peek() == "_":
            result += self.advance()
        return result

    def tokenize(self) -> List[Token]:
        keywords = {
            "int": TokenType.INT,
            "string": TokenType.STRING_TYPE,
            "boolean": TokenType.BOOLEAN_TYPE,
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "while": TokenType.WHILE,
            "for": TokenType.FOR,
            "function": TokenType.FUNCTION,
            "return": TokenType.RETURN,
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "print": TokenType.PRINT,
        }

        while self.pos < len(self.text):
            self.skip_whitespace()

            if self.pos >= len(self.text):
                break

            char = self.peek()

            if char == "\n":
                self.tokens.append(Token(TokenType.NEWLINE, char, self.line))
                self.advance()
            elif char.isdigit():
                self.tokens.append(
                    Token(TokenType.NUMBER, self.read_number(), self.line)
                )
            elif char == '"':
                self.tokens.append(
                    Token(TokenType.STRING, self.read_string(), self.line)
                )
            elif char.isalpha() or char == "_":
                identifier = self.read_identifier()
                token_type = keywords.get(identifier, TokenType.IDENTIFIER)
                if token_type in [TokenType.TRUE, TokenType.FALSE]:
                    token_type = TokenType.BOOLEAN
                self.tokens.append(Token(token_type, identifier, self.line))
            elif char == "=":
                self.advance()
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token(TokenType.EQUAL, "==", self.line))
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, "=", self.line))
            elif char == "!":
                self.advance()
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token(TokenType.NOT_EQUAL, "!=", self.line))
            elif char == "<":
                self.advance()
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token(TokenType.LESS_EQUAL, "<=", self.line))
                else:
                    self.tokens.append(Token(TokenType.LESS_THAN, "<", self.line))
            elif char == ">":
                self.advance()
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, ">=", self.line))
                else:
                    self.tokens.append(Token(TokenType.GREATER_THAN, ">", self.line))
            elif char == "+":
                self.tokens.append(Token(TokenType.PLUS, char, self.line))
                self.advance()
            elif char == "-":
                self.tokens.append(Token(TokenType.MINUS, char, self.line))
                self.advance()
            elif char == "*":
                self.tokens.append(Token(TokenType.MULTIPLY, char, self.line))
                self.advance()
            elif char == "/":
                self.tokens.append(Token(TokenType.DIVIDE, char, self.line))
                self.advance()
            elif char == "(":
                self.tokens.append(Token(TokenType.LPAREN, char, self.line))
                self.advance()
            elif char == ")":
                self.tokens.append(Token(TokenType.RPAREN, char, self.line))
                self.advance()
            elif char == "{":
                self.tokens.append(Token(TokenType.LBRACE, char, self.line))
                self.advance()
            elif char == "}":
                self.tokens.append(Token(TokenType.RBRACE, char, self.line))
                self.advance()
            elif char == ";":
                self.tokens.append(Token(TokenType.SEMICOLON, char, self.line))
                self.advance()
            elif char == ",":
                self.tokens.append(Token(TokenType.COMMA, char, self.line))
                self.advance()
            else:
                self.error(f"Unexpected character: {char}")

        self.tokens.append(Token(TokenType.EOF, "", self.line))
        return self.tokens
