from typing import Any, Dict, Optional


class Environment:
    def __init__(self, parent: Optional["Environment"] = None):
        self.variables: Dict[str, Any] = {}
        self.parent = parent

    def define(self, name: str, value: Any):
        self.variables[name] = value

    def get(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        raise Exception(f"Undefined variable: {name}")

    def assign(self, name: str, value: Any):
        if name in self.variables:
            self.variables[name] = value
            return
        if self.parent:
            self.parent.assign(name, value)
            return
        raise Exception(f"Undefined variable: {name}")
