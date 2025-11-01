fruits = ["apple", "banana", "cherry"]

fruits.remove("apple") #it remove first match
fruits.pop(0) # remove at the index
fruits.pop() # remove last index
fruits.clear()# remove all from index

len(fruits)

for fruit in fruits:
    print(fruit)

if("apple" in fruits):
    print("apple is present in the list")