from bulang.models.ast_node import ASTNode
from bulang.models.token import Token


class UnaryOp(ASTNode):
    def __init__(self, operator: Token, operand: ASTNode):
        self.operator = operator
        self.operand = operand
