''' Selection Sort
Why is sorting important?
- Many data structures are dependant on sorted data to be performant

SELECTION SORT
- very similar to a method people use for when people are sorting objects in real life
- The basic idea is to continually look for the smallest value and put it in the front till you have everything sorted
- method goes through the whole array and finds the smallest number and swaps it with the index at the front and onwards
- Selection Sort Runtime: (n - 1)(0.5n) -> O(n^2) [SLOW]
- The best case and the worse case is both O(n ^ 2)
'''

import random

def random_list(length):
    l = [random.randint(-50, 9999) for i in range(length)]
    return l

def selection_sort(target_list):
    for start_i in range(len(target_list)):
        lowest_i = start_i
        # finds smallest value that occurs after start i
        for check_i in range(start_i + 1, len(target_list)):
            if target_list[check_i] < target_list[lowest_i]:
                lowest_i = check_i
        
        # just swapping the values (with the lowest and start value)
        target_list[start_i], target_list[lowest_i] = target_list[lowest_i], target_list[start_i]
        
    return target_list

def selection_sort_fast(target_list):
    for start_i in range(len(target_list)):
        check_list = target_list[start_i:]
        lowest_i = check_list.index(min(check_list)) + start_i
        target_list[start_i], target_list[lowest_i] = target_list[lowest_i], target_list[start_i]
    return target_list

l = random_list(10) # becomes very slow as input size increases (time increases n^2)
print('Random values: ' + str(l))
print('Sorted values: ' + str(selection_sort(l)))
