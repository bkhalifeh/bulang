from bulang.models.ast_node import ASTNode


class Identifier(ASTNode):
    def __init__(self, name: str):
        self.name = name
