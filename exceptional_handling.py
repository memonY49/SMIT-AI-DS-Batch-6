"""
Exceptional Handling: Is used to handle runtime
errors.
-> EH has two clauses Try and Except
-> Try clause is used to check te code that can
   show an error.
-> Except clause would be executed if there is
   any error in try code.
"""
"""
mylist = [1,2,4,5,8,9]

#print(mylist[9])

try:
    raise(Exception("Yasir is Hacking"))
    #mylist[9]
    x = int(input("Enter a number1 to add: "))
    y = int(input("Enter a number2 to add: "))
    
    print(x+y)
except IndexError:
    print("Index is not available in the list")
except ValueError:
    print("Please Enter int only")
except Exception as e:
    print("Something went wrong...\nerror:",e)
"""
"""
Task: Create a Never ending Banking app where:
-> Show user a menu (1. View Balance, 2. withdraw,3. Deposit,
   0. Exit)
-> Create if/elif statements for every function and add 'try
   and except' for handling runtime errors
Note: Application shows Welcome to the owner and greating
while leaving.
"""

accountTitle = "Yasir Nawaz"
balance = 0

while True:
    print("===================")
    print(f"  Welcome {accountTitle}")
    print("===================")
    print("1. View Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("0. Exit")
    userinput = input("Enter you Selection: ")
    if userinput == "0":
        break
    elif userinput == "1":
        print("----------------------")
        print(f"Your Balance is: {balance}")
        print("----------------------")
    elif userinput == "2":
        print("----------------------")
        try:
            amount = int(input("Enter amount to withdraw:"))
            if amount <= balance:
                if amount % 500 == 0:
                    balance -= amount
                else:
                    print("Amount should be multiple of 500")
            else:
                print("Insufficient Balance...!!!")
        except ValueError:
            print("Invailed input.....")
    elif userinput == "3":
        try:
            amount = int(input("Enter amount to Deposit:"))
            if amount % 10 == 0:
                balance += amount
            else:
                print("Amount should be more than 9")
        except ValueError:
            print("Invailed input.....")
    else:
        print("Wrong Selection...!!!")
           









