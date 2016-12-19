class Bike(object):
    def __init__(self, price, speed, miles):
        self.price= price
        self.speed= speed
        self.miles= miles
    def displayInfo(self):
        print "Bike Price: $", self.price
        print "Bike speed:", self.speed,"mph"
        print "Miles on the bike:", self.miles
        return self
    def ride(self):
        # for x in range(0, 3):
            print "Riding"
            self.miles+=10
            print self.miles
            return self
    def reverse(self):
        # for x in range(0, 1):
            if self.miles>=0:
                print "Backing UP!"
                self.miles-=5
                print self.miles
            else:
                self.miles=0
                print self.miles
            return self


new = Bike(100, 20, 0)
new.ride().ride().ride().reverse().displayInfo()
