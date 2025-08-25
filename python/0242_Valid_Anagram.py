# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        frecs = {}
        for ch in s:
            frecs[ch] = frecs.get(ch , 0) +1

        frecs = sorted(frecs.items())

        frect = {}
        for ch in t:
            frect[ch] = frect.get(ch , 0) +1

        frect = sorted(frect.items())

        return frecs == frect


# Optimized Approach
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        frecs = {}
        for ch in s:
            frecs[ch] = frecs.get(ch , 0) +1

        for ch in t:
            if ch in frecs:
                frecs[ch] -= 1
                if frecs[ch] < 0:
                    return False
            else:
                return False

        return True