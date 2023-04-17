# Logical Operators with values
What if the expression has values not booleans?
  - In terms of is True/False semantically, same But it is useful to understand it
  - Rule: The false value comes either from 0 or None or empty data structure Empty string (‘’) and later empty list [] or empty tuple () or empty map {}
##### Note
  - Observe: negative values are not False
# Values
- Remember the shortcut
 - Or:
   - True expression: Return first one that evaluates True
   - False expression: Return last expression that evaluates False
 - And: Opposite logic
   - True: return last True
   - False: return first False
 - In complex expressions, better avoiding depending on returned value
      - Just T or F
```py

x = -5
if x:
    print(x, 'is considered True')  # printed

x = ''
if not x:
    print(x, 'is considered False')  # printed

print(5 or 7)               # 5
print(0 or 7)               # 7
print(0 and 7)              # 0

print(5 and 7 and 10)       # 10
print(5 or 7 or 10)         # 5
print(0 or 5 or 7 or 10)    # 5

print('' or 0)              # 0
print(0 or '')              # Empty str ''
```
# bool function
  - What if I want to get True or False from expression of values
  - print(bool(3 or 5)) ⇒ True
  - print(bool(3 and '')) ⇒ False
