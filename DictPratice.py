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
"""

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










    
