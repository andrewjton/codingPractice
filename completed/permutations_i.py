#https://leetcode.com/problems/permutations/description/
#generalized approach (subsets, combinations, permutations, combination-sum)

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