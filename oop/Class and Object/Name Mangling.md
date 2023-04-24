# Name Mangling
- Prefixing specific attributes with _classname
- If they have :
    - at least 2 leading (before) underscores __
    - and at most 1 trailing (after) _
- Examples, for a book class:
   - __var ⇒ _book__var
   - __var_ ⇒ _book__var_ 
- So by default, the user can't access them
- unless the coder wanna really use them ⇒ then use the mangled name
## With functions

```py

class Book:
    def __init__(self):
        pass
    def __f1(self):
        print('__f1')
    def __f2_(self):
        print('__f2_')
    def _f3(self):
        print('_f3')

book = Book()
#book.__f1()   # AttributeError
#book.__f2_()  # AttributeError
book._f3()     # _f3

print(dir(book))    # return the names in the current scope
# ['_Book__f1', '_Book__f2_', '__class__', ... , '_f3']

```
## Visible from inside
 ```py
 
class Book:
    def __init__(self):
        self.__att4 = 4  # _Book__att4

    def hello(self):
        print(self.__att4)  # visible from INSIDE!
        print(self._Book__att4)  # visible from inside!


if __name__ == '__main__':
    book = Book()
    # print(book.__att4)          # NOT visible from OUTSIDE
    print(book._Book__att4)  # we still can access indirectly
    book.hello()

 ```
