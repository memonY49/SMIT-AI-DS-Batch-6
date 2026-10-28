# Dictionary: is an unordered collection of key and value pair.


mydict = {"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03000000000",
          "age":28,
          "email":"abc@gmail.com",
          "pass":"abc123"}

#print(mydict["email"])
"""
for v in mydict:
    print(v)
"""
#dict methods:
    # .keys()
    # .values()
    # .items()


#print(list(mydict.values()))
"""
for v in mydict.values():
    print(v)
"""
#print(mydict.items())
#for k, v in mydict.items():
#    print(k, v)
"""
mydict["email"] = "xyz@gmail.com"
mydict["add"] = "jkbsajhbvjhsavbjhasv"


del mydict["email"]
del mydict
print(mydict)
"""
"""
std = {"Urdu": 50,
        "Sindhi": 60,
        "Math": 80,
        "Science": 85,
        "English": 90
        }
Task1: create a dictionary with 5 subjects with their marks.
-> find total marks.
-> find total % out or 100% (max marks are 500).
                            (obtain/total)*100
-> find average marks. (obtain)/no of subjects
-> find max marked subject.


std = {"Urdu": 50,
        "Sindhi": 60,
        "Math": 80,
        "Science": 85,
        "English": 10,
       "Computer": 90
        }

Total = len(std)*100
Obtain = 0
Maxsubject = ""
Max = 0
for k,v in std.items():
    Obtain += v
    if Max < v:
        Max = v
        Maxsubject = k
    
    

print("Obtain Marks:",Obtain)
print("Total %:",Obtain/Total*100)
print("Average:",Obtain/len(std))
print("Max Subject:",Maxsubject)
"""
"""
Task 1:Product Price Calculator
    Create a dictionary containing five products and their prices.
    Requirements:
        1.Display all products and their prices.
        2.Ask the user to enter a product name.
        3.Display its price if the product exists.
        4.Display an appropriate message if the product does not exist.

product = {
        "Mouse": 500,
        "Keyboard": 1000,
        "Laptop":30000,
        "PC": 20000,
        "Monitor":10000
    }

for k, v in product.items():
    print(f"{k}: {v}")
    
user_input = input("Enter product name: ")

if user_input in product.keys():
    print("*"*20)
    print(f"Product: {user_input}\nPrice: {product[user_input]}")
    print("*"*20)
else:
    print("Pruct does not exist...!!")
"""
"""
Task 2: Student Marks Management
    Create a dictionary containing the marks of five students.
    Requirements:
        1.Store each student's name as a key and marks as a value.
        2.Display all students and their marks using a loop.
        3.Calulate the average marks.
        4.Find the student with the highest marks.
        5.Find the student with the lowest marks.
        6.Count how many students passed, assuming 50 marks are required to pass.

std = {"Usama": 30,
        "Ayan": 49,
        "Hasnain": 80,
        "Yasir": 85,
        "Waqas": 80,
       "Zubair": 90
        }
total = 0
MaxMarks = 0
MaxStd = ""
MinMarks = 100
MinStd = ""
Passed = 0
for k, v in std.items():
    print(f"{k}: {v}")
    total += v
    if MaxMarks < v:
        MaxMarks = v
        MaxStd = k
    if MinMarks > v:
        MinMarks = v
        MinStd = k 
    if v >= 50:
        Passed +=1
print("*"*20)
print(f"Average: {total/len(std)}")
print(f"Student with max marks: {MaxStd} with {MaxMarks}")
print(f"Student with min marks: {MinStd} with {MinMarks}")
print(f"No: of students passed: {Passed}")
print("*"*20)
"""
    
"""
Task 3:Character Frequency Counter
    Write a Python program that counts how many times each
    character appears in a string.
    Requirements:
        1.Ask the user to enter a string.
        2.Count the frequency of every character.
        3.Ignore spaces.
        4.Display each character and its frequency.
    Example input:
        programming
    Expected output:
        {p:1,r:2,o:1,g:2,a:1,m:2,i:1,n:1}



user_str = input("Enter any string: ")
str_count = {}
for char in user_str:
    str_count[char] = user_str.count(char)


print(str_count)
"""


data = {"std1":{"name":"Yasir1",
                "fname":"Nawaz",
                "phone":"03000000000",
                "age":28,
                "email":"abc@gmail.com",
                "pass":"abc123"},
        "std2":{"name":"Yasir2",
                "fname":"Nawaz",
                "phone":"03000000000",
                "age":28,
                "email":"abc@gmail.com",
                "pass":"abc123"},
        "std3":{"name":"Yasir3",
                "fname":"Nawaz",
                "phone":"03000000000",
                "age":28,
                "email":"abc@gmail.com",
                "pass":"abc123"}}
#print(data["std1"]["email"])
for stdid, student in data.items():
    print(student["pass"])

"""
Week Task: Create a multi dimensional Dict to store details for atleast five students and ask
user for a user_email and user_pass and than match user_email with email in every dictionary
and user_pass with pass in every dictionary. If matched print all details of that student
else print "user not found".
Note: Output should be well detailed.
"""




































    
