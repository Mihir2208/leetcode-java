class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(find_first):
            l = 0
            h = len(nums) - 1
            candidate = -1

            while l <= h:
                mid = (l + h) // 2

                if nums[mid] == target:
                    candidate = mid

                    if find_first:
                        h = mid - 1       # keep searching left
                    else:
                        l = mid + 1       # keep searching right

                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1

            return candidate

        first = find_bound(True)
        last = find_bound(False)

        return [first, last]           
        