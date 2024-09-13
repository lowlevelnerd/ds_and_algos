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


# Tuples
# Set
# Dictionary
