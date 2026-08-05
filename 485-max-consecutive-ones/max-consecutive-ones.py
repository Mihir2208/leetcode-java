class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_value = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                max_value = max(counter, max_value)
                counter = 0

        return max(counter, max_value)       
