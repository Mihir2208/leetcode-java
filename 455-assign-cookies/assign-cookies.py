class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        len_g = len(g)
        len_s = len(s)
        g.sort()
        s.sort()

        left = 0 # This pointer is for cookies
        right = 0 # This pointer is for children

        while left < len_s and right < len_g:
            if g[right] <= s[left]:
                right += 1
            left+=1

        return right        
        