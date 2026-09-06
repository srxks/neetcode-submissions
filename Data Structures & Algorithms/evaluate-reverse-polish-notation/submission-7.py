class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            elif i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                stack.append(-stack.pop() + stack.pop())
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operand1 / operand2))
        return stack[0]
