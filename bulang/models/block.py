from typing import List
from bulang.models.ast_node import ASTNode


class Block(ASTNode):
    def __init__(self, statements: List[ASTNode]):
        self.statements = statements
