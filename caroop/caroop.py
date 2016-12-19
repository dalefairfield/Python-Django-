class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price : $", str(self.price)
        print "Speed :", str(self.speed), "mph"
        print "Fuel : ", self.fuel
        print "Mileage : ", str(self.mileage), "mpg"
        print "Sales Tax : " , str(self.tax)
Auto1 = Car(2000, 35, "Full", 15)
Auto2 = Car(2000, 5, "Not Full", 105)
Auto3 = Car(2000, 15, "Kind of Full", 95)
Auto4 = Car(2000, 25, "Full", 25)
Auto5 = Car(2000, 45, "Empty", 25)
Auto6 = Car(20000000, 35, "Empty", 15)
