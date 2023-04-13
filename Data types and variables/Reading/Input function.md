# Input function
- Similar to the print function
- It always reads the input as a string
- there are 2 ways
    - input() which reads directly
    - input(msg) which prints a message first
  
- Input() function reads a complete line, and return as string
    - Let’s say you want to read 2 numbers
    - Then don’t enter both of them on the same line
    - Use 2 input() and input twice (2 lines)
    - a = input()
    - b = input()
### Another way:
- Let’s read 3 strings:
    - a, b, c = input().split()
    - Then: a, b, c are 3 strings
- Let’s read 4 integers:
    - a, b, c, d = map(int, input().split())
    - But you must enter really 4 integers
- Let’s read 5 floats
    - a, b, c, d, e = map(float, input('Enter 5 numbers: ').split())
