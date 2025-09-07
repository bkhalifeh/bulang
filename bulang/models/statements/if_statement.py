from typing import Optional
from bulang.models.ast_node import ASTNode


class IfStatement(ASTNode):
    def __init__(
        self,
        condition: ASTNode,
        then_branch: ASTNode,
        else_branch: Optional[ASTNode] = None,
    ):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
