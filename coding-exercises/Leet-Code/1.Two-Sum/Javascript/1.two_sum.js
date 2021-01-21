var twoSum = function(nums, target) {
    let obj = {}
    let len = nums.length;
    for(let i = 0;i < len; i++) {
        let containKey = target - nums[i];
        if(obj[containKey]!=undefined) {
            return [obj[containKey],i]
        }
        obj[nums[i]] = i;
    }
};