from dataclasses import dataclass, field


@dataclass
class StackFrame:
    name: str
    staticLink: 'StackFrame | None'
    dynamicLink: 'StackFrame | None' = None
    vars: dict[str, int] = field(default_factory=dict)


class Scoper:
    def __init__(self):
        # Starts with the global scope
        self.call_stack: list[StackFrame] = [StackFrame("global", staticLink=None)] 

    def pushScope(self, stack_frame: StackFrame):
        stack_frame.dynamicLink = self.call_stack[-1]
        self.call_stack.append(stack_frame)

    def popScope(self):
        self.call_stack.pop()

    def getTopScope(self):
        return self.call_stack[-1]

    def getTopIdx(self):
        return len(self.call_stack) - 1

    def previousScope(self, currentScope):
        raise NotImplementedError

    def get(self, var):
        current_scope = self.call_stack[-1]
        while current_scope is not None:
            if var in current_scope.vars:
                return current_scope.vars[var]
            current_scope = self.previousScope(current_scope)
        return None

    def assign(self, var, val):
        current_scope = self.call_stack[-1]
        while current_scope is not None:
            if var in current_scope.vars:
                current_scope.vars[var] = val
                return
            current_scope = self.previousScope(current_scope)

    def declare(self, var, val):
        self.call_stack[-1].vars[var] = val


class DynamicScoping(Scoper):
    def previousScope(self, current_scope):
        return current_scope.dynamicLink


class StaticScoping(Scoper):
    def previousScope(self, current_scope):
        return current_scope.staticLink