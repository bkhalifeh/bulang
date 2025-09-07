from bulang.models.ast_node import ASTNode


class String(ASTNode):
    def __init__(self, value: str):
        self.value = value
