''' Array Lists (aka dynamic arrays, growable arrays, resizable arrays, dynamic tables, mutable arrays)
- Arrays inheritly dont have an add or delete function
- Arrays Lists server as wrappers for arrays and will manipulate an underlying array to give an array some extra features
- A python list is closer to an array list then an array 
- An array list deals with an evergrowing amount of data and also provide other operations
- It does this by allocating more space for an underlying array than is needed and then resizing it if you use all the space
'''


'''
Array List Time Complexity
- delete -> O(n)
- add -> O(1) average, O(n) worst case [when the whole array needs to be reallocated when the size limit is reached]
- update - O(1)
- read -> O(1)
'''

''' C implementation of an Array List
#include <stdio.h> 
#include <stdlib.h>

int main(void) {
    return 0;
}

'''