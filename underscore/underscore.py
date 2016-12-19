class Underscore(object):
    def map(self, callback):
        return callback(2)
    def reduce(self):
        return callback(z)
    def find(self):
        return callback(z)
    def filter(self):
        return callback(z)
    def reject(self):
        return callback(z)
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore()
print _.map([1, 2, 3, 4, 5, 6], lambda x: x * 3) # yes we are setting our instance to a variable that is an underscore
print _.reduce([1, 2, 3, 4, 5, 6], lambda x: x += x)
print _.find([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0)
print _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 3 != 0)
# should return [2, 4, 6] after you finish implementing the code above
