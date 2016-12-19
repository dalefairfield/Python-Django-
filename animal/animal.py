class Animal(object):
    def __init__(self, name):
        print "ROAR...maybe... IM A NEW ANIMAL"
        self.name = name
        self.health = 100
    def walk(self):
        print "These hooves...maybe...are made for walking"
        self.health-=1
        return self
    def run(self):
        print "RUN IT! RUN IT!"
        self.health-=5
        return self
    def displayHealth(self):
        print "I am a ", self.name
        print "Health remaining : ", self.health
        return self


# new = Animal("animal")
# new.walk().walk().walk().run().run().displayHealth()
