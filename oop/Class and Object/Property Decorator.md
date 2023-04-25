# A property decorator
- It is a way of defining properties in a class without manually calling the built-in function property(). 
- A property is an attribute that can be accessed or modified by using getters and setters methods.
- A property decorator makes a method act like a getter, and also allows us to define setter and deleter methods for the same property.


```py
class Time:
  def __init__(self, hours=0, minutes=0, seconds=0):
    self.total_seconds = hours * 3600 + minutes * 60 + seconds

  @property
  def hours(self):
    return self.total_seconds // 3600

  @hours.setter
  def hours(self, value):
    self.total_seconds = value * 3600 + self.minutes * 60 + self.seconds

  @property
  def minutes(self):
    return (self.total_seconds % 3600) // 60

  @minutes.setter
  def minutes(self, value):
    self.total_seconds = self.hours * 3600 + value * 60 + self.seconds

  @property
  def seconds(self):
    return self.total_seconds % 60

  @seconds.setter
  def seconds(self, value):
    self.total_seconds = self.hours * 3600 + self.minutes * 60 + value

t = Time(5, 12, 37) # old constructor works
print(t.hours) # prints 5
t.minutes = 30 # modifies the minutes attribute
print(t.total_seconds) # prints 18637
```

