#https://leetcode.com/problems/minimum-time-difference/description/

class Solution:
    
    def findMinDifference(self, A):
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        minutes = map(convert, A)
        minutes.sort()

        return min( (y - x) % (24 * 60) 
                    for x, y in zip(minutes, minutes[1:] + minutes[:1]) )
    def lfindMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        #two subproblems
        #1. convert to minutes -> linear
        #2. find the shortest distance between any (circular) -> sort & then compare the excess--> nlogn +n + O(1)
        
        #alternative LINEAR time solution is to create a boolean array of size 1440. then you don't have to sort!
        #https://leetcode.com/problems/minimum-time-difference/discuss/100640/Verbose-Java-Solution-Bucket
        minutesArray = self.convertToMinutes(timePoints) #good abstraction in an interview
        minutesArray.sort()
        
        minDiff = minutesArray[1] - minutesArray[0]
        
        for curr in range(len(minutesArray) - 1):
            nxt = curr + 1
            diff = minutesArray[nxt] - minutesArray[curr]
            if (diff < minDiff):
                minDiff = diff
        
        diffToMidnight = 1440 - minutesArray[-1]
        diff = minutesArray[0] + diffToMidnight
        if (minDiff > diff):
            minDiff = diff 
        return minDiff
            
    def convertToMinutes(self, timePoints):
        minutes = list()
        for i in timePoints:
            s = i.split(':')
            m = int(s[0]) * 60 + int(s[1])
            minutes.append(m)
        return minutes