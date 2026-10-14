# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

#--------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------- Solution ------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

"""
i cerate a binary search algorithm to find the index of the target value in the sorted array. If the target is not found, 
I will return the index where it would be inserted in order :D
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            
            if  target == nums[mid] :
                return mid
            
            if  target > nums[mid] :
                low = mid +1
            else :
                high = mid -1
        else:
            if target > nums[mid]:
                return mid +1 
            else :
                return mid
  

#--------------------------------------------------------------------------------------------------------------------------------------
