#https://leetcode.com/problems/permutations/description/
#generalized approach (subsets, combinations, permutations, combination-sum)
#todo: implement the iterative versions

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permRecursiveUtil(result, [], nums)
        return result
    
    def permRecursiveUtil(self, result, temp, nums):
        if (len(temp) == len(nums)):
            result.append(temp)
        elif (len(temp) > len(nums)):
            return
        
        for i in range(0, len(nums)):
            if (nums[i] in temp):
                continue
            self.permRecursiveUtil(result, temp + [nums[i]], nums)



#https://leetcode.com/problems/permutations-ii/description/

import copy 

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
        usedNums = [False] * len(nums)
        self.__permuteUniqueUtil(result, [], usedNums, nums)
        
        return result
    
    def __permuteUniqueUtil(self, result, temp, usedNums, nums):
        if (len(nums) == len(temp)):
            result.append(temp)
        elif (len(nums) < len(temp)):
            return
    
        for i in range(0, len(nums)):
            if (usedNums[i] or (i > 0 and nums[i] == nums[i - 1] and not usedNums[i-1]) ): #i dont quite understand the last argument
                continue
            usedNums[i] = True
            self.__permuteUniqueUtil(result, temp + [nums[i]], usedNums, nums)
            usedNums[i] = False            
        return