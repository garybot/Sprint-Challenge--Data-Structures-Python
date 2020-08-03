import time
from singly_linked_list import LinkedList
from BST import BST

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# runtime is O(n^2) or is it O(2^n)?
#
# Replace the nested for loops below with your improvements
# for name_1 in names_1: # one n
#     for name_2 in names_2: # another n
#         if name_1 == name_2:
#             duplicates.append(name_1) # potentially a third n?

# maybe linked lists will help?

# ll_names_2 = LinkedList()
# for name in names_2:
#     ll_names_2.add_to_head(name)
# print("made a ll from an array")
# for name in names_1:
#     if ll_names_2.contains(name):
#         duplicates.append(name)

# duplicates = [name for name in names_1 if ll_names_2.contains(name)]

# well this works but doesn't use any of the data structures covered this week.
# duplicates = [x for x in set(names_1).intersection(set(names_2))]

# I think a binary search tree would work too.

bst = BST("init");
for name in names_2:
    bst.insert(name)
for name in names_1:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
