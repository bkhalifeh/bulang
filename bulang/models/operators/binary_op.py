from bulang.models.ast_node import ASTNode
from bulang.models.token import Token


class BinaryOp(ASTNode):
    def __init__(self, left: ASTNode, operator: Token, right: ASTNode):
        self.left = left
        self.operator = operator
        self.right = right
