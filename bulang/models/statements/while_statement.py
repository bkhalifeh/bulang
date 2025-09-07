from bulang.models.ast_node import ASTNode


class WhileStatement(ASTNode):
    def __init__(self, condition: ASTNode, body: ASTNode):
        self.condition = condition
        self.body = body
