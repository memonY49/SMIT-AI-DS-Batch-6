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

"""

details = ["Yasir","Nawaz","0300000000",27,
         "abc@gmail.com"]
labels = ["Name","FName","Phone","Age","Email","Password"]


#for value, label in zip(details, labels):
#    print(label, value)


for i in range(6):
        print(f"{labels[i]}: {details[i]}")

"""

#Tuple:
"""
mytuple = (1,2,5,6,8,9)
print(mytuple[5])
"""

#Sets:
"""
myset = {False,3.4,"A",0}
print(myset)
"""

#List Methods:

#mylist = [2,5,8,9,5,2]
#mylist.append(90)
#mylist.extend([2,7,8,9])
#mylist.insert(2,7)
#mylist.clear()
#deleted_element = mylist.pop(1)
#mylist.remove(5)
#mylist.reverse()
#mylist.sort(reverse = True)

#print(mylist.count(8))
#print(len(mylist))
#print(mylist.index(9))

#print(mylist)
#print(deleted_element)

#counting = mylist.count(5)

#for i in range(counting):
#    mylist.remove(5)

#print(mylist)
    


#task1: Create a list of integers, separate even and
#       odd numbers by creating two separate lists one for
#       even and one for odd numbers.
"""
numbers = [1,4,5,7,8,9,20,23,67]
even  = []
odd = []
for element in numbers:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)
print("even number:",even)
print("odd number:",odd)
"""


#task2: Find common elements in two avaiable list and create
#       a new list.
"""
list1 = [1,4,5,8,9]
list2 = [2,5,8,0,7]
common = []
for element in list1:
    if element in list2:
        common.append(common)
print(common)
"""


#task3: Find all pairs whos sum is equal to 9.
#       list = [2, 4, 3, 7, 5, 8, 9, 1]
#       output:
#               [(2, 7),(4, 5), (8, 1)]

mylist = [2, 4, 3, 7, 5, 8, 9, 1]
pairs = []
for i in range(len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i]+mylist[j] == 9:
            pairs.append((mylist[i],mylist[j]))

print(pairs)






























