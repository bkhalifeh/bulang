from bulang.enums.token_type_enum import TokenType


class Token:
    def __init__(self, type_: TokenType, value: str, line: int = 0):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type}, {self.value})"
