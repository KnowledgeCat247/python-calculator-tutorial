# This is a Python Helper

### By Ezekiel Bruijn
___

## How to Output

~~~python
print("Something")
~~~
___

## How to Input

~~~python
answer = input()
~~~
___

## How to change a variable

~~~python
int = 5
print(type(int))
print(int)

int = float(int)

print(type(int))
print(int)
~~~

___

## How to do if Statements

~~~python
if answer == 5:
    #Can't do a string + a int or a float
    print("answer is ", 5)
~~~

___
## How Lists Work

~~~python
List = [1,2,3,4,5]
#This will output index 0 (1) from the list
print(List[0])

# You can also do this negatively from right to left
# This will output 5
print(List[-1])

# We can also change an item in the list
List[0] = 25

# We can also add things to a list

List.append(33)

# We can also remove a list item
List.remove(3)
~~~

___

## How To Do For Loops

~~~python
list = ["garden", "kitchen", "garage"]

# How this for loop works is that for every item in the index(i) of the list
# it will print out "The" index "is needing to be done"
for i in list:
    print("The", i, "is needing to be done")


# We can also loop through a single string
# and in this example we use that to create an uppercase alphabet
char = []
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    char.append(i)

print(char[0])

#Let us break from a for loop in this example

randNumbers = [33,55,34,25]

for i in randNumbers:
    print(i)
    if i == 55:
        break

# Or we could continue the loop
#In this example though we are skipping over the 55 (Not outputting it)
for i in randNumbers:
    print(i)
    if i == 55:
        continue

# When will this be done?

for i in char:
    print(i)
else:
    print("This is now done after 27 letters in the Alphabet")
~~~

___

## How to Do Functions

~~~python
def function():
   print("I hate Cheese!")

function()

# VERY IMPORTANT
int = 5

def function():
    # This makes sure that your getting the variable outside of the function
    global int
    print(int)

# Else you'd get this:
def function():
    int = 29
    print(int)

## You could also put in arguments into the function
def function(name):
      print(name, "had lunch")
~~~
___

## How to do Classes

~~~python
class person:
    def function():
        print("Awesome, I'm alive!")

# A lot of classes need constructors, how do we do that?

class teacher:
    # The self argument is important in class constructors in Python
    def _init_(self, name, age, gender, period):
        self.name = name
        self.age = age
        self.gender = gender
        self.period = period
    
    # We can also add functions to classes
    def nameCall(self):
        print(self.name, "Present!")

mrsBerkley = teacher("Bark Berkley", 34, "female", "math")

# This will output Mrs. Berkley's name
mrsBerkley.nameCall()
~~~
___

## How to import other py files

~~~python
# Only do this if it's in the same directory
import art

#if it's not in the same directory then:
import functions
# That functions.path.append will get the relative path of the file
functions.path.append('/path/to/application/app/folder')

# if you only want to import a function:
from doge import function

function()
~~~
___

That is all I have gathered so far, Thank you!






