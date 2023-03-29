#functions

#def = define a function
def say_hi(name , age):
    print("hello" + name + " youre age is " + str(age) )

#flow of function def    
print("top")
say_hi(" Donatelo", '25' )
print("bottom")

say_hi(" Mike", '30')

#return statement

def cube(num):
    #returning a function
    return num*num*num
print(cube(3))
result =cube(4)

print(result)







