# Lists
# Might contain items of different types, but usually the items
# all have the same type
squares = [1, 4, 9, 16, 25]
print(squares) # Outputs: 1, 4, 9, 16, 25
# Lists can be indexed
print(squares[2]) # Output: 9
# Lists are mutable(changeable cintent):
squares[2] = 400
print(squares) # Output: 1, 4, 400, 9, 16, 25
# To add new item to the list: append()
print(squares.append(0)) # Output: 1, 4, 400, 9, 16, 25, 0
# List length: len()
print(len(squares)) # Output: 7
# Lists can be nested: Creating list that contains lists
list_one = ['a', 'b', 'c']
list_two = [1, 2, 3]
list_three = [list_one, list_two]
print(list_three) # Output: ['a', 'b', 'c'], [1, 2, 3]
# Methods on Lists
#
sample_list = [1, 2, 3, 4]
# .append(): add an item to the end of list. Equivalent to a[len(a):] = [x]
print(sample_list.append(5)) # Output: 1, 2, 3, 4, 5
# .extend(iterable): Extend the list by appending all items from the iterable. Equivalent to a[len(a):] = iterable
print(list_one.extend(list_two)) # Just like nesting
# .insert(i, x): Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)
print(sample_list.insert(5, 6)) # Output: 1, 2, 3, 4, 5,6
# .remove(x): Remove the first item from the list whose value is equal to x. Raises ValueError if there is no such item
sample_list = [1, 2, 3, 4, 7]
print(sample_list.remove(7)) # Returns: None because there is no first item whose value = 7
# .pop([i]): remove the item at a given position in the list, and return it. 
sample_list = [1, 2, 3, 4, 7]
print(sample_list.pop(2)) # Returns: 3
# if no index is specified, a.pop() removes and returns the last item in the list.
# returns IndexError if the list is empty or the index is outiside the list range.
# .clear(): remove all items from the list. Equvalent to del a[:]
# .index(x[, start[, end]]): return zero-based index in the first item whose value is equal to x. Raises ValueError if there is no such item.
# .count(x): return number of times x appears in the list.
sample_list = [1, 2, 3, 4, 7]
print(sample_list.count(3)) # Should return 1
# .sort(*, key=None, reverse=False): sort the items of the list in place
# .reverse(): reverse the elements of the list in place
# .copy(): return a shalloe copy of the list. Equivalent to a[:]
#
# Using Lists as Ques (first-in, first-out) but it is not effective
# Use collections.deque to implement a queue
from collections import deque

queue = deque(['John', 'Jane', 'Doe'])
queue.append('Oloo') # Oloo arrives
queue.append('Flopp') # Flopp arrives
queue.popleft() # The first to arrive now leaves
# 'John'
queue.popleft() # The second to arrive now leaves
# 'Jane'
queue # >>> deque(['Doe', 'Oloo', 'Flopp'])


# Tuples
# Set
# Dictionary
