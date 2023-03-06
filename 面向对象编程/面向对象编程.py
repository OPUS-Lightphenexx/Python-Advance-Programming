class testclass:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def str(self):
        return self.num+self.den

    def __str__(self):
        return str(self.num)

    def show(self):
        print(self.num, '?', self.den)

    def addone(self,newone):
        return self.num+newone

    def add(self,otherfraction):
        newnum = self.num*otherfraction.den+self.den*otherfraction.num

        newden = self.den*otherfraction.num

        return testclass(newnum,newden)


test1 = testclass(3,5)
test2 = testclass(4,5)
print(testclass.add(test1,test2))
print(test1.show())




