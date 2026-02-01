class Solution(object):
    def isPalindrome(self, s):
        c = ""
        for char in s:
            if char.isalnum():
                c = c+char.lower()

        i=0
        j= len(c) - 1
        while i<j:
            if c[i] != c[j]:
                return False
            i+=1
            j-=1    

        return True
        