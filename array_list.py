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

#C implementation of an Array List
include <stdio.h> 
include <stdlib.h>

define BASE_CAPACITY 10

typedef struct ArrayList {
    int *data; (pointing to the beginning of the array of integers)
    int size; (current amount of items)
    int capacity; (how much the array size is gonna start at)
} al;

al * create_al(void) {
    al * new_al = malloc(sizeof(al));
    new_al->capacity = BASE_CAPACITY;
    new_al->size = 0;
    new_al->data = calloc(new_al->capacity, sizeof(int));
    return new_al;
}

void append_al(al * target_al, int val) {
    target_al->data[target_al->size] = val;
    target_al->size++;
    if (target_al->size == target_al->size) {
        printf("Realloc %d\n", target_al->capacity);
        target_al->capacity *= 2;
        target_al->data = realloc(target_al->data, sizeof(int) * target_al->capacity);
    }
}

void print_al(al * target_al) {
    for (int i = 0; i < target_al->size; i++) {
        printf("%d\n", target_al->data[i]);
    }
    printf("\n");
}

int main(void) {
    al* my_array_list = create_al();
    
    append_al(my_array_list, 2);
    append_al(my_array_list, 5);
    append_al(my_array_list, 3);
    
    print_al(my_array_list);
    
    printf("%d\n", my_array_list->capacity);
    return 0;
}

