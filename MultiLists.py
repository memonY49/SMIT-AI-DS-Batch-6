#list of lists
"""
my2dlist = [
            [1,5,7,8],
            ['a','b','c','d'],
            [True, False, 7.8, 9.0]
            ]

print(my2dlist[0][1])
print(my2dlist[2][1])


my3dlist = [
            [
              [4,7,8,9],
              [1,4,5,6]
                ],
            [
              [4,6,9,0],
              [0,3,4,2]
                ]
            ]

print(my3dlist[1][1][1])
"""
"""
data = [["Yasir1","Nawaz","030000000","abc1@gmail.com","abc123"],
        ["Yasir2","Nawaz","030000000","abc2@gmail.com","abc123"],
        ["Yasir3","Nawaz","030000000","abc3@gmail.com","abc123"],
        ["Yasir4","Nawaz","030000000","abc4@gmail.com","abc123"],
        ["Yasir5","Nawaz","030000000","abc5@gmail.com","abc123"],
        ]

useremail = input("Enter your email: ")
userpass = input("Enter your password: ")

for element in data:
    if useremail == element[3] and userpass == element[4]:
        print("Name:",element[0])
        print("FName:",element[1])
        print("Phone:",element[2])
        print("Email:",element[3])
        break
else:
    print("Email and password is incorrect!!!")
"""    



#Weekly Task:
    #step1: show a menu to user as follows:
        # 1. Toyota
        # 2. Suzuki
        # 3. Honda
    #step2: Ask user to select any company.
    #step3: than show a menu for cars as follows:
        # 1. Corolla
        # 2. Cross
        # 3. Fortuner
    #step4: Ask user to select any car.
    #step5: Show all details about that car as follows:
        # Company: Toyota
        # Name: Corolla
        # Year: 2007
        # Model: GLI
        # Price: 1500000

"""
mylist = ["a","b","c"]

for i,e in enumerate(mylist):
    print(f"{i+1}. {e}")
"""
        

cardata = [
            [["Toyota","Corolla1",2007,"GLI",1500000],
             ["Toyota","Corolla2",2007,"GLI",1500000],
             ["Toyota","Corolla3",2007,"GLI",1500000],
             ["Toyota","Corolla4",2007,"GLI",1500000]],
            [["Suzuki","Mehran1",2008,"VXR",800000],
             ["Suzuki","Mehran2",2008,"VXR",800000],
             ["Suzuki","Mehran3",2008,"VXR",800000]],
            [["Honda","City1",2010,"Aspire",2200000],
             ["Honda","City2",2010,"Aspire",2200000],
             ["Honda","City3",2010,"Aspire",2200000]],
            [["Kia","Spotage",2018,"Gen 1", 6000000]
             ]
            ] 

"""
for company in cardata:
    print(company[0][0])
    

usercomp = input("Enter your selection: ")


for company in cardata:
    if company[0][0] == usercomp:
        for car in company:
            print(car[1])
            


usercar = input("Enter your selection: ")


for company in cardata:
    if company[0][0] == usercomp:
        for car in company:
            if car[1] == usercar:
                print(car)


"""

"""
for i,company in enumerate(cardata):
    print(f"{i+1}. {company[0][0]}")

usercomp = int(input("Enter your selection: "))

if usercomp >= 1 and usercomp <= len(cardata):

    for i,car in enumerate(cardata[usercomp - 1]):
        print(f"{i+1}. {car[1]}")
        

    usercar = int(input("Enter your selection: "))

    if usercar >= 1 and usercar <= len(cardata[usercomp -1]):
        print(cardata[usercomp -1][usercar - 1])
    else:
        print("Wrong Selection!!!")

else:
    print("Wrong Selection!!!")
"""





"""
Create a never ending atm application which shows a menu:
        Welcome Yasir Nawaz
        Options:
            1. Withdraw
            2. Deposit
            3. View Balance
            0. Exit
            
"""

acc_title = "Yasir Nawaz"
acc_balance = 0

while True:
    print(f"Welcome {acc_title}")
    print("Options")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. View Balance")
    print("0. Exit")

    userinp = int(input("Enter your selection: "))

    if userinp == 0:
        break
    elif userinp == 1:
        amount = int(input("Enter your amount to withdraw: "))
        acc_balance -= amount
        print(f"Balance: {acc_balance}")
        
    elif userinp == 2:
        amount = int(input("Enter your amount to deposit: "))
        acc_balance += amount
        print(f"Balance: {acc_balance}")
        
    elif userinp == 3:
        print(f"Balance: {acc_balance}")
    else:
        print("Wrong selection!!!")





































