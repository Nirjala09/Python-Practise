#Comprehension is a shortcut in Python to create lists or dictionaries in one line.
""" syntax for list comprehension [expression for item in iterable if condition]
"""
squares = [x * x for x in range(5)]
print(squares)



# dict comprehension
squares = {x: x * x for x in range(5)}
print(squares)
