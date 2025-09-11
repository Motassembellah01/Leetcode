from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                rightOperand = stack.pop()
                leftOperand = stack.pop()
                if token == "+":
                    stack.append(leftOperand + rightOperand)
                elif token == "-":
                    stack.append(leftOperand - rightOperand)
                elif token == "*":
                    stack.append(leftOperand * rightOperand)
                else:
                    stack.append(int(leftOperand / rightOperand))
            else:
                stack.append(int(token))
        return stack[-1]