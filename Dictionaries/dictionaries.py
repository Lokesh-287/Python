# dictionaries are use to store a key value pairs like map in java
#duplicates are not allowed
info={
    "name":"Loki",
    "age" : 20,
    "isMale":True,
    "fav food":["briyani","Dosa","Pongal"]
}
print(info)
print(len(info))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print(info["name"])
#or
print(info.get("name"))
 # to update
info["name"]="Lokesh Krihsna"
print(info)

"""
info["name"] → ❌ error if key not found.

info.get("name") → ✅ returns None if key not found.
"""

#keys() this will give all keys
l=list(info.keys())
print(l)

#values()
list1=list(info.values())
print(list1)

