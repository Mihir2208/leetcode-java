class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0

        operator = '+'
        s += '+' # This is require to push the last element into the stack because on +,- it pushes into the stack.

        for ch in s:
            if ch == ' ':
                continue

            if ch.isdigit():
                num = num * 10 + int(ch)
                continue

            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop()*num)
            elif operator == '/':
                stack.append(int(stack.pop()/num))

            operator = ch #updating the current operator so next time it will choose the latest one
            num = 0 # reset to zero because to create new number by adding digits

        return sum(stack)




        