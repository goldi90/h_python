# String Slicing and other function in python srting
str0="The Quick Brown Fox Jumps Over The Lazy Dog"
str1="Kaushik is good boy"
print(str1)
print(len(str1))
print(str1[0:19]) #start:end:
print(str1[0:6:2]) #start: end:skipp(Note:2 start skipping one charnot one)
###################################Negative index
print("Negative index")
print(str1[-12:-1])
##################################Reserse number
print(str1[::-1])

##################################is.digit etc
print(str1.isalnum())
print(str1.isalpha())
print(str1.endswith("boy"))
print(str1.endswith("bob"))
print(str1.count("o"))
print(str0.capitalize())
print(str0.find("Fox"))
print(str0.lower())
print(str0.upper())

