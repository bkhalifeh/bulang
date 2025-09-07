from enum import StrEnum


class TokenType(StrEnum):
    NUMBER = "NUMBER"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    IDENTIFIER = "IDENTIFIER"

    INT = "int"
    STRING_TYPE = "string"
    BOOLEAN_TYPE = "boolean"
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    FOR = "for"
    FUNCTION = "function"
    RETURN = "return"
    TRUE = "true"
    FALSE = "false"
    PRINT = "print"

    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_THAN = "<"
    GREATER_THAN = ">"
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    SEMICOLON = ";"
    COMMA = ","

    NEWLINE = "NEWLINE"
    EOF = "EOF"
