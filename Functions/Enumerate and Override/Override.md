# Override!
- Using a previously used name (of a function or a variable), override the old one
```py
def sum(a, b):
    return a + b

print(sum(2, 3))    #5

# now we override previous one. You can't call
def sum(a, b, c):
    return a + b + c

# TypeError: sum() missing 1 required positional argument: 'c'
#print(sum(2, 3))    #5

print(sum(2, 3, 5))    #10

# be careful with functions with the same name

print(len('ragdha'))   #6

len = 1     # now len binds to something else
# TypeError: 'int' object is not callable
```
