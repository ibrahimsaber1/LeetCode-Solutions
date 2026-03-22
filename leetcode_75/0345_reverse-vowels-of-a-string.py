# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


#--------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------- Solution ------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o','u']
        left = len(s) -1
        right = 0

        while right < left and right < len(s)-1:
            # print(f"left >> {left}")
            # print(f"right >> {right}")
            if s[right].lower() in vowels and s[left].lower() in vowels:
                left_value = s[right]
                s[right] = s[left]
                s[left] = left_value
                # print(f"00 update s ==> {s}")
                right +=1
                left -=1
                
            elif s[right].lower() in vowels and s[left].lower() not in vowels:
                # print(f"01 update s ==> {s}")
                
                left -=1
            elif s[right].lower() not in vowels and s[left].lower() in vowels:
                # print(f"02 update s ==> {s}")
                
                right +=1
            else:
                right +=1
                left -=1
                
        return "".join(s)

#--------------------------------------------------------------------------------------------------------------------------------------
