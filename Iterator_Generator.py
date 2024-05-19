# ================================================================================================================================
# 이터레이터(Iterator)
# __next__() 메서드를 사용하여 객체를 반환하는 __iter__() 메서드를 정의합니다.
# 클래스가 __next__() 메서드를 정의하면 __iter__()는 self를 반환할 수 있습니다.
# ================================================================================================================================
a = iter([1,2,3,4,5])
for item in range(5):
    print(next(a)) # next() 함수를 호출할 때마다 이터레이터 객체의 요소를 차례대로 반환

# for문을 이용하면 next()를 호출할 필요 없음(for문이 자동으로 호출)
a = iter([1,2,3,4,5])
for item in a:
    print(item)

# 이터레이터 만들기 예제1
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.start = 0
        pass
    
    def __iter__(self):
        return self
        pass
    
    def __next__(self):
        if self.start >= len(self.data):
            raise StopIteration
        rtn, self.start = self.data[self.start], self.start + 1
        return rtn

a = MyIterator(['오레오 쿠키 앤 크림', '에스프레소 앤 크림', '이상한 나라의 슈팅스타', '애플 민트'])
for item in a:
    print(item)

# 이터레이터 만들기 예제2
class SubIterator:
    def __init__(self, start, end, data):
        if(start > end):
            raise IndexError
        if(end - start > len(data)):
            raise RuntimeError
        self.start, self.end = start, end
        self.position = start
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if self.position >= self.end:
            raise StopIteration
        rtn = self.data[self.position]
        self.position += 1
        return rtn

a = SubIterator(5,10,list(range(20)))
for item in a:
    print(item)


# ================================================================================================================================
# 제너레이터(Generator)
# 제너레이터는 이터레이터를 생성하기 위한 간단하고 강력한 도구입니다.
# 제너레이터는 일반 함수처럼 작성되지만 데이터를 리턴할 때마다 return 대신 yield 키워드를 사용합니다.
# next()가 호출될 때마다 제너레이터는 중단된 부분 부터 다시 시작합니다.(모든 데이터 값과 마지막으로 실행된 문장을 기억함).
# ================================================================================================================================

# 제너레이터 만들기 예제1
def my_generator1():
    yield 10
    yield 20
    yield 30
    pass

g1 = my_generator1()
print(type(g1))   # <class 'generator'>

next(g1) # 10
next(g1) # 20
next(g1) # 30
next(g1) # StopIteration 예외 발생



# 제너레이터 만들기 예제2
def my_generator2(data):
    for idx in range(data.__len__()-1, -1, -1):
        yield data[idx]
        pass
    pass

for a in my_generator2(['라이트블루아쿠아', '마시멜로우피치', '마젠타레이디']):
    print(a)

# 🔴 제너레이터로 수행할 수 있는 모든 작업은 이전 섹션에서 설명한 대로 클래스 기반 이터레이터로 수행할 수도 있습니다.
# 제너레이터를 매두 컴팩트하게 만드는 이유는 __iter__()와 __next__() 메서드가 자동으로 생성된다는 것입니다.


# ================================================================================================================================
# 제너레이터 표현식
# 일부 간단한 제너레이터는 리스트 컴프리헨션과 유사한 구문을 사용하지만 대괄호 대신 괄호를 사용하여 표현식으로 간결하게 코딩할 수 있습니다.
# 이러한 표현식은 둘러싸는 함수에 의해 제너레이터가 즉시 사용되는 상황을 위해 설계되었습니다.
# 제너레이터 표현식은 완전한 제너레이터 정의보다 간결하지만, 융통성은 떨어지고, 비슷한 리스트 컴프리헨션보다 메모리를 덜 쓰는 경향이 있습니다.
# ================================================================================================================================

# 제너레이터 표현식 예제1
my_generator3 = (i*i for i in range(1,10))
for a in my_generator3:
    print(a)


# 제너레이터 표현식 예제2
my_generator4 = ((i, j, i+j) for i in range(1,5) for j in range(1,5))
for a, b, c in my_generator4:
    print(F'a={a}, b={b}, c={c}')
