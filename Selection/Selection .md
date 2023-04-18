# If statement
```py
"""
Write a program that reads an integer salary
○ Then If salary < 1000,
■ print you are poor
○ Otherwise do nothing
○ End program with printing Work Hard
"""
salary = int(input())

if salary < 1000:
    print('You are poor')

print('Work hard')
```
### Variable scope
- The part of a program where a variable is accessible.
### Common coding mistakes
- Forget the : in end of the if statement
- Multiple lines per a block with different indentation 
- Variables are accessed after the if-condition, but never assigned

### What if I need more conditions?
```py
"""
Write a program that reads an integer salary then:
● If salary < 1000,
○ print you are poor
● elif salary >= 1000 and < 20000,
○ print good salary
● elif salary >= 20000,
○ print you are rich
"""
salary = int(input())

if salary < 1000:
    print("You are poor")
elif 1000 <= salary < 20000:
    print("good salary")
elif salary >= 20000:
    print("you are rich")
```
#### Summary:
![Screenshot 2023-04-18 at 02-35-44 03 Selection 2 pdf](https://user-images.githubusercontent.com/76912120/232639408-b444aca0-8726-471a-8ba5-c3870d70e1ce.png)

