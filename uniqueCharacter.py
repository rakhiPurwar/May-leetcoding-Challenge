  First Unique Character in a String
Solution
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=collections.Counter(s) #counter is a dictionary sub class, which is used to store elements as
        #as keys and there count as values
        for element,index in enumerate(s):
            if count[index]==1:
                return element
        return -1
                
