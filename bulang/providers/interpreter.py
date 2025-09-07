from typing import Any
from bulang.enums.token_type_enum import TokenType
from bulang.models.ast_node import ASTNode
from bulang.models.block import Block
from bulang.models.operators.assignment import Assignment
from bulang.models.operators.binary_op import BinaryOp
from bulang.models.operators.identifier import Identifier
from bulang.models.operators.unray_op import UnaryOp
from bulang.models.program import Program
from bulang.models.statements.if_statement import IfStatement
from bulang.models.statements.print_statement import PrintStatement
from bulang.models.statements.while_statement import WhileStatement
from bulang.models.types.boolean import Boolean
from bulang.models.types.number import Number
from bulang.models.types.string import String
from bulang.models.var_declaration import VarDeclaration
from bulang.providers.environment import Environment


class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.environment = self.global_env

    def interpret(self, node: ASTNode) -> Any:
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: ASTNode):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    def visit_Program(self, node: Program) -> Any:
        result = None
        for statement in node.statements:
            result = self.interpret(statement)
        return result

    def visit_VarDeclaration(self, node: VarDeclaration) -> Any:
        value = None
        if node.value:
            value = self.interpret(node.value)
        else:
            if node.var_type == "int":
                value = 0
            elif node.var_type == "string":
                value = ""
            elif node.var_type == "boolean":
                value = False

        self.environment.define(node.name, value)
        return value

    def visit_Assignment(self, node: Assignment) -> Any:
        value = self.interpret(node.value)
        self.environment.assign(node.name, value)
        return value

    def visit_BinaryOp(self, node: BinaryOp) -> Any:
        left = self.interpret(node.left)
        right = self.interpret(node.right)

        if node.operator.type == TokenType.PLUS:
            return left + right
        elif node.operator.type == TokenType.MINUS:
            return left - right
        elif node.operator.type == TokenType.MULTIPLY:
            return left * right
        elif node.operator.type == TokenType.DIVIDE:
            if right == 0:
                raise Exception("Division by zero")
            return left / right
        elif node.operator.type == TokenType.EQUAL:
            return left == right
        elif node.operator.type == TokenType.NOT_EQUAL:
            return left != right
        elif node.operator.type == TokenType.LESS_THAN:
            return left < right
        elif node.operator.type == TokenType.GREATER_THAN:
            return left > right
        elif node.operator.type == TokenType.LESS_EQUAL:
            return left <= right
        elif node.operator.type == TokenType.GREATER_EQUAL:
            return left >= right

        raise Exception(f"Unknown binary operator: {node.operator.type}")

    def visit_UnaryOp(self, node: UnaryOp) -> Any:
        operand = self.interpret(node.operand)

        if node.operator.type == TokenType.MINUS:
            return -operand
        elif node.operator.type == TokenType.PLUS:
            return +operand

        raise Exception(f"Unknown unary operator: {node.operator.type}")

    def visit_Number(self, node: Number) -> float:
        return node.value

    def visit_String(self, node: String) -> str:
        return node.value

    def visit_Boolean(self, node: Boolean) -> bool:
        return node.value

    def visit_Identifier(self, node: Identifier) -> Any:
        return self.environment.get(node.name)

    def visit_IfStatement(self, node: IfStatement) -> Any:
        condition = self.interpret(node.condition)

        if self.is_truthy(condition):
            return self.interpret(node.then_branch)
        elif node.else_branch:
            return self.interpret(node.else_branch)

        return None

    def visit_WhileStatement(self, node: WhileStatement) -> Any:
        result = None
        while self.is_truthy(self.interpret(node.condition)):
            result = self.interpret(node.body)
        return result

    def visit_Block(self, node: Block) -> Any:
        previous = self.environment
        self.environment = Environment(previous)

        try:
            result = None
            for statement in node.statements:
                result = self.interpret(statement)
            return result
        finally:
            self.environment = previous

    def visit_PrintStatement(self, node: PrintStatement) -> Any:
        value = self.interpret(node.expression)
        print(value)
        return value

    def is_truthy(self, value: Any) -> bool:
        if value is None or value is False:
            return False
        if value == 0 or value == "":
            return False
        return True
