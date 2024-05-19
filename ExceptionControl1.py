while True:
    try:
        x=int(input('숫자를 입력  <<< '))
        break
    
    except ValueError:
        print("타입에 하자가 있어서 다시 하세요")

    
# ================================================================================================================================
# < try 문의 실행 규칙 >
# 1. 먼저 try 절 (try와 except 사이의 문장들)이 실행된다.
# 2. 예외가 발생하지 않으면, except 절을 건너뜀,
# 3. 만약 try 절을 실행하는 동안 예외가 발생하면, 나머지 절은 건너뛴다. 이때, except 키워드 뒤에 이름지어진 예외와 타입이 일치하면 except 절이 실행되고 try/except 블록을 빠져나간다.
# 4. 만약 매칭되는 예외가 발생하지 않으면, 무시하고 try 절 밖으로 빠져나고 예외는 핸들링되지 않는다.
# try 문은 서로 다른 예외들을 명시하기 위해 하나 또는 그 이상의 except 절을 가질 수 있고, 적어도 하나의 핸들러가 실행되면 try문을 빠져나간다.
# 당연한 소리지만 핸들러들은 오직 동일한 try 문 안에서 발생하는 예외들만 다룬다. 같은 try 문에 있지 않으면 의미없음.
# except문은 여러개의 예외를 처리하기 위해 튜플로 다음과 같이 지명할 수도 있다.
# except (RuntimeError, TypeError, NameError):
#     pass
# ================================================================================================================================


# except 문에 있는 클래스는 같은 클래스의 예외 또는 except 문에 지정한 클래스를 기본 클래스(base class)로 가지는 예외와 호환된다. (그러나 그 반대는 아님)
# 예를 들어 다음 코드는 B, C, D를 순서대로 출력할거다.

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:  # B, C, D를 순서대로 출력한다.
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')

for cls in [B, C, D]: # B, B, B  <- B만 3번 출력
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
# ================================================================================================================================
# ▶ 모든 예외들은 BaseException 클래스를 상속되므로 와일드카드로 사용할 수 있다. 그런데 이 방법은 실제 프로그래밍 오류를 가릴 수 있으므로
# 주의해서 사용해야 한다. BaseException으로 오류 메세지를 출력해서 볼 수 있고, 또 다른 예외를 다시 일으켜서(re-raise) 호출자가 예외를 쉽게 처리하도록 할 수도 있다.
# 선택적으로 마지막 except 문에서 예외이름을 생략할 수 있다. 그러나 예외 값은 sys.exc_info()[1]에서 검색되어야 한다.
# try-except 문에서 선택적으로 else 절을 넣을 수 있다. (단 else절은 모든 except 보다 뒤에 나와야 한다.) else 절은 try 문이 예외를 발생시키지 않는 경우 반드시 실행되어야 하는 코드에 유용하다.
# ================================================================================================================================
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    
except OSError as err:
    print("OS Error: {0}".format(err))     # OS Error: [Errno 2] No such file or directory: 'myfile.txt'

except ValueError:
    print("Could not convert data to an integer")

except BaseException as err:
    print(F"Unexpected {err =}, {type(err)=}")
    raise

print(sys.exc_info())




try:
    a = {'key1':'value1','key2':'value2'}
    a.pop('key3')
    print(repr(a))
    pass
except (ImportError, ModuleNotFoundError, \
        SyntaxError, IndentationError, \
        TypeError, ValueError, \
        ZeroDivisionError, IndexError, KeyError) as e1:
    print('무언가 오류 발생'+str(e1))
    pass
except BaseException as e1:
    print(e1)
    pass
else:
    print('오류가 없을 경우에만 수행됩니다.')


