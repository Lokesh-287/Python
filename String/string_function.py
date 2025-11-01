
drive_name="Lokesh Krishna R"
print(drive_name.lower())
print(drive_name.upper())
print(drive_name.capitalize())


mobile="9876543210"
#      first 2 digit        last 2 digit
masked=mobile[:2]+"******"+mobile[-2:]
print(masked)


#title - this will captial the first letter of each word and others to lower case
song ="shape  OF YoU"
print(song.title())

#Replace(old,new)
location ="From chennai"
location=location.replace("chennai","Dharapuram")
print(location)

#Split("particular letter or word ") & strip() it will remove extra space

message="your role number is : 303 : save it for future use"
print(message.split(":")[1].split(":")[0].strip())

#in
promo_msg="use zomoto100 to get 100 off on your first order"
if("zomoto100" in promo_msg):
    print("Offer applied ")

#get the position of a particular word
feedback="the ui is very good , and also nice and good"
print(feedback.find("good"))# search from left
print(feedback.rfind("good")) # search from right
initials =" ".join([word[0].upper() for word in feedback.split()])
print(initials)

#length
print(len(initials))

#index(sub) | Like find(), but raises error if not found


#count() find the accurence in string
name ="lokesh krishna"
print(name.count("h"))

#startwith()
#endwith()

#isalpha()
#isdigit()
#isdecimal()
#isnumeric
#islower()
#isupper()
#istitle
