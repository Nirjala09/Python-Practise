#Lambda is a small anonymous function used for short, simple functions in one line.
def myfunc(n):
      return lambda a : a * n    #lambda arguments : expression

mydoubler = myfunc(2)

print(mydoubler(11))