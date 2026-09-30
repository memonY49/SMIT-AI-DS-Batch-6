#mylist =[2,4.6,"ABC",True]
#print(mylist[2])

"""
user1 = ["Yasir","Nawaz","0300000000",27,
         "abc@gmail.com","abc123"]
labels = ["Name","FName","Phone","Age","Email","Password"]

useremail = input("Enter your email: ")
userpass = input("Enter your password: ")


if useremail == user1[4] and userpass == user1[5]:
    for i in range(6):
        print(f"{labels[i]}: {user1[i]}")
else:
    print("User not found!!")

"""

#step1: Store user details in a list where details are(name
#       ,fname, phone, age, email, password)
#step2: ask user for useremail and userpass
#step3: match useremail with emai in a list and
#       userpass with a pasword in a list
#step4: If matches print all details in list as:
#           Name: Yasir
#           FName: Nawaz
#           Phone: 030000000000
#           Age: 27
#           Email: abc@gmail.com
#           Password: abc123



details = ["Yasir","Nawaz","0300000000",27,
         "abc@gmail.com"]
labels = ["Name","FName","Phone","Age","Email","Password"]


#for value, label in zip(details, labels):
#    print(label, value)


for i in range(6):
        print(f"{labels[i]}: {details[i]}")


















