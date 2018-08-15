#https://leetcode.com/submissions/detail/169308731/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        #two alternate solutions
        
        #1. K*N time. K space. k is max val
        #create an array from 1-K. for each of N pairs, fill in their values
        
        #2. NLOGN
        #sort by first value in each pair. iterate over list. check if the first neightbor's end value is greater than the 2nd neighbor's first value. if so merge.
        
        res = []
        for i in sorted(intervals, key = lambda i: i.start): #creates a new list sorted by the start value of each interval
            if (res and (res[-1].end >= i.start)):
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res

#edge case
def mergeIntervalsPalantirInterview(l):
    #1. sort
    l.sort(key = lambda: i[0]) #python will be nlogn
    
    prev = [-1,-1] #
    result = []
    isFirstGo = True
    #2 iterate through sorted list
    for i in l:
        if isFirstGo:
            isFirstGo = False
            prev = l[0]
            continue
        if (prev[1] >= i[0]): #overlap
            prev[1] = max(i[1], prev[1])
        else: #no overlap
            result.append(prev)
            prev = i
    result.append(prev)
        
    return result
    
#[-1,-1]
#[1,5]
#[6,11]

result [[1,5], [6,11]]
        
