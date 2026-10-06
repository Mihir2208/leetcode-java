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


# class Solution:
    def calculate(self, s: str) -> int:
        # Idea: the expression is just a sum of signed numbers.
        # "10 - 2 + 3" = (+10) + (-2) + (+3)
        # Brackets are handled by saving the outer state on a stack,
        # computing the inside separately, then merging it back.

        stack = []   # holds saved (res, sign) pairs, one pair per open bracket
        res = 0      # running total of the current level (inside the current bracket)
        cur = 0      # the number currently being built from digits
        sign = 1     # sign to apply to cur: +1 or -1

        for ch in s:
            if ch.isdigit():
                # Build multi-digit numbers: "234" -> 2 -> 23 -> 234
                cur = cur * 10 + int(ch)

            elif ch in ["+", "-"]:
                # The number before this operator is finished: add it with its sign
                res += cur * sign
                cur = 0
                # This operator decides the sign of the NEXT number
                if ch == "-": sign = -1
                else: sign = 1

            elif ch == "(":
                # Entering a bracket: save the outer total and the sign in front of the bracket
                # e.g. "10 - (": saves res=10, sign=-1
                stack.append(res)
                stack.append(sign)
                # Start a fresh calculation for the inside of the bracket
                res = 0
                sign = 1

            elif ch == ")":
                # Finish the last number inside the bracket
                res += cur * sign
                cur = 0
                # Now res = value of the whole bracket
                # Apply the sign that was in front of the bracket (pushed last, so popped first)
                res *= stack.pop()
                # Add back the outer total saved before the bracket
                res += stack.pop()

            # Spaces match no branch, so they're skipped automatically

        # The last number never meets an operator after it, so add it here
        return res + cur * sign        
