Number Complement
Solution
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

Solution:

class Solution(object):
    def findComplement(self, num):
        b = bin(num)[2:] # bin is the inbuilt function to convert a decimal number to binary. 
        opt = 0     # [2:] is used because it when we convert from decimal to binary it contains (0b) also in the beginning, so as to eliminate it we start from 2nd position.
        for i, c in enumerate(reversed(b)): # Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
            if c=='0': opt+=pow(2,i)         # i is used for the index and c is uded for the element at at that index. 
        return opt 
