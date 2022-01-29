try:
    raise Exception('Not Found', 404)
except Exception as inst:
    print(type(inst)) # <class 'Exception'>
    print(inst.args)  # ('Not Found', 404)
    print(inst)       # ('Not Found', 404)
    
    (data1, data2) = inst.args
    x, y = inst.args
    print(F"x = {x}, y = {y}, data1 = {data1}, data2 = {data2}") # x = Not Found, y = 404, data1 = Not Found, data2 = 404
    pass


# except 절에서 예외 이름 뒤에 arguments를 지정할 수 있고 예외 객체의 args에 저장된다.


# ▶▶▶ raise 문은 프로그래머가 지정한 예외가 발생하도록 강제할 때 사용한다.
# raise 문에서 사용하는 단일 인자는 발생시킬 예외를 가리킨다. (예외 인스턴스이거나 예외 클래스(Exception을 상속받은 클래스))
# 예외 클래스가 전달되면, 묵시적으로 인자 없이 생성자를 호출해서 인스턴스를 만든다.
# raise ValueError    -> raise ValueError()의 축약형

try:
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise   # 이렇게 어떤 예외가 발생하였는지 알고싶지만 처리하고 싶지 않다면 raise문으로 다시 그 예외를 발생시킬 수 있다.
except NameError:
    print('다시발생한 예외 처리됨...')
    









# < 예외 연쇄 (Chaning Exceptions) >
# raise 문에서 선택적으로 from 을 같이 사용해서 chaning exceptions를 할 수 있다.
# [ raise RuntimeError from exc ] 여기서 exc는 예외 객체 또는 None이다.

def func():
    raise ConnectionError

try:
    func()
    
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

"""
Traceback (most recent call last):
  File "c:/Users/mypc/VSCODE-WORKS/PythonCode/Learn-Python/ExceptionControl2.py", line 38, in <module>
    func()
  File "c:/Users/mypc/VSCODE-WORKS/PythonCode/Learn-Python/ExceptionControl2.py", line 35, in func
    raise ConnectionError
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:/Users/mypc/VSCODE-WORKS/PythonCode/Learn-Python/ExceptionControl2.py", line 41, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
"""


# ================================================================================================================================
# < finally로 마무리 >
# finally 문은 try 문이 예외를 생성하는지와 관계없이 try 문이 완료되기 전에 무조건 실행된다. 
# finally 문의 더 복잡한 경우는 다음과 같은 상황이 있을 수 있다.
# 1. try 문을 실행하는 동안 예외가 발생하면, except 문에서 예외를 처리할 수 있다. 예외가 except 문에서 처리되지 않으면, finally 문이 실행된 후 예외가 다시 발생한다.
# 2. except 나 else 문 실행 중에 예외가 발생할 수도 있다. 다시 finally 문이 실행된 후 예외가 다시 발생한다.
# 3. 만약 finally 문에 break, continue 또는 return 이 포함되면, 예외는 다시 발생하지 않는다. -> not re-raise
# 4. try 문이 break, continue 또는 return 문에 도달하면, finally 문은 break, continue, return 문 실행 직전에 실행된다 (왜냐하면 무조건 실행되기 때문..)
# 5. finally 문에 return 문이 포함되면, 반환 값은 try절의 return 문이 주는 값이 아니라, finally 절의 return 문이 주는 값이 된다.
# ================================================================================================================================

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return()) # False

# ================================================================================================================================
# 전체적인 try문은 다음과 같이 생겨먹었다.
# try:
#     statements...
# (except [expression as identifier]]:) +
# 
# else:
#     statements...
# finally:
#     statements...
# ================================================================================================================================