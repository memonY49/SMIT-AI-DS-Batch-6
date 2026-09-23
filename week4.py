
"""
Name = "Yasir"
Message = "My name is"

print(Message,Name,sep=' ',end = ' ')
print("and Im a teacher")






complete = Message+" "+str(20)
print(complete)



print("Yasir "*10)

for counter in range(1,12,2):
    print(counter)
"""


#for c in range(1,6):
#    print("*"*c)




"""

*
* *
* * *
* * * *
* * * * *


"""



#for i in range(10,1,-1):
#    print(i)




"""

----*
---* *
--* * *
-* * * *
* * * * *


"""
"""
n = 6
for i in range(1,n-1):
    print(" "*(n-i),"* "*i)
   

for i in range(1,n):
    print(" "*(i),"* "*(n-i))

"""

# Task:

"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""
"""
counter = 1
while counter < 10:
    print(counter)
    counter += 1
"""

"""
counter = 1
while counter <= 10:
    print(f"{counter} X 9 = {counter*9}")
    counter += 1
"""



"""
1 X 9 = 9
2 X 9 = 18
3 X 9 = 27
4 X 9 = 36
5 X 9 = 45
6 X 9 = 54
7 X 9 = 63
8 X 9 = 72
9 X 9 = 81
10 X 9 = 90
"""
# Task 2:
"""
n = int(input("Enter a number for table: "))
counter = 1
while counter <= 10:
    print(f"{counter} X {n} = {counter*n}")
    counter += 1
"""

#Task 3:
"""
total = 0
counter = 1
while counter <= 100:
    total += counter
    counter +=1
print(f"Total:{total}")
"""

#Task4:
"""
message = "SMIT AI AND DATASCIENCE"
for char in message:
    print(char)
"""
#Task5:
"""
n = int(input("Enter a number for fact!: "))
fact = 1
while n >= 1:
    fact *= n
    n -= 1
print("Fact!:",fact)
"""

#Task6
total = 0
num = 1
while num != 0:
    num = int(input("Enter a number: "))
    total += num


print("Total is:",total)
    









































