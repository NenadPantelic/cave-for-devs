## 1. Two Sum

Given an array of integers _nums_ and an integer _target_, return _indices_ of the two numbers such that they add up to target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Example 1 :

```python
Input: nums = [2,7,11,15],
target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9,
we return [0, 1].
```

### Example 2 :

```python
Input: nums = [3,2,4],
target = 6
Output: [1,2]
```

### Constraints:

- 2 <= nums.length <= 103
- -109 <= nums[i] <= 109
- -109 <= target <= 109

Only one valid answer exists.
