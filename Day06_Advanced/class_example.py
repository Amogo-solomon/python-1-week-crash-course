class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
      print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

      ent1.age = 21
      print(ent1.age)

ent1 = Student("Alice", 20)
ent1.greet()