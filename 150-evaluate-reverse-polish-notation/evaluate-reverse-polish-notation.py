class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:  
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                add = num1+num2
                stack.append(add)

            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                sub = num2 - num1
                stack.append(sub)

            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                product = num1*num2
                stack.append(product)

            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                divide = int(num2/num1)
                stack.append(divide)

            else:
                stack.append(int(token))                

        return stack.pop()        



