from bulang.models.ast_node import ASTNode


class PrintStatement(ASTNode):
    def __init__(self, expression: ASTNode):
        self.expression = expression
