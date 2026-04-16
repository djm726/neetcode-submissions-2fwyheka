class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                operands.append(operands.pop() + operands.pop())
            elif tokens[i] == "-":
                result1, result2 = operands.pop(), operands.pop()
                operands.append(result2 - result1)
            elif tokens[i] == "*":
                operands.append(int(operands.pop()) * int(operands.pop()))
            elif tokens[i] == "/":
                result1, result2 = operands.pop(), operands.pop()
                operands.append(int(float(result2) / result1))
            else:
                operands.append(int(tokens[i]))

        return int(operands[0])