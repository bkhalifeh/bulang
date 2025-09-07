from bulang.models.ast_node import ASTNode


class Boolean(ASTNode):
    def __init__(self, value: bool):
        self.value = value
