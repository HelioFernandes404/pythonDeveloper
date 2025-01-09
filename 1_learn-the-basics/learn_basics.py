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



# Exceptions

# Functions, builtin functions

# List, Tuple, Set,

# Dictionaries
