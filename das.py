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


# Tuples
# Set
# Dictionary
