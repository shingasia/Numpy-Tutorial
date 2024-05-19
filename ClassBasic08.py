
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

b = Computer()
b.cpu = 'Intel i7 13th'
b.ram = '32GB'
b.disk = '2TB'
b.power = True

a.toString()       # Intel i9 10th 16GB 2TB False
b.toString()       # Intel i7 13th 32GB 2TB True

def powerOnOff(obj):
    if(obj.power):
        obj.power=False
        print('PC의 전원을 껐습니다.')
    else:
        obj.power=True
        print('PC의 전원을 켰습니다.')

a.powerOnOff = powerOnOff
b.powerOnOff = powerOnOff
a.powerOnOff(a)
b.powerOnOff(b)


print(a.__init__, b.__init__)
# <method-wrapper '__init__' of Computer object at 0x00000170AF08D690> <method-wrapper '__init__' of Computer object at 0x00000170AF08E990>
print(a.__class__, b.__class__) # a와 b 둘 다 <class '__main__.Computer'>
del Computer, a, b, powerOnOff


# ================================================================================================================================
# 클래스 메서드(Class Method)
# @classmethod 데코레이터를 붙이고 첫번째 인수로 클래스에 해당하는 cls인수를 받는다.
# ================================================================================================================================
class BookRentalService:
    retain_count = 50000 # 보유중인 도서
    lend_count = 0       # 빌려간 도서
    
    def __init__(self):
        pass
    
    @classmethod
    def print_count(cls):
        print(F'{cls.lend_count}개의 도서를 빌려갔습니다. {cls.retain_count}개 남았습니다.')
        pass
    
    def borrow_book(self, count):
        BookRentalService.lend_count += count
        BookRentalService.retain_count -= count
        print(F'{count}개의 책을 빌려갔습니다.')
    
    def return_book(self, count):
        BookRentalService.lend_count -= count
        BookRentalService.retain_count += count
        print(F'{count}개의 책을 반납했습니다.')


obj1 = BookRentalService()
BookRentalService.print_count() # 클래스이름.클래스메서드() 또는 객체.클래스메서드() 를 통해 호출할 수 있다.

obj1.borrow_book(10)
BookRentalService.print_count() # 10개의 도서를 빌려갔습니다. 49990개 남았습니다.

obj1.return_book(3)
BookRentalService.print_count() # 7개의 도서를 빌려갔습니다. 49993개 남았습니다.

obj2 = BookRentalService()
obj1.borrow_book(20)
BookRentalService.print_count() # 27개의 도서를 빌려갔습니다. 49973개 남았습니다.



# ================================================================================================================================
# 정적 메서드 (Static Method)
# 특정 객체에 소속되지도 않고, 클래스와 관련된 동작을 하는 것도 아니어서 따로 self 또는 cls와 같은 인수를 받지 않는다.
# 정의할 때 @staticmethod 데코레이터를 붙여주면 된다.
# ================================================================================================================================

class Library:
    @staticmethod
    def intro(name):
        print(F'안녕하세요 {name}에 오신것을 환영합니다.')
    


Library.intro('떡잎마을 어린이도서관')   # 클래스이름.스태틱메서드()
Library().intro('떡잎마을 어린이도서관') # 객체.스태틱메서드()

