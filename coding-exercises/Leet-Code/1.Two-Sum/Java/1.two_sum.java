class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int compliment = target - current;
            
            if (map.containsKey(compliment) && map.get(compliment) != i) {
                return new int[] {map.get(compliment), i};
            }
            
            map.put(current, i);
        }
        throw new IllegalArgumentException("No numbers add to the target value");
    }
}
