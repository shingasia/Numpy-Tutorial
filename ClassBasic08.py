# @classmethod, @staticmethod, @abstractmethod 등등 알아보기

class Computer:
    def toString(self):
        print(F'{self.cpu} {self.ram} {self.disk} {self.power}')
        pass
    pass

a = Computer()

a.cpu='Intel i9 10th'
a.ram='16GB'
a.disk='2TB'
a.power=False


a.toString()       # Intel i9 10th 16GB 2TB False

def powerOnOff(obj):
    if(obj.power):
        obj.power=False
    else:
        obj.power=True

a.powerOnOff = powerOnOff
a.powerOnOff(a)

a.toString()       # Intel i9 10th 16GB 2TB True
print(a.__init__)  # <method-wrapper '__init__' of Computer object at 0x01659148>
print(a.__class__) # <class '__main__.Computer'>

