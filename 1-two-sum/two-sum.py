class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if(ans in map):
                return [map[ans], i]
            map[nums[i]]=i

        return [0, -1]        

             
            


        