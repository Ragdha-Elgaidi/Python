# Namespaces
#### In a Python program, there are four types of namespaces:
- Built-In (e.g. len, int, max, sum, TypeError, etc)
- Global: contains any names defined at the level of the main program
- Enclosing: Later
- Local: local to the function and remains in existence until the function terminates.
#### Using a variable in a function: Python search order?
- Is it local? Then it is a local variable in a local namespace
- Is it enclosing? Then it enclosing namespace
- Is it global? Then it global namespace
- Is it in Built-In? Then it Built-In namespace
- None? Error
