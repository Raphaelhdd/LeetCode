#Brute Force: Start from beginning and check with the rest of the list and so on
#T : O(n^2)
#S: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return []

#Best solution:
#T : O(n)
#S: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen_num:
                return [seen_num[diff], i]
            seen_num[n] = i