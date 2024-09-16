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
