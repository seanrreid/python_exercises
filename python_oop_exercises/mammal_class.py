class Mammal:
    def __init__(self, name, type_of_mammal, breed, legs):
        self.name = name
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "%s is eating" % (self.name)

class Cat(Mammal):
    def __init__(self, name, type_of_mammal, breed, legs, fur):
        super().__init__(name, type_of_mammal, breed, legs)
        self.fur = fur

    def __str__(self):
        return "%s is a %s %s breed with %d legs and %s fur" % (self.name, self.type_of_mammal, self.breed, self.legs, self.fur)

    def purr(self):
        return "%s is purring" % (self.name)

    def eat(self):
        return "THE CAT EATS DIFFERENTLY FOR REASONS!!!"

guster = Cat("Gus", "cat", "mixed", 4, "short hair")
harry = Mammal("Harry", "dog", "bischon frize", 4)
#print(guster)
print(guster.eat())
#print(guster.purr())
print(harry.eat())