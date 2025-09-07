from typing import Optional
from bulang.models.ast_node import ASTNode


class VarDeclaration(ASTNode):
    def __init__(self, var_type: str, name: str, value: Optional[ASTNode] = None):
        self.var_type = var_type
        self.name = name
        self.value = value
