# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

#--------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------- Solution ------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

# 1- Create a set of the given list and compare the length of the set with the length of the list

class Solution(object):
    def containsDuplicate(self, nums):

        len1 = len(nums)
        len2 = len(set(nums))

        if len1 == len2:
            return False
        else:
            return True
        
# Time complexity : O(n)
# Space complexity : O(n)

# --------------------------------------------------------------------------------------------------------------------------------------

# 2- Create a Hashset and add the elements of the list to the set. If the element is already in the set return True

class Solution(object):
    def containsDuplicate(self, nums):
        hash_map = set()
        
        for num in nums:
            if num in hash_map:
                return True
            hash_map.add(num)
        return False

# Time complexity : O(n)
# Space complexity : O(n)

# --------------------------------------------------------------------------------------------------------------------------------------