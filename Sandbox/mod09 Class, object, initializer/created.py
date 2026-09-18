class Dog:
    created =  0
    def __init__(self, name, birth_year, sound="woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created += 1
    def bark(self,times):
        for i in range(times):
            print(self.sound)
        return
    
dog1 = Dog("Jallu", 2001)
dog2 = Dog("Mini", 2009, "arf arf")
dog3 = Dog("Aava", 2014, "bark bark")

print(f"Total dogs created {Dog.created}")