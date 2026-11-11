"""
escape characters: 
	\" = "
	\' = '
	\\ = \
	\n = new line + cursor at position start
	\t = one tab space
	\b = backspace
	\r = carriage return

String Functions:
	1. capitalize(): "Make first Alphabet Capital" 
	2. lower(): "It converts all characters into lower"
	3. upper(): "It converts all characters into upper"
	4. count(element/member):"Counts the duplication of an alphabet"
	6. endswith(String): "It checks if the value string is ending with given String"
	.. startswith(String):
	7. find(element/member) "Finds the elements in any way if it is available or not"
	9. format()
        10. index(element/member) "Gets the location of an element same as find but it shows an error if the element is not available" 
	11. isalnum() "It Checks the string if it is alpha numeric or not"
	12. isalpha() "It Checks the string if it is aliphatic or not"
	13. isdecimal() "It Checks the string if it is decimal or of base 10 or not"
	14. islower() "It Checks the string if it is in lower case or not"
	15. isupper() "It Checks the string if it is in upper case or not"
	16. isnumeric() "It Checks the string if it is numeric or not"
	17. join() "It joins tow strings like same as + operator do"
	20. split(string by which to split) "It splits or breaks the string from the given string 
	21. lstrip(): "It removes all extra spaces and line breaks in a string from its left side only"
	22. rstrip(): "It removes all extra spaces and line breaks in a string from its Right side only"
	23. replace(replacing string, replacing with)
	24. strip() "It removes all extra spaces and line breaks in a string"
	25. swapcase()
	26. title()
"""


mystr = "AbCdEfGaAaHiJkLmN1"

#print(mystr.lower())
#print(mystr.upper())

#print(mystr.capitalize())
#print(mystr.title())
#print(mystr.count("A"))
#print(mystr.endswith("gggmN"))
#print(mystr.find("a"))
#print(mystr.index("a"))
#print(mystr.isalpha())
#print(mystr.isnumeric())
#print(mystr.isalnum())

#mymessage = "My name is {name},and Im a {desg}"
#print(mymessage.format(desg = "Teacher",
#                       name="Yasir"))

#mystr2 = "My name is Yasir"
#data = "Yasir Nawaz,Nawaz,03000000,28,abc@gmail.com,abc123"
#data_list = data.split(",")
#mylist = ["4","6","7","8","9","0"]
#print(",".join(mylist))


mystr3 = "\nabc 123\n"

print(mystr3.strip())

"""
Task1: Ask user to enter a message of atleast 10
words and than count how many words are there in
your message if words are >= 10 show your
message is aproved else say try again.

message = input("enter a message of 10 words:")
message_list = message.split(" ")
if len(message_list) >= 10:
    print("Message approved")
else:
    print("Try again")
"""
"""
Task2: You need to create a system to clean any
string. Use "    Yasir    Nawaz    " as string and
clean this string to convert in "Yasir Nawaz".

hint:(split,strip,join)

mystr = "    Yasir    Nawaz    "
mystr = mystr.strip()
mystr = mystr.split()
mystr = " ".join(mystr)
print(mystr)
"""

name = "Yasir-Nawaz1"
print(name.replace("a","@"))


















