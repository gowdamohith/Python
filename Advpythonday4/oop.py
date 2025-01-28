class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.marks = 0

    def set_marks(self,marks):
        self.marks = marks

S1 = Student("abc" , 23)
print(S1.name, S1.age, S1.marks)

class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    
    def update_model(self, new_model):
        self.model = new_model


my_car = Car("Toyota", "Corolla", 2020)


print(my_car.make)  
print(my_car.model)  
print(my_car.year)  


my_car.display_info() 


my_car.update_model("Camry")
my_car.display_info() 


class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")


person1 = Person("Alice", 30, "New York")


print(person1.name)  
print(person1.age)  
print(person1.city)  


person1.display_info()  


person1.age = 31
print(person1.age)  


person1.display_info()  