global_Variable= "Its is Global String" #Global Variable

def Function():
    local_variable="Its is Local String"
    print(local_variable)

Int =10
Float =10.00
bool=True


print(global_Variable,type(global_Variable))
Function()
print("Integer : ",Int,type(Int))
print("Float : ",Float,type(Float))
print("Bool : ",bool,type(bool))