set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
myset2 = set1 | set2 | set3 |set4
print(myset)
print(myset2)