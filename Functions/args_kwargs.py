#args

def addition(*args):
    total=0
    for i in args:
        total+=i
    return total
print(addition(1,3,4,5,6,7))

#**kwargs (for key value pairs)
def function(**kwarg):
    for key,value in kwarg.items():
        print(f"{key} = {value} ")

function(name="loki",age=20)