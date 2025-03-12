#Brute Force -> Each number will be compare to other num and if a number is equal, return True 
# O(n) for each number -> Time Complexity : O(n^2)
# No need extra space -> O(1)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num_i in range(len(nums)):
            for num_j in range(len(nums)):
                if num_i != num_j and nums[num_i] == nums[num_j]:
                    return True
        return False



#Sort : sort the array force and check the neighboor 
#O(n) to pass on the array and sort O(logn)
#Time complexity : O(nlogn)
#Space complexity : O(1)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(1,len(nums)):
            if nums[index] == nums[index-1]:
                return True
        return False
    
#Use set : store in a set each number
#Time : O(n)
#Space(O(n))
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set()
        for num in nums:
            if num in set_num:
                return True
            set_num.add(num)
        return False