# ================================================================================================================================
# NumPy 객체는 동종의 다차원 배열이다. 그리고 이것은 요소(보통 숫자)의 테이블이다.
# 모두 같은 타입 음이 아닌 정수의 튜플에 의해 인덱싱고, NumPy에서는 차원을 axis(축)이라고 한다.

# 예를 들어 3차원 공간의 좌표 [1, 2, 1]은 하나의 축을 가진다. 그리고 그 축에는 3개의 요소가 있다.
# 그래서 우리는 길이가 3이라고 말한다. 아래의 예에서 배열에는 2개의 축이 있다.(첫 번째 축의 길이는 2이고 두 번째 축의 길이는 3이다.)
# [[1., 0., 0.],
#  [0., 1., 2.]]
#   
# NumPy의 배열 클래스는 ndarray라고 불린다. 별칭으로 array라고 알려져있지만 이것은 표준 파이썬 라이브러리 클래스 array.array와는 다른것이다.
# ▶▶▶ ndarray의 중요한 속성들 
# 1. ndarray.ndim     ▶ 배열의 축(차원) 수입니다.
# 2. ndarray.shape    ▶ 배열의 차원이다. 이것은 각 차원에 있는 배열의 크기를 나타내는 정수들의 튜플이다 
#    -> 예를 들어 n개의 행과 m개의 칼럼이 있는 2차원 배열에서 shape는 (n, m)이 된다. 따라서 shape튜플의 길이는 차원의 수이다.
# 3. ndarray.size     ▶ 배열의 총 요소 수입니다. 이것은 shape요소들의 곱과 같다
# 4. ndarray.dtype    ▶ 배열의 요소 타입을 설명하는 객체이다. 표준 파이썬 데이터 타입을 사용하여 dtype을 만들거나 지정할 수 있다.
#                     추가적으로 NumPy 자체 데이터 타입도 제공한다.(numpy.int32, numpy.int16, numpy.float64 등등 매우 많음...)
# 5. ndarray.itemsize ▶ 배열의 각 요소의 크기(Byte)입니다.
#    -> 예를 들어 float64 타입의 요소들을 가진 배열은 itemsize가 8(=64/8)이고, complex32 타입은 itemsize가 4(=32/8)이다
#    -> ndarray.itemsize 는 ndarray.dtype.itemsize와 동일하다.
# 6. ndarray.data     ▶ 실제 배열의 요소들을 포함하는 버퍼이다. 일반적으로 인덱싱 기능을 사용하여 배열의 요소에 엑세스하기 때문에 이 속성은 사용할 필요가 없음
# ================================================================================================================================

import numpy as np
import math as math


a = np.arange(15, dtype=np.int64).reshape(3, 5) # 키워드 인자 dtype으로 타입을 지정할 수 있다.
print(a)
print(a.shape)        # (3, 5)
print(a.ndim)         # 2
print(a.dtype)        # int64
print(a.dtype.name)   # int64
print(a.itemsize)     # 8
print(type(a))        # <class 'numpy.ndarray'>

# 배열을 만드는 방법들 중 몇개만 알아보자
a = np.array([1,2,3,4,5])
print(a)              # [1 2 3 4 5]
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)        # float64


a = np.array([(1.5, 2, 3), (4, 5, 6,)]) # 중첩 시퀀스(튜플이나 리스트)로 만들 수 있다
print(a)
# [[1.5 2.  3. ]
#  [4.  5.  6. ]]
c = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
print(c)
# [[1.+0.j 2.+0.j]
#  [3.+0.j 4.+0.j]
#  [5.+0.j 6.+0.j]]
print(c.shape)        # (3, 2)
print(c.ndim)         # 2


zero_array = np.zeros((2, 3, 4))
print(zero_array)
# [[[0. 0. 0. 0.]
#   [0. 0. 0. 0.]
#   [0. 0. 0. 0.]]

#  [[0. 0. 0. 0.]
#   [0. 0. 0. 0.]
#   [0. 0. 0. 0.]]]
print(zero_array.dtype) # float64   -> 기본적으로 float64 타입으로 만들지만 키워드 인자 dtype으로 원하는 타입을 지정할 수 있다.
print(zero_array.ndim)  # 3
print(zero_array.size)  # 24(=2 X 3 X 4)
one_array = np.ones((3, 4), dtype = np.complex64)
print(one_array)
# [[1.+0.j 1.+0.j 1.+0.j 1.+0.j]
#  [1.+0.j 1.+0.j 1.+0.j 1.+0.j]
#  [1.+0.j 1.+0.j 1.+0.j 1.+0.j]]

random_array = np.empty((2, 3)) # empty함수는 메모리 상태에 따라 요소값이 무작위인 배열을 만든다

# 숫자들의 시퀀스를 만들기 위해 표준 파이썬의 range() 함수와 유사하게 NumPy에서는 arange 함수를 제공한다.
print(np.arange(10, 30, 5))       # [10 15 20 25]
print(type(np.arange(10, 30, 5))) # <class 'numpy.ndarray'>

# arange함수가 부동소수점 타입의 파라미터와 같이 사용될 때 한정된 부동소수점 정밀도 때문에 일반적으로 얻은 요소의 수를 예측하는 것은 불가능하다
# 이러한 이유로 linspace 함수를 사용하는 것이 일반적으로 더 좋다 linspace 함수는 arange와 다르게 step 대신에 우리가 원하는 요소의 개수를 받는다

a = np.linspace(0, 2, 9)
print(a)  # [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]    <- 0부터 2까지의 9개의 숫자
x = np.linspace(0, 2 * np.pi, 100)
f = np.sin(x)
print(f)

# [ 0.00000000e+00  6.34239197e-02  1.26592454e-01  1.89251244e-01
#   2.51147987e-01  3.12033446e-01  3.71662456e-01  4.29794912e-01
#   4.86196736e-01  5.40640817e-01  5.92907929e-01  6.42787610e-01
#   6.90079011e-01  7.34591709e-01  7.76146464e-01  8.14575952e-01
#   8.49725430e-01  8.81453363e-01  9.09631995e-01  9.34147860e-01
#   9.54902241e-01  9.71811568e-01  9.84807753e-01  9.93838464e-01
#   9.98867339e-01  9.99874128e-01  9.96854776e-01  9.89821442e-01
#   9.78802446e-01  9.63842159e-01  9.45000819e-01  9.22354294e-01
#   8.95993774e-01  8.66025404e-01  8.32569855e-01  7.95761841e-01
#   7.55749574e-01  7.12694171e-01  6.66769001e-01  6.18158986e-01
#   5.67059864e-01  5.13677392e-01  4.58226522e-01  4.00930535e-01
#   3.42020143e-01  2.81732557e-01  2.20310533e-01  1.58001396e-01
#   9.50560433e-02  3.17279335e-02 -3.17279335e-02 -9.50560433e-02
#  -1.58001396e-01 -2.20310533e-01 -2.81732557e-01 -3.42020143e-01
#  -4.00930535e-01 -4.58226522e-01 -5.13677392e-01 -5.67059864e-01
#  -6.18158986e-01 -6.66769001e-01 -7.12694171e-01 -7.55749574e-01
#  -7.95761841e-01 -8.32569855e-01 -8.66025404e-01 -8.95993774e-01
#  -9.22354294e-01 -9.45000819e-01 -9.63842159e-01 -9.78802446e-01
#  -9.89821442e-01 -9.96854776e-01 -9.99874128e-01 -9.98867339e-01
#  -9.93838464e-01 -9.84807753e-01 -9.71811568e-01 -9.54902241e-01
#  -9.34147860e-01 -9.09631995e-01 -8.81453363e-01 -8.49725430e-01
#  -8.14575952e-01 -7.76146464e-01 -7.34591709e-01 -6.90079011e-01
#  -6.42787610e-01 -5.92907929e-01 -5.40640817e-01 -4.86196736e-01
#  -4.29794912e-01 -3.71662456e-01 -3.12033446e-01 -2.51147987e-01
#  -1.89251244e-01 -1.26592454e-01 -6.34239197e-02 -2.44929360e-16]


# ================================================================================================================================
# Printing Arrays
# 배열을 출력할 때 NumPy는 중첩 리스트와 유사한 방식으로 배열을 출력하지만, 다음과 같은 형식으로 출력한다
# 1. 마지막 차원(axis)는 왼쪽에서 오른쪽으로 출력된다
# 2. 마지막에서 두 번째 차원은 위에서 아래로 출력된다
# 3. 나머지 부분도 위에서 아래로 출력되고, 각 슬라이스는 빈 줄로 다음 슬라이스와 구분된다.
# ================================================================================================================================

a = np.arange(120).reshape(2,3,4,5)
print(a.ndim)        # 4
print(a)
# [[[[  0   1   2   3   4]
#    [  5   6   7   8   9]
#    [ 10  11  12  13  14]
#    [ 15  16  17  18  19]]

#   [[ 20  21  22  23  24]
#    [ 25  26  27  28  29]
#    [ 30  31  32  33  34]
#    [ 35  36  37  38  39]]

#   [[ 40  41  42  43  44]
#    [ 45  46  47  48  49]
#    [ 50  51  52  53  54]
#    [ 55  56  57  58  59]]]


#  [[[ 60  61  62  63  64]
#    [ 65  66  67  68  69]
#    [ 70  71  72  73  74]
#    [ 75  76  77  78  79]]

#   [[ 80  81  82  83  84]
#    [ 85  86  87  88  89]
#    [ 90  91  92  93  94]
#    [ 95  96  97  98  99]]

#   [[100 101 102 103 104]
#    [105 106 107 108 109]
#    [110 111 112 113 114]
#    [115 116 117 118 119]]]]

# ================================================================================================================================
# 기본적인 연산기능
# ================================================================================================================================

a = np.array(([10, 20, 30], [40, 50, 60]))
b = np.arange(1.5, 10, 1.5, dtype=np.float64).reshape(2, 3)
c = a + b
print(c)
# [[11.5 23.  34.5]
#  [46.  57.5 69. ]]

a = np.linspace(0, 2, 9)     # 0부터 2까지 9개
b = np.linspace(0, 5, 9)     # 0부터 5까지 9개
a = np.sin(a).reshape(3, 3)
b = np.cos(b).reshape(3, 3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a @ b)                 # matrix product (행렬 곱) <- a.dot(b)와 같음

# [[ 1.          1.05836708  0.7947479 ]
#  [ 0.38210525  0.04032737 -0.05087773]
#  [ 0.17693563  0.65296154  1.19295961]]
# [[-1.         -0.56355916  0.16410318]
#  [ 0.98117227  1.6426146   1.94884696]
#  [ 1.81805434  1.31501035  0.62563524]]
# [[ 0.          0.20063549  0.15117359]
#  [-0.20417365 -0.67413911 -0.94885399]
#  [-0.81850385 -0.32572336  0.2579333 ]]
# [[ 0.          0.30507424  1.52042987]
#  [-2.27566782 -1.05033725 -0.94911527]
#  [-1.21562807 -2.97254802  3.20556448]]
# [[-0.46750289 -0.35690766 -0.11137501]
#  [-0.3491082  -0.43549228 -0.35722816]
#  [-0.04337429 -0.28038205 -0.41138473]]

a = np.arange(10, 61, 10).reshape(2, 3)
b = np.arange(2, 13, 2, dtype=float).reshape(2, 3)
a +=3
print(a)
# [[13 23 33]
#  [43 53 63]]
b /= 10
print(b)
# [[0.2 0.4 0.6]
#  [0.8 1.  1.2]]
# ================================================================================================================================
# 서로 다른 타입의 배열을 연산하면 결과 배열의 타입은 더 일반적이거나 정확한 타입이다(업캐스팅으로 알려진 동작)
# 배열에 있는 모든 요소의 합을 계산하는 것과 같은 많은 단항연산들은 ndarray 클래스에 구현되어 있다.
# ================================================================================================================================
a = np.ones(3, dtype=np.int64)
b = np.linspace(0, math.pi, 3)
c = a + b
print(c)  # [1.         2.57079633 4.14159265]
print(c.dtype.name) # float64

d = np.exp((c * 10J))   # 입력 배열에 있는 모든 요소의 지수를 계산
print(d)  # [-0.83907153-0.54402111j  0.83907153+0.54402111j -0.83907153-0.54402111j]
print(d.dtype.name) # complex128

print(F"d.sum() => {d.sum()}, d.min() => {d.min()}, d.max() => {d.max()}")
# d.sum() => (-0.8390715290764528-0.5440211108893692j), d.min() => (-0.8390715290764531-0.5440211108893688j), d.max() => (0.8390715290764528+0.5440211108893693j)


# ================================================================================================================================
# NumPy는 sin, cos, exp와 같은 친숙한 수학 함수를 제공한다. 이 함수들은 "Universal Functions"(ufunc) 라고 불린다.
# 이러한 Universal Functions들은 배열에서 각 요소별로 계산을 하고 계산 결과를 새로운 배열에 담아 리턴한다
# ================================================================================================================================



