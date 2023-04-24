# Class 
- group relevant data and methods in a single unit (e.g. Student/Book/Admin)
# Object
- we instantiate/create many objects from the class blueprint
###### Note:
- We studied built-in classes: int, float, list, str, tuple, dict, set
- We learned about (im)mutability, in-place changes and memory name-value binding
# Create an Object
#### Line 3: Class Employee
- It gathers together the related variables of the class
- We call them attributes
- Class = blueprints to create objects
#### Line 9
- Employee()
- Creates a variable of type Employee
- We call it object
#### Line 10+: 
- Using (.) operator: we can access the internal variables
```py

# This is a bit improper...wait with me
class Employee:
    name = None
    salary = None
    address = None

ragdha = Employee()
ragdha.name = 'ragdha'
ragdha.salary = 1000
ragdha.address = 'Lovely Canada'

print(ragdha.address)  # Lovely Canada

emp2 = Employee()
emp2.name = 'noura'
emp2.salary = 0
emp2.address = 'Same as her dad'

print(emp2.address)  # Same as his dad
emp2.address = 'BC'
print(emp2.address)  # BC
```
