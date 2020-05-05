print("Code with me!!!")
print("*" * 10)

price = 100  # variable store the value temporary in memory so that we can use it in our program
price = 123  # integer value
ratings: float = 4.5  # floating value
name: str = "Kapil"  # String value
is_published = True  # boolean value (python is case sensitive language thus True and true aren't same

print(price)
print(ratings)
print(name)
print(is_published)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

patient_name: str = "John Smith"
age: int = 20
is_newPatient: bool = True  # you can set a data type help using followed by : (ex- : bool, : float etc..
print(patient_name)
print(age)
print(is_newPatient)

# What is PEP?
# PEP stands for Python Enhancement Proposal.
# A PEP is a design document providing information to the Python community,
# or describing a new feature for Python or its processes or environment.
# The PEP should provide a concise technical specification of the feature and
# a rationale for the feature.
# We intend PEPs to be the primary mechanisms for proposing major new features,
# for collecting community input on an issue,
# and for documenting the design decisions that have gone into Python.
# The PEP author is responsible for building consensus within the community and
# documenting dissenting opinions.
# Expression : a piece of code that produces value

name: str = input("What is your name? ")  # input() is used to get value from user
color: str = input("What is your favorite color? ")
print("{0} likes {1}".format(name, color))  # print(name + " likes " + color is
# equivalent to print("{0} likes {1}".format(name, color))
# and print(f"{name} likes {color}") --> f-string literal

birth_year = input("Birth year : ")
print(type(birth_year))  # type() tells the type of the supplied variable.
#  age = 2020 - birth_year  # gives you error beacause here we are subtracting string value by integer value
age = 2020 - int(birth_year)  # converting birth year as integer
#  like int() we have float() and bool()
print(age)
print(type(age))

print("Beginner's course")  # quotes example
print('Course for "beginners"')  # quotes example
print('''
Hi John!!!
this course is for beginners.
Thanks
Support Team.
''')  # print multi-line string

############# Strings ###################################

course = 'Python for beginners'
print(course[0])  # Output will be P
print(course[-1])  # Output will be s. We can use -ve indexing in python
print(course[-2])  # Output will be r.
print(course[0:3])  # Output will be Pyt
print(course[0:])  # print complete string
print(course[1:])  # print string starting from index 1
print(course[:5])  # output will be Pytho
print(course[:])  # print complete string
name = 'jeniffer'
print(name[1:-1])  # output eniffe
print(name[-3:-1])  # output fe
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'  # formatted string
print(message)
print(msg)
course = 'Python For Beginners'
print(len(course))
print(course)
print(course.capitalize())
print(course.upper())
print(course.lower())
print(course.find('P'))  # output index 0  # find() method is case sensitive
print(course.find('Pyt'))  # output index 0
print(course.find('yth'))  # output index 1
print(course.find('For'))  # output index 7
print(course.find('s'))  # output index 19
print(course.find('not'))  # output -1 if not present in string
print(course.replace('Beginners', 'absolute beginners'))
print('Python' in course)  # Output is True - if supplied sequence is present// search for exact match

# Lists are very similar to arrays.
# They can contain any types of variables, and they can contain as many variables as you wish.

numbers = [1,2,3]
strings = ["hello","world"]
names = ["John", "Eric", "Jessica"]
second_name = names[1]
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# Basic Operators
number = 1 + 2 * 3 / 4.0
print(number)  # output 2.5
remainder = 11 % 3
print(remainder)  # output 2
# Using two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 2 ** 3
print(squared)  # output 49
print(cubed)  # output 8

# Using operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)  # output - hello world
# Python also supports multiplying strings to form a string with a repeating sequence:
lotsofhellos = "hello" * 10
print(lotsofhellos)
# Using operators with lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers  # Lists can be joined with addition operator
print(all_numbers)  # output [1, 3, 5, 7, 2, 4, 6, 8]

print([1,2,3] * 3)  # Output [1, 2, 3, 1, 2, 3, 1, 2, 3]
# Just as in strings,
# Python supports forming new lists with a repeating sequence using the multiplication operator:

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# String Formatting
# Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with
# "argument specifiers", special symbols like "%s" and "%d".

name = "John"
print("Hello, %s!" % name)  # This prints out "Hello, John!"
name = "John"
age = 23
print("%s is %d years old." % (name, age))  # This prints out "John is 23 years old."
# Any object which is not a string can be formatted using the %s operator as well.
mylist = [1,2,3]
print("A list: %s" % mylist)  # This prints out: A list: [1, 2, 3]

# Here are some basic argument specifiers:
#
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)  # Hello John Doe. Your current balance is $53.44.

# Basic String Operation

astring = "Hello World!"
print(len(astring))  # output 12
print(astring.index("o"))  # output 4
print(astring.count("l"))  # output 3
print(astring[3:7])  # output lo w
print(astring[3:7:2])  # output l
print(astring[3:7:1])  # output lo w
print(astring[4:8:3])  # output oo
print(astring[::-1])  # output !dlroW olleH
print(astring.upper())  # output HELLO WORLD!
print(astring.lower())  # output hello world!
print(astring.startswith("Hello"))  # output True
print(astring.endswith("asdfgh"))  # output False


s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# Conditions
# Python uses boolean variables to evaluate conditions.
# The boolean values True and False are returned when an expression is compared or evaluated.
x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True
# Boolean operators
# The "and" and "or" boolean operators allow building complex boolean expressions,
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operator
# The "in" operator could be used to check
# if a specified object exists within an iterable object container, such as a list:

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
# The 'is' operator
# Unlike the double equals operator "==", the 'is' operator does not match the values of variables,
# but the instances themselves.
x = [1,2,3]
y = [1,2,3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False
# The 'not' operator
# Using 'not' before a boolean expression inverts it:
print(not False) # Prints out True
print((not False) == False) # Prints out False
# Loops
# The for loop
primes = [2,4,6,8]
for prime in primes:
    print(prime)
for x in range(5):
    print(x)  # Prints out the numbers 0,1,2,3,4
for x in range(3, 6):
    print(x)  # Prints out 3,4,5
for x in range(3, 8, 2):
    print(x)  # Prints out 3,5,7
# while loops
count = 0
while count < 5:
    print(count)  # Prints out 0,1,2,3,4
    count += 1

# "break" and "continue" statements
# break is used to exit a for loop or a while loop
# continue is used to skip the current block, and return to the "for" or "while" statement.

count = 0
while True:
    print(count)  # Prints out 0,1,2,3,4
    count += 1
    if count >= 5:
        break
for x in range(10):
    if x % 2 == 0:  # Check if x is even
        continue
    print(x)  # Prints out only odd numbers - 1,3,5,7,9

# "else" clause for loops
# When the loop condition of "for" or "while" statement fails then code part in "else" is executed.
# If break statement is executed inside for loop then the "else" part is skipped.
# Note that "else" part is executed even if there is a continue statement.
count = 0
while count < 5:
    print(count)  # Prints out 0,1,2,3,4
    count += 1
else:
    print("count value reached %d" % count)  # it prints "count value reached 5"

for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Functions

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1, 2)
print(x)

# function Example
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


# Classes and Objects
# Classes are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.
# A basic example of class


class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class.")
# to assign the above class(template) to an object we would do the following:
myobjectx = MyClass()
# Accessing Object Variables
print(myobjectx.variable)
# You can create multiple different objects that are of the same class(have the same variables and functions defined).
# However, each object contains independent copies of the variables defined in the class.
myobjecty = MyClass()
myobjecty.variable = "yackity"
print(myobjecty.variable)
# Accessing Object Functions
myobjectx.function()

# Example
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())