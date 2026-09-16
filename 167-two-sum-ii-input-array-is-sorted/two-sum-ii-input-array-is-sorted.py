class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans = []
        left = 0
        right = len(numbers) - 1

        while left<=right:
            total = numbers[left]+numbers[right]
            # print(total)

            if total == target:
                ans.append(left+1)
                ans.append(right+1)
                break

            if total > target:
                right -= 1
            else:
                left += 1

        return ans            



        