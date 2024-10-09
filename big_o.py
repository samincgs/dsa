'''
 - Big O is a way to define how something grows in relation to one or more controlling variables (Big O is a measurement of growth)
 - In Computer Science it is primarily used as a way to define time complexity
 - Big O is also used for space complexity which instead of measuring performance or the number of operations, it measures the amount of memory it takes
 - Big o will be used to show how well an algorithm scales when ur dealing with different parameters
 - Big O is usually represented in terms of n
 - Big O is used to describe worst cases
 - Big Omega (Ω) to describe best cases
 - Big Theta (Θ) to describe average cases
 '''

''' The most common runtimes in big O notation ()
    O(1) -> constant time
    O(log(n)) -> binary search
    O(n) -> linear runtime
    O(nlog(n)) -> sorting algorithms (for go through whole data O(n)) then (sort the data O(log(n)))
    O(n^2), O(n^3) -> worst case for sorting algorithms
    O(2^n), O(3^n) 
    O(n!)
    O(n^n)
'''

n = 5  
k = 2

print('abc') # constant runtime O(1) since there is no controlling variable (no n or k)


print('abc') # still O(1) even if its multiple because there is no variable controlling its runtime/growth
print('abc')

# Note: Even if there is a controlling variable, an algorithm can be O(1) if the variable has no impact of the runtime
for i in range(1000):  # 'i' is a controlling variable, but it is never used
    print("Hello, World!") # this would be O(1000) -> O(1) because we are executing it a fixed size so it does not scale in growth

# This algorithm has a big O of O(n)
for i in range(n): # controlling variable is n (grows linearly according to the value of n)
    print('abc')
    
# (FOR EXAMPLE) 
# In big o you drop all the coefficients so if its O(3n) we cut out the 3 
for i in range(n): # the big o for this is still O(n)
    print('abc')
    print('abc')
    print('abc')

# This algorithm has a big O of O(n ^ 2)
for i in range(n): # this algorithm will print abc n * n times
    for j in range(n):
        print('abc')

for i in range(n * n): # This also has a big O notation of O(n ^2) 
    print('abc')        
    
# you would assumec the big O would be O(n ^ 2 + n) but we drop all the lower terms
# The actual big O notation for this statement is O(n ^ 2)
for i in range(n): 
    for j in range(n):
        print('abc')
    print('abc')

for i in range(n): # the first loop would run n * n O(n ^ 2)
    for j in range(n):
        print('abc')
for i in range(k): # the second loop would run k times (that means there are two different control variables) O(k)
    print('abc')
# In Big O notation, the terms are additive, and both 𝑛2 and k contribute to the final complexity since they are independent control variables
# the big o for this would be O(n ^ 2 + k)
