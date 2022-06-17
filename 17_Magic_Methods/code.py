class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #def __str__(self):
    #    return(f"person {self.name}, {self.age} years old")

    
    def __repr__(self):
        return(f"<person {self.name}, {self.age} years old>")


bob = Person("Bob", 23)

print(bob)