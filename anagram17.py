Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

SOLUTION:

import operator
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=[]
        if(len(s)<len(p)):return l
        lk=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ll = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        #making dictionaries with a-z as key and value as 0
        d1=dict(zip(ll,lk))
        d2=dict(zip(ll,lk))
        #hashing p to d1
        for e in p:
            d1[e]+=1
        #print(d1)
        #hashing starting elements of s to d2
        for e in s[:len(p)]:
            d2[e]+=1  
        #print(d2)
        #checking if both dictionaries are equal
        if(operator.eq(d1,d2)==True):l+=[0]
        #traversing the string s and at each point removing initial element and adding the new element to keep           length as len(p)
        for i in range(1,len(s)-len(p)+1):
            d2[s[i-1]]-=1
            d2[s[i+len(p)-1]]+=1
            #print(d2)
            #checking if both dictionaries match
            if(operator.eq(d1,d2)==True):l+=[i]
        return l
