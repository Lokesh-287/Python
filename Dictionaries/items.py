info={
    "name":"Loki",
    "age" : 20,
    "isMale":True,
    "fav food":["briyani","Dosa","Pongal"]
}

items_info=info.items()# this will return the each key and value as tupel
print(items_info)#dict_items([('name', 'Loki'), ('age', 20), ('isMale', True), ('fav food', ['briyani', 'Dosa', 'Pongal'])])

for key,value in items_info:
    print(f"key :{key} | value :{value} ")

    # or

for key,value in info.items():
    print(f"key :{key} | value :{value} ")

if "name" in info:
    print("yes name is present in info")