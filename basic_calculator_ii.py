#https://leetcode.com/problems/basic-calculator-ii/

import operator
import math

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #NOTE THIS IS A VERY TRICKY QUESTION TO EXPLAIN TO INTERVIEWIERS. be very careful
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv} #nice touch
        
        valuesToAdd = list() #NOTE: WE ONLY PUSH ON TO THE STACK WHEN REACH THE 2nd symbol
        num = 0 #this is the most recent number
        sign = '+' #this is the PREVIOUS sign. we have a plus first because we always push the 1st value of expression onto stack

        
        for i,c in enumerate(s):
            if (c.isdigit()):
                num = 10*num + int(c)
                
            if ((not c.isdigit() and c != ' ') or i == (len(s) - 1)): #note that this if statement and the previous one can BOTH RUN. In fact, they both run during for the last character of the string.
                if (sign == '*'):
                    fn = opers[sign]
                    valuesToAdd.append(fn(valuesToAdd.pop(),num))
                elif (sign == '/'):
                    valuesToAdd.append(int(float(valuesToAdd.pop()) / num)) #weird python behavior for floor division of negative values
                elif (sign == '-'):
                    valuesToAdd.append(-num)
                elif (sign == '+'):
                    valuesToAdd.append(num)
                sign = c
                num = 0
        
        return sum(valuesToAdd)
    
        #1. pass through to define numbers & operators
        #2. pass through to do multiplication/division 
        #3. pass through to do addition/subtraction
        
        #OR (actual solution)
        
        #1 create a stack (list) to contain all numbers to be ADDED
        #2 switch
        #     * --> pop off stack & multiply --> push result onto stack
        #     / --> pop off stack & divide --> push result onto stack
        #     + --> push value onto stack
        #     - --> push value onto stack
        # stack is beautiful for this question because you only need the previous value to compute
        #open quesiton: WHY USE A PREFIX TREE vs. this solution for solving this question??
        #Suppose there are parentheses ---> then use recursion...?