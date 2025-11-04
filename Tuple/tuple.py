thistuple = ("apple",)
print(type(thistuple))#<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #<class 'str'> without , comma the python see the parantheses as a grouping to avooide this
#menthioning with comma to indicate this is a tuple not aq string


#to create a single element tuple we should use , comma

tupel=1,2,3,4,5
print(type(tuple)) #this is also a tuple

def func():
    return 1,2,3
print(func(),type(func())) # this also return the tuple

