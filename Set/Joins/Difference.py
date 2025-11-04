# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#
# Example
# Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

set4 = set1 - set2
print(set4)
#
# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
#
# Example
# Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)