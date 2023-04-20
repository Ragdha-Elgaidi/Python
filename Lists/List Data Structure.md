# List
- It is an ordered sequence of items
- They can be of different types!
- It is a mutable class
- -It is iterable
- It can have different data types!

### Creating a list
- We use brackets [] to create a list
- Between []: put your items, comma separated
- It is iterable!

```py
my_list = [1, 2, 3, 4]

print(len(my_list))
print(1 in my_list)
print(7 in my_list)

for item in my_list:
    print(item, end=" ")

print()

print(my_list)

my_list = [1, "Ragdha", 3]

# IndexError: list assignment index out of range
#my_list[3] = 0
```
### Indexing
```py
numbers = [1, 2, 3, 4]

numbers[0] = 7
numbers[3] *= 2
numbers[2] -= 4

for index in range(4):
    print(numbers[index], end=" ") #7 2 -1 8 

print()
```

