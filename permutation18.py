Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

SOLUTION:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = [0] * 26
        for c in s1:
            mapp[ord(c) - 97] += 1
        i, j, count_chars = 0, 0, len(s1)
        while j < len(s2):
            if mapp[ord(s2[j]) - 97] > 0:   
                count_chars -= 1
            mapp[ord(s2[j]) - 97] -= 1
            j += 1
            if count_chars == 0:
                return True
            if j - i == len(s1):
                if mapp[ord(s2[i]) - 97] >= 0:
                    count_chars += 1
                mapp[ord(s2[i]) - 97] += 1
                i += 1
                
        return False
