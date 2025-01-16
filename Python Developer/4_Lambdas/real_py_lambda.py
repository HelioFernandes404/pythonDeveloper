# How to Use Python Lambda Functions


# Lambda Calculus
# History
# First Example
def identity(x):
    return x


## In contrast, the lambda equivalent is:
identity = lambda x: x
# Output: x

# slightly more elaborate example
lambda x: x + 1
(lambda x: x + 1)(2)
# Output: 3

# Reduction
(lambda x: x + 1)(2)  # Evaluates to 3
# Step-by-step reduction:
# (lambda x: x + 1)(2)
# = (2 + 1)
# = 3

# Rename lambda
add_one = lambda x: x + 1
add_one(2)  # Output: 3


# Multiple Arguments
full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
print(full_name("guido", "van rossum"))  # Output: Full name: Guido Van Rossum

# Anonymous Functions
_(1, 2)  # type: ignore
# Output: 3

# iffy in Python
(lambda x, y: x + y)(2, 3)  # Output: 5

# Higher-Order Functions lambda
high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)  # Output: 6
high_ord_func(2, lambda x: x + 3)  # Output: 7

# Python Lambda and Regular Functions
# https://realpython.com/python-lambda/#python-lambda-and-regular-functions TODO: continue from here

# Functions
# Traceback
# Syntax
# Arguments
# Decorators
# Closure
# Evaluation Time
# Testing Lambdas
# Lambda Expression Abuses
# Raising an Exception
# Cryptic Style
# Python Classes
# Appropriate Uses of Lambda Expressions
# Classic Functional Constructs
# Key Functions
# UI Frameworks
# Python Interpreter
# timeit
# Monkey Patching
# Alternatives to Lambdas
# Map
# Filter
# Reduce
# Are Lambdas Pythonic or Not?
# Conclusion
