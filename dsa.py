# Data Structures & Algorithms
# why is algorithms always associated? it is because algorithms process the data, that data is stored in a data structure

# Algorithms: Just a process of doing something (typically uses a function to carry out a particular solution)
# Data: Is the structured data being passed into the function

# simplest example of an algorithm
print('hello') # print is the algorithm and 'hello' is the data passed into it

def sorted_data(data): # this is the algorithm
    return sorted(data)

# similarly
data = [10, 3, 1, -1] # this is the data structure

data_sorted = sorted_data(data)

print(data_sorted)

# if we were to retrive a data (last element) from a dynamic array vs a linked list

arr = [10, 20, 30, 40, 50]

# in a dynamic array we would be able to automatically index to the last element because they are all sequential in memory and is sorted
# however in a linked list, they are all seperated into different nodes so it would take 5 different visits

# Therefore, in the case of millions of data, the performance of the algorithm matters alot!
# we use big O notation to specify how long it takes 

# Array -> O(1) -> constant time
# Linked List -> O(n) -> linear time

# O(1) > O(n) is better 