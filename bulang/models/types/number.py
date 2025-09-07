from bulang.models.ast_node import ASTNode


class Number(ASTNode):
    def __init__(self, value: float):
        self.value = value
