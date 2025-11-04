#converting tuple to list is possible
tuple=(1,2,3,4,5)
list=list(tuple)
list.append(10)
print(list,type(list))


#adding tuple to tuple is allowed in pyhton
tuple2=1,
tuple+=tuple2
print(tuple)