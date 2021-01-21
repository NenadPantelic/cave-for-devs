public class Solution 
{
    public int[] TwoSum(int[] nums, int target) 
    {
        int[] result = new int[2];
        Dictionary<int,int> id = new Dictionary<int,int>();
        
        for(int i =0; i< nums.Length; i++)
        {
            if(id.ContainsValue(target - nums[i]))
            {
                result[1] = i;
                foreach (var key in id.Keys)
                    {
                        if (id[key] == target - nums[i])
                            result[0] = key;
                    }
                
            }
            id[i] = nums[i];
        }
        return result;
    }
}