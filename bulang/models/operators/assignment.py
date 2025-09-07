from bulang.models.ast_node import ASTNode


class Assignment(ASTNode):
    def __init__(self, name: str, value: ASTNode):
        self.name = name
        self.value = value
