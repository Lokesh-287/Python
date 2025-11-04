info={
    "name":"Loki",
    "age" : 20,
    "isMale":True,
    "fav food":["briyani","Dosa","Pongal"]
}
print(info)
info["city"]="dharapuram"
print(info)

info.update({"pincode":638673})
x = {"country": "India", "isMale":True}
info.update(x)
print(info)

info.update(name="Lokesh krshnae")