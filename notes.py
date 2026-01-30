#sets:
    set is a collection of different datatype , unique elements. it is mutable and represents with '{}'

#properties:-
    1. set allows unique elements except list
    2. set is unordered collection
    3. set does not support index and slicing
    4. set is mutable
    5. set allows hashabale datatypes
# empty set:
 s1 = {} # dictionary
 s2 = set() #.set
 s = set(map(int, input().split())

# operations:-
         union, intersection, difference, symmetric difference,
# checking sets:-
         is_subset, is_superset, is_disjoint

# functions:
         add()#only if number is not there it is going to be added
         remove(),discard(),pop()#deletes (removes element if present if not key error), pop removes randomly, and discard removes if not founf does nothing
time complexity - list (O(n))
''     ''       - set (1)
hw:-
book management with set and dictionary: set book reg number , dict stores book details(name, author, quantity, )
operations: add book, delete book, update book count, total books, all books, borrowed books
 