# Python Lists are ordered collections of data.
# Lists allow different types of elements together.
# Costly operation is inserting or deleting the element
# from the begining of the List since all the elements
# will need to be shifted.
# Insertion and deletion at the end of the list can also
# become costly where the preallocated memory becomes full.
sample_list = [1, 2, 3, 'a string', 1.2]
print(sample_list) # Output: [1, 2, 3, 'a string', 1.2]
# List elements can be accessed by the assigned index.
# In Python starting index of the list, a sequence is 0
# and the ending index is (if N elements are there) N-1
#
# List Operations
sample_list = [1, 2, 3, 'a string', 1.2]
# Access elements
print(sample_list[3]) # Output: 'a string'
