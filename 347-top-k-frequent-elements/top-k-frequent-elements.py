class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        for n in nums:
            dict[n] = dict.get(n, 0)+1 
        # print(dict)

        max_heap = []
        for num, freq in dict.items():
            heapq.heappush(max_heap,(-freq, num))

        # print(max_heap)    

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(max_heap)
            result.append(num)

        return result    
        