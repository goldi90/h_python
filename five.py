# list and list function
grocery=["harpic"," vim bar","graninula","deo","soyabin",22]
print(grocery)
print(grocery[4])
# print(grocery[6]) Erroe
number=[2,7,9,11,3]
#number.sort() #short list
#number.reverse()#reverse
print(number)
#########slicing
print("slicing")
print(number[:4])
print(number[::2])#one step skip
print(number)
###########mini max len
#print(len(number))
#print(max(number))
#print(min(number))
###########append,insert,pop
number.append(71) # insert 71 at last of list[]
#print(number)
number.insert(1,52)# here 1 is index number and 52 is value to be inserted
print(number)
number.remove(52)# remove number 52  from list
print(number)
number.pop() # remover last value from list[]
print(number)
number[1]=21
print(number)
#mutbale =can change
#immutable=cant` changeprint
print("tuples")
#tp=(1,2,3)
#print(tp)
# swap number
a=1
b=8
a,b=b,a
print (a,b)
