class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> mp = new HashMap<>();
        // This is counting prefix sum and frequency of that prefix count
        mp.put(0,1);
        int prefixsum = 0;
        int cnt = 0;

        for(int i=0; i<nums.length; i++){
            prefixsum += nums[i];
            int remove = prefixsum-k;
            if(mp.containsKey(remove)) cnt += mp.get(remove);
            mp.put(prefixsum, mp.getOrDefault(prefixsum, 0)+1);

        }

        return cnt;
    }
}