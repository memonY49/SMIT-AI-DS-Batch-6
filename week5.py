"""
    Nasted Loop:
        Loop inside a loop.
"""




#for i in range(5):
#    for j in range(4):
#        print(i, j)

for i in range(1,7):
    for j in range(i):
        print(i, end = '')
    print()




"""
1
22
333
4444
55555
666666
"""


"""
1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25
"""


"""
i = 1
while i<6:
    j = 1
    while j<6:
        print(i*j, end = ' ')
        j += 1
    print()
    i += 1
"""



while True:
    amount = int(input("Enter your amount: "))
    if amount % 500 == 0:
        print("5000: ",int(amount/5000))
        amount = amount % 5000
        print("1000: ",int(amount/1000))
        amount = amount % 1000
        print("500: ",int(amount/500))
        amount = amount % 500
        break
    else:
        print("Enter the multiple of 500 to withdraw!!!!")















