# Tuples are immutable.
# Tuples can contain elements of various types
# To create a tuple of one element there must be 
# a trailing comma.
# For example, (4,) will create a tuple containing
# 4 as the element.
sample_tuple = ('Jane', 'Doe', 'John')
# Create a tuple with use of list
sample_list = ['Jane', 'Doe', 'John']
make_it_a_tuple = tuple(sample_list)
print(make_it_a_tuple) # Output: ('Jane', 'Doe', 'John')
# Elements in a tuple can be accessed by indexing
print(sample_tuple[0]) # Output: 'Jane'

