#https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #how well you do on this kind of question depends on how many input cases you have lined up!
        
        #parse through the string to remove white space. if
        #if the 1st character is not a +/- or a digit, then return 0.
        #parse the digit until you reach a nondigit character.
        #return
        i = 0
        sign = 1
        result = 0
        
        while(i < len(str) and str[i] == " "):
            i += 1
        if (i >= len(str)):
            return 0
        
        if (str[i] == "+"):
            sign = 1
            i += 1
        elif (str[i] == "-"):
            sign = -1
            i += 1
        elif (str[i].isdigit()):
            pass
        else: 
            return 0
        
        result = self.parseDigit(str, i, result)
        result = result*sign
        
        if (result < 2**(31)*-1):
            return 2**(31)*-1
        elif (result > 2**31 - 1):
            return 2**31 - 1
        return result
        
    def parseDigit(self, str, i, result):
        while (i < len(str) and str[i].isdigit()):
            result = result*10 + int(str[i])
            i += 1
        return result
              