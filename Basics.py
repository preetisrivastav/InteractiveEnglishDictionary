#Variable are used to store objects
#In the following the variable name is character and the variable type is string
#String can be declared using single or double quotes
#The type of the of the variable can be found using the type command type()
character = "Jon Snow"

#In the following section price is a variable and the variable type in integer
price = 10
print(price)

#Math Operators
x = 1
y = 2
z = 3
result = ((x*y)**z)/8
print(result)

#Simple Sum
a = 1.0
b = 2
c = int(a)
result = c + b
print(result)

#list is defined by listname = [listitem1, listitem2, etc]
#first list item has an index of 0 in positive indexing
#last list item has an index of -1 in negative indexing 
#Slice of a list can be found using listname[x:y] - it is upper bound exclusive with the index starting from zero
#negative slicing can be done too [-lastlistitem,till the number require]
#print function can have multiple arguments
mylist = ["ListItem1",2,3.0]

#print only h from the following
name = "John"
print(name[-2:-1])

#Print 'hn '
#The character 'J' is the name[0]
name = "John Smith"
print(name[2:4])

#Print the letter y
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-2:-1])

#Print the letters xy
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-3:-1])

#Print the 18th item of the list
#print mylist[17:18] returns the 'slice of a list' but mylist[17] returns the value in the index 
#The datatype is different
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17])

#print(dir(list))
#print(help(list))

#indexing does not work for dictionaries data type
mydict = {"Student1":1,"Student2":2}

#Input function will always send out a string function
#def <functionname>(<arguments>):

#Calculate length of string
mystring = input("Enter the input string: ")
def string_length(mystring):
    if type(mystring) == int:
         return "Please enter strings not integers"
    elif type(mystring) == float:
         return "Please enter strings not floating point values"
    else:
         return len(mystring)
print(string_length(mystring))

#program to convert Celcius to Fahrenheit
CelciusInput = float(input("Enter the temperature in celcius : "))
def converter(CelciusInput):
    return (CelciusInput*(9/5)+32)
print("Temperature in Fahrenheit is :")
print(converter(CelciusInput))

#program to read contents of a file

myfile = open("fruits.txt")
contents = myfile.read()
print(contents)














