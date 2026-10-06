class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = cur = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                cur = cur * 10 + int(ch)

            elif ch in ["+","-"]:
                res += cur * sign
                cur = 0
                if ch == "-" : sign = -1
                else: sign = 1
                
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0 
                sign = 1    
            
            elif ch == ")":
                res += cur * sign
                res *= stack.pop()
                res += stack.pop()
                cur = 0

        return res + cur * sign        

        
