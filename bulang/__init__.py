from bulang.providers.interpreter import Interpreter
from bulang.providers.lexer import Lexer
from bulang.providers.parser import Parser


def run_bulang(code: str):
    try:
        lexer = Lexer(code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter()
        result = interpreter.interpret(ast)

        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
