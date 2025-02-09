# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

#--------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------- Solution ------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
# Kadane's Algorithm AT : https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

def maxSubarraySum(arr):
    
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)
    
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr))

# --------------------------------------------------------------------------------
# using the kadane's algorithm in leetcode

class Solution(object):
    def maxSubArray(self, arr):
        res = arr[0]
        maxEnding = arr[0]
        for i in range(1, len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            res = max(res, maxEnding)
        return res

# --------------------------------------------------------------------------------

class Solution(object):
    def maxSubArray(self, nums):
        
        max_nums = current_sum = nums[0]
        for i in nums[1:]:
            current_sum = max(i, current_sum + i)
            max_nums = max(max_nums ,current_sum )
        return max_nums

# --------------------------------------------------------------------------------------------------------------------------------------