from animal import Animal
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
        print "I am Dragoooooon!"
    def fly(self):
        self.health -= 10
        return self

fledgling = Dragon("Chicken!")
fledgling.walk().walk().walk().run().run().fly().fly().displayHealth()
