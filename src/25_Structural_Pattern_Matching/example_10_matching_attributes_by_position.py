#!/usr/bin/env python

class Task:
    __match_args__ = ("op1", "operator", "op2")
    def __init__(self, operand1, operator, operand2):
        self.op1 = operand1
        self.operator = operator
        self.op2 = operand2

    def evaluate(self):
        match self:
            case Task(int(op1), op, int(op2)):
                match op:
                    case "+": return op1 + op2
                    case "-": return op1 - op2
                    case "*": return op1 * op2
                    case "/": return op1 // op2
                    case _: raise ValueError(f"Unknown operator: {op}")
            case Task(Task() as op1, op, op2):
                return Task(op1.evaluate(), op, op2).evaluate()
            case Task(op1, op, op2=Task() as op2):
                return Task(op1, op, op2.evaluate()).evaluate()
            case _:
                print("Invalid task:", self)

    def __str__(self):
        match (self.operator, self.op1, self.op2):
            case (op, Task() as op1, Task() as op2):
                return f"({op1}) {op} ({op2})"
            case (op, Task() as op1, int(op2)):
                return f"({op1}) {op} {op2}"
            case (op, int(op1), Task() as op2):
                return f"{op1} {op} ({op2})"
            case (op, op1, op2):
                return f"{op1} {op} {op2}"


if __name__ == "__main__":
    task = Task(Task(Task(23, "-", 3), "/", 5), "+", Task(2, "*", 3))
    print(f"{task} = {task.evaluate()}")
