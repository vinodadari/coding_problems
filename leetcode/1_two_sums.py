"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Testcase:

[2,7,11,15] 9
[3,2,4] 6
[3,3] 6
[3,2,3] 6

"""
from typing import List

# memory - 17.6MB
# runtime - 2779ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if -10**9 <= target and target <= 10**9:

            initial_index = 0
            while 2 <= len(nums)and len(nums) <= 10**4:
                for index in range(initial_index + 1, len(nums)):

                    total = nums[initial_index] + nums[index]
                    if target == total:
                        return [initial_index, index]

                initial_index += 1
        return []


# low memory - 15MB
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pred = {} # predicate -> i
        for i, n in enumerate(nums):
            p = target - n
            print(pred)
            if p in pred:
                return [i, pred[p]]
            pred[n] = i

        return []


# runtime - 56ms
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = []
            nums_dict[nums[i]].append(i)

        nums_upd = sorted(list(set(nums)))

        for i in range(len(nums_upd)):
            el = nums_upd[i]

            if el == target // 2 and len(nums_dict[el]) > 1:
                print("returned")
                return [nums_dict[el][0], nums_dict[el][1]]

            l, r = i + 1, len(nums_upd)
            while r - l > 1:
                m = (l + r) // 2
                if nums_upd[m] > target - el:
                    r = m
                else:
                    l = m

            if nums_upd[l] == target - nums_upd[i]:
                ind1 = nums_dict[el][0]
                ind2 = nums_dict[nums_upd[l]][0]
                return [ind1, ind2]
        return []

# runtime - 122ms
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the naive approach would be to do a loop and inner loop and check their sum
        # that would be n * (n - 1) / 2 complexity
        # if we sort the list first, the inner loop can stop as soon as the sum is above target
        if target > 0:
            num_indices = [(nums[i], i) for i in range(0, len(nums))]
        else:
            num_indices = [(-nums[i], i) for i in range(0, len(nums))]
            target = -target
        num_indices.sort()
        for i in range(0, len(num_indices)):
            num1 = num_indices[i][0]
            if num1 > target:
                break
            left = i + 1
            right = len(num_indices) - 1
            while left <= right:
                mid = (left + right) // 2
                s = num1 + num_indices[mid][0]
                if s == target:
                    return [num_indices[i][1], num_indices[mid][1]]
                elif s > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return []

if __name__ == "__main__":
    nums = [4,5,6,1,2,3,4,5]
    target = 9

    output = Solution().twoSum(nums,target)
    print(output)
    output = Solution1().twoSum(nums,target)
    print(output)
    output = Solution2().twoSum(nums,target)
    print(output)
    output = Solution3().twoSum(nums,target)
    print(output)
