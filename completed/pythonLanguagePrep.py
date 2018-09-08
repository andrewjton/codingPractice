#Python Preparation

#BIT MANIPULATION -----------------------------------------------------------
# -integers have arbitrary precision (infinite range) in python 3 --> no overflow issues, unless your machine runs out of memory
# -sys.maxsize refers to the word size on a system but you can exceed that
# - -16 >> 2 = -4. no such thing as unsigned shift in python
# -shift and bitwise operations are constant time

import sys
print(sys.maxsize) # 2**63 - 1 on a 64 bit system

#1. count the number of bits
def countBits(num)
	numBits = 0
	while num:
		numBits += 1
		num >>= 1
countBits(3)


#2. zero out the Least significant 1
#this is useful if you're trying to count the number of 1's in a solution. constant time operation!
def zeroOutLSB(num):
	num = num&(num-1)
	return num

#3. ....



#TRAVERSING FOR LOOPS -----------------------------------------------------------
zip(listA, listB) #combine two lists
reversed(listA)
enumerate(listB) #iterator i, item v
map(lambda x: x**2, range(0,4)) #iterator over [0, 1, 4, 9]

d = {} #dictionaries
for key, value in d.items(): 
	pass


#'SEQUENCE' Data Types (list, range, tuple) -------------------------------------
#https://docs.python.org/3/tutorial/datastructures.html 
#1. Lists
l = [1,2,3,4,10,11]
l.remove(10)
l.append(10)
del l[5]
l.reverse()

#2. Ranges
range(0, 1e1000) #takes a constant amount of space!! it's an iterator.
range(0, 100, 2)#0, 2, 4, 6, ..., 100


#3. Tuple. immutable, but the objects within it can be mutable
#*only sequence data type that can be used as a hash for a dict*
tup = ('hey', 7, 'supp')

#4. splicing
s = 'andrewton'
s[::2] #'adetn'     every other
s[::-1] #notwerdna  backwards
s[0:3] #and 

#5. creating a string from a list. more efficient to deal with appending to a list than a string
s = ['h', 'el', 'lo']
s += 'moreefficienttoappendtolisthanastring'
''.join(s)

#6. sorting
l = [1, 2, 0 , 1.5]
l2 = sorted(l)
l.sort() # inplace

#7. List comprehensions 
#concise way of generating lists
l = [(i, j) for i in range(0,4) for j in range(0,4) if i == j]
#output:[(0, 0), (1, 1), (2, 2), (3, 3)]

# Inefficient way:
# l = []
# for i in range(0,4):
# 	for j in range(0,4):
# 		if i == j:
# 			l.append((i,j))

#filter
f = filter(lambda x: x %2 == 0, range(0,10))
print(list(f))# [0, 2, 4, 6, 8]


#8. deep copy vs shallow copy
#...

# QUEUES, HEAPS, DICTIONARIES, SETS  -------------------------------------
#1. Queue
from lists import deque
q = deque([0,1,2,3])
q.popleft() #constant time operation
q.append(4)

#2. Heap
#the first element in tuple is the key
import heapq
h = []
heapq.heappush(h, (10, 'blah'))
heapq.heappush(h, (9, 'filler text'))
heapq.heappush(h, (6, 'aaaaa'))
heapq.heappush(h, (8, 'there must be an equivalent number of elements in each tuple'))
minimum = heapq.heappop(h)


heapq.heapify([10, 12, 3, 4])

#3. dictionaries and sets
s = set()
s = {'hi', 'this', 'is', 'set'}
s.add(1)
if 'this' in s:
	print('present')

d = {} #empty dictionary
d[1] = 2
d[2] = 4
del d[1]


#NUMBER STUFF (Precision) ------------------------------------------------------------------
abs(-3)
abs(-3.0)
max(3,1)
4**1/2 #square root

import math
math.ceil(5.1)
math.ceil(-5.1)
math.floor(5.1)
math.floor(-5.1)

float('inf') #floats don't have infinite precision unfortunately.
float('-inf')

#floats also have problems with precision. because of the limitations of binary
#https://docs.python.org/3/tutorial/floatingpoint.html
format (1/10, '.20g') # '0.10000000000000000555' should be .1
.2 + .4 == .6 #FALSE
math.isclose(.2 + .4, .6) #TRUE

from fractions import Fraction 
from decimals import Decimal 
num1 = Fraction(1,2)
num2 = Fraction(2,3)
num1+num2
num1*num2
num1/num2
num1-num2
num1 = Decimal(3.2)
num2 = Decimal(3.2)
num1+num2

#casting to ascii
ord('a') # 97
chr(97) #a

#NUMBER STUFF (Random) ------------------------------------------------------------------
# 1. functools.reduce
#reduces it down to a single value
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3]) #6
reduce(lambda x, y: max(x, y), [1,2,3]) #3

# 2. groupby
#...
# 3. accumulate()
#...

# 4. product()
#...

# 5. combinations()
#...





#LAMBDA FUNCTIONS -----------------------------------------------------------------------
#1. sorting
#2. passing a function into a variable (anonymous functions)

pairs = [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
sorted(pairs, key = lambda i: i[0])
#output: [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

m = map(lambda x: x**2, [0, 1, 2, 3, 4])
print(list(map)) # [0, 1, 4, 9, 16]

#BUILTIN TYPES -----------------------------------------------------------------------
#https://docs.python.org/3/library/functions.html
all()
any()
hash()


#COLLECTIONS  -----------------------------------------------------------------------
#named tuples are useful for storing readable objects
#more readable than a dict, list or tuple WHILE less verbose than a class
from collections import namedtuples
Point = namedtuple('Point', ['x', 'y'] ) 
p1 = Point(1,2)
p1.x
p1.y
print(p1) # output: Point(x=1, y=2)

