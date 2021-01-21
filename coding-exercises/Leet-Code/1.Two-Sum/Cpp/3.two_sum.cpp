#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int,int> nums_map;
        std::vector<int> result;
        for (int i = 0; i < nums.size(); i++){
            nums_map[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++){
            int value = target - nums[i];
            if (nums_map.find(value) != nums_map.end() && nums_map[value] != i) {
                result.push_back(i);
                result.push_back(nums_map[value]);
                return result;
            }
        }
    }
};