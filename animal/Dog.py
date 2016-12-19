from animal import Animal
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
        print "I am DOG!"
    def pet(self):
        self.health += 5
        return self

puppy = Dog("PORK!")
puppy.walk().walk().walk().run().run().pet().displayHealth()
