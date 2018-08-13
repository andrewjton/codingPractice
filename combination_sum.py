#https://leetcode.com/problems/combination-sum/description/
#aka isSubsetSum
import copy

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #use backtracking & recursion
        #choose a number from the array & subtract if from target. then call combination sum. base case is if target < 0.
        
        #edge cases: target is less than 0
        if (target < 0 ):
            return []

        combinations = list()
        for c in candidates:
            combinations = combinations + (self.cSum(candidates,(target-c),[c]))
        return combinations
    
    def cSum(self, candidates, target, subset):
        if (target < 0 ):
            return []
        elif (target == 0):
            return list([subset])
        combinations = list()
        for c in candidates:
            cSumSubset = copy.deepcopy(subset)
            
            cSumSubset.append(c)
            combinations = combinations + (self.cSum(candidates,(target-c),cSumSubset))
        return combinations