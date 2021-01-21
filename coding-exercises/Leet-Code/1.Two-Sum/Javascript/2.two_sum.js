var twoSum = function(nums, target) {
    const length = nums.length;
    const cacheNumbToIndex = {};
    let index;
    
    for (index = 0; index < length; index++) {
        const gotNum = nums[index];
        const wantedNum = target - gotNum;
        
        if (cacheNumbToIndex[wantedNum] !== undefined) {
            return [index, cacheNumbToIndex[wantedNum]].sort();
        }
        
        cacheNumbToIndex[gotNum] = index;
    }
};