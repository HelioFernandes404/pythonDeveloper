from __future__ import print_function

# Basic Syntax
print("Hello World")

## Reserved Words

# and as assert break class continue def del elif else except exec finally for from global if import in is lambda not or pass print raise

# Variables and Data Types
name = "John"
age = 25

type(name)  # <class 'str'>
type(age)  # <class 'int'>

# Coditionals
if "foo" in ["bar", "baz", "qux"]:
    print("Expression was true")
    print("Executing statement in suite")
    print("...")
    print("Done.")
print("After conditional")

# Does line execute?                        Yes    No
#                                           ---    --
if "foo" in ["foo", "bar", "baz"]:  #  x
    print("Outer condition is true")  #  x

    if 10 > 20:  #  x
        print("Inner condition 1")  #        x

    print("Between inner conditions")  #  x

    if 10 < 20:  #  x
        print("Inner condition 2")  #  x

    print("End of outer condition")  #  x
print("After outer condition")  #  x

# Loops
count = 0
while count < 5:
    count = count + 1
    print("Hello World")

# While loop with else
count = 0
while count < 5:
    count = count + 1
    print("Hello World")
else:
    print("In else Black")

# For loop
n = 4
for i in range(0, n):
    print(i)

# For loop with Dictionary
d = dict({"foo": 1, "bar": 2, "baz": 3})
for i in d:
    print("key: %s, value: %d" % (i, d[i]))

# Dictionary output
# key: foo, value: 1
# key: bar, value: 2
# key: baz, value: 3

# Index of Sequences
list = [1, 2, 3, 4, 5]
for index in range(len(list)):
    print(list[index])

# For loop with else
list = [1, 2, 3, 4, 5]
for index in range(len(list)):
    print(list[index])
else:
    print("In else block")

## Index of Sequences
list = ["apple", "banana", "cherry"]
for index in range(len(list)):
    print(list[index])
# Output: apple banana cherry    

## Nested loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 

## Loop control statements
### Continue statement
for letter in "python":
    if letter == "h":
        continue
    print("Current Letter: ", letter)
### Break statement
for letter in "python":
    if letter == "h":
        break
    print("Current Letter: ", letter)
    # Output : Current Letter:  h
### Pass statement
for letter in "python":
    if letter == "h":
        pass
        print("Last letter: ", letter)
    print("Current Letter: ", letter)
### How for loops internally in Python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
fruit = ["apple", "banana", "cherry"]
iter_obj = iter(fruit)
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break
# output: apple banana cherry

# Type Casting

## Two types of type casting (Implicit and Explicit)

# Integer to float
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# Display the new number and result data type
print("Value ", new_number)
print("Data type", type(new_number))

## Addition of string and integer using explict conversion
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting: ", type(num_string))
# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting: ", type(num_string))

num_sum = num_string + num_integer

print("sum: ", num_sum)
print("Data type of sum: ", type(num_sum))


# Exceptions

## Python Exceptions

### Python Built-in Exceptions
print(dir(locals()['__builtins__']))

### Python Error and Exception
# Python try...except Block
try:
    # block of code
    pass
except Exception as e:
    # block
    pass

# Exception handling using try... except
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print("Result: ", result)
except:
    print("Error: Division by zero")

# Catchinh specific exception in Python
try:
    even_numbers = [2, 4, 6, 8, 10]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Error: Division by zero")
except IndexError:
    print("Error: Index out of range")

# Python try with else clause 
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Error: Only even numbers are allowed")
else:
    reciprocal = 1 / num
    print("Reciprocal of ", num, " is ", reciprocal)

# Python try with finally clause
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print("Result: ", result)
except:
    print("Error: Division by zero")
finally:
    print("This is finally block")


# Python Custom Exceptions
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


# Python User-Defined Exception
class InvalidAgeExeption(Exception):
    "Raised whe in input value is less than 18"
    pass

# you need to guess this number
number = 18
try:
    i_num = int(input("Enter a number: "))
    if i_num < number:
        raise InvalidAgeExeption
    else:
        print("Congratulations! You guessed it correctly.")

except InvalidAgeExeption:
    print("This value is too small, try again!")  


# Customizing Exception Classes
class SalaryNotInRange(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"

salary = int(input("Enter salary: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRange(salary)

# Functions, builtin functions

# List, Tuple, Set,

# Dictionaries
