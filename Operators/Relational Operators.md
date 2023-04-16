# Relational Operators
- Boolean data type
```py
status = True
print(status)     # True
# not flips true to false and false to true
print(not status) # False

print(bool('0'))  # True
print(bool('1'))  # True
print(bool(''))   # False

print(bool(5))     # True
print(bool(-5))    # True
print(bool(5.5))   # True
print(bool(0))     # False

# bool():
# False for empty string and zero
# True otherwise
```
- Comparing strings
```py
# Based on English Dictionary
# Letter by letter comparison

# If a word has a smaller letter: it appears first
print('love' < 'zebra') # True  l is before z
print('love' < 'long')  # False: lo are common, but v > n
print('love' != 'long') # True

# If one word is done in comparison: the smaller in length comes first
print('counter' < 'counterattack')  # True

# Upper letters are smaller than small letters
print('A' < 'a')            # True
print('A' < 'z')            # True
print('Z' < 'a')            # True
print('loVE' < 'love')      # True V < v
print('loVE' < 'long')      # True V < n

print('' < 'A')             # True empty is smaller

print(' ' < 'A')            # True: space smaller than letters
print(' ' < 'a')            # True: space smaller than letters

print('0' < 'A')            # True: Digits smaller than letters
print('0' < 'a')            # True: Digits smaller than letters


```
- Comparing Floating point
```py


a = 3 / 7
b = 0.1 + 3/7 - 0.1

print(a)        # 0.42857142857142855
print(b)        # 0.4285714285714286
print(a == b)   # False

x = 5.0
y = 4.9999999999999999999999999999999999999
print(x == y)   # True: y is approximated to 5
```
