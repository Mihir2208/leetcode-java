class Solution(object):
    def groupAnagrams(self, strs):
        mp = {}
        for i in range (len(strs)):
            sorted_character = sorted(strs[i])
            join_str = "".join(sorted_character)
            if join_str not in mp:
                mp[join_str] = []
            mp[join_str].append(strs[i])     
        return list(mp.values())  







        