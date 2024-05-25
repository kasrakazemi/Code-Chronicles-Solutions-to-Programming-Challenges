import math
class Solution(object):
    def minOperations(self, nums, numsDivide):
     nums.sort()
 
     gcd = math.gcd(*numsDivide)

     for index, element in enumerate(nums):
   
        if gcd % element ==0:
           return index
     else: 
           return -1  
        