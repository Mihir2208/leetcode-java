class Solution(object):
    def firstUniqChar(self, s):
        mp = {}
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0)+1
        for i, char in enumerate(s):
            if mp[char] == 1:
                return i
            
        return -1    

        

        