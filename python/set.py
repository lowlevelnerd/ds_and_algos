# Set is a mutable collection of data that does not allow any duplication.
# Basically used to include membership testing and eliminating duplicate
# entries.
# Data structure used is hashing, a popular technique to perform insertion,
# deletion, and traversal in O(1) on average.
# If multiple values are present at the same index position, then the value
# is appended to that index position, to form a linked list.
# Creating a set
sample_set = set([1, 3, 'Jane', 'Doe'])
# Accessing elements uding a for loop
for i in sample_set:
    print(i, end=' ')
print()

# Frozen Sets: Immutable objects that only support methods and operators
# that produce a result without affecting the frozen set or sets to which
# they are applied. 
# Elements of a frozen set cannot be modified.
_set = set([1, 2, 3, 4])
frozen_set = frozenset(_set)
