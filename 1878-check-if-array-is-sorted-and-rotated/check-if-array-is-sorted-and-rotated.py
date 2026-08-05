class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)

        count = 0

        for i in range(1, N):
            if nums[i-1] > nums[i]:
                count += 1

        if nums[N-1] > nums[0]:
            count += 1

        return count <= 1                

