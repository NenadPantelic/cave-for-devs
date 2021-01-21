class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                      
        mapping = {n: i for i, n in enumerate(nums)}
        
        for i, num in enumerate(nums):
            diff = mapping.get(target - num, False)
            
            if diff and diff != i:
                return [i, diff]