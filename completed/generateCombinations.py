class Solution:
    #iterative solution: 
    #0. initialize result = [[]], a list of lists
    #1. iterate over nums
    #     a. for each item in result, add the current num to the front
    #  2^n runtime
    def subsetsI(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res += [l2 + [i] for l2 in res]
                
        return res
    
    #recursive solution
    #backtracking & DFS
    #result = list of lists
    #temp = list that keeps track of 
    #num = original list
    #startP = imagine it as the start index. it get's incremented TWICE*hardest one to explain*
    def subsets(self, nums):
        #nums.sort()
        result = []
        temp = []
        self.subsetRecursiveUtil(result, temp, nums, 0)
        return result
    
    def subsetRecursiveUtil(self, result, temp, nums, startP):
        result.append(temp)
        i = startP
        while(i < len(nums)):
            self.subsetRecursiveUtil(result, temp + [nums[i]], nums, i+1)
            i += 1
        #note: you don't have to return anything because in python, list variable is a pointer which is passed down by method. ("pass by object reference")
            