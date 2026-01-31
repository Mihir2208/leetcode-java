class Solution(object):
    def groupAnagrams(self, strs):
        mp = defaultdict(list) # mapping char_count with list of anagrams
        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord("a")] += 1 #ascii value a=80, to put in 0th pos we do a-a = 80-80

            mp[tuple(count)].append(s)

        return mp.values()    





        