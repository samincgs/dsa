''' Arrays (is a sequence of data that is stored one after another in memory)
- Array will have a starting index where a pointer is assigned and then it is incremented in memory to access the element of the array
- Arrays are usually a specified length (designated endpoint) -> usually is relocated if expanding past the specified length
- In lower level languages like c -> an array is usually declared with a big amount of memory then needed and slowly expanded int big_arr[16];
- If you need an array with an unknown amount of space, usually an array with a big size is specified and then if it is passed then it is deleted and allocated double the space in memory
- Lists are not arrays! but they use arrays on a lower level 
'''

my_list = [5, 7, 1, 13, 92, 47, 19, 0]

''' Array Time Complexities (where n is the size of the array)
 read - O(1) -> doesnt matter how much data is in the array, if you know the index of the item then you can access it immediately
 search - O(n) -> if the index is not known, we need to go through each item in the array
 update - O(1) -> if the index is known, the update operation is instant
 add - not possible
 delete - not possible
 '''