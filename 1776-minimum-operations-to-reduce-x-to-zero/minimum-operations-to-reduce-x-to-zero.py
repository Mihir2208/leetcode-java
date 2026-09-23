class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = 0
        if x == total:
            return len(nums)
        if x > total:
            return -1
        else:
            target = total - x #6 = 11 - 5

        left = 0
        current_sum = 0
        max_length = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                window_length = right-left+1
                max_length = max(max_length, window_length)

        if max_length == 0:
            return -1        

        return len(nums) - max_length        


        