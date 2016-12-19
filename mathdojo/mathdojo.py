class MathDojo(object):
    def __init__(self):
        # self.arg1 = arg1
        # self.y = y
        self.result = 0
    def add(self, *restarg):
        # self.result += arg
        for x in restarg:
            if type(x) is list:
                for y in x:
                    self.result += y
            elif type(x) is int:
                        self.result += x
            if type(x) is tuple:
                for y in x:
                    self.result += y
        return self
    def subtract(self, arg, *restarg):
        # self.result -= arg
        for x in restarg:
            if type(x) is list:
                for y in x:
                    self.result -= y
            elif type(x) is int:
                        self.result -= x
            if type(x) is tuple:
                for y in x:
                    self.result -= y
        return self
md = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
print md
