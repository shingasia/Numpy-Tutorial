import numpy as np


# <비트 연산> ====================================================================================================================

# ================================================================================================================================
# logical_and
# bitwise_or
# bitwise_xor
# binary_repr
# 위 함수들은 입력한 숫자의 이진 문자열 형태를 리턴한다(아래의 예시에서 학습하자)
# ================================================================================================================================

# AND 연산
# ▶▶▶ numpy.bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) -> 이름만 봐도 AND 연산인걸 알 수 있다.
# -> x1, x2는 정수 또는 boolean 값만 되고, 당연히 x1.shape 와 x2.shape 가 다르다면 공통 모양으로 브로드캐스트 할 수 있는 형태만 가능하다
# -> x1, x2 둘 다 스칼라 값이면, 결과 또한 스칼라 값이다.

print(np.bitwise_and(13, 17)) # 1
# -> 13은 00001101로 표현되고, 마찬가지로 17은 00010001로 표현된다 따라서 13과 17의 AND 연산은 000000001 또는 1이다.
print(np.binary_repr(12))     # '1100'
print(np.bitwise_and([14, 3], 13)) # [12, 1]
x1 = np.array([2, 5, 255])
x2 = np.array([3, 14, 16])
print(np.bitwise_and(x1, x2)) # [ 2  4 16]

x1 = np.array([(True, True, False), (True, True, False)])
x2 = np.array([(False, True, True)])

print(np.bitwise_and(x1, x2)) # np.bitwise_and(x2, x1) 도 가능
# [[False  True False]
#  [False  True False]]

x1 = np.arange(2 * 4).reshape(2, 4)
x2 = np.array((2, 2, 2, 2))
print(x1 & x2)    # 이렇게 연산자(&)도 가능
# [[0 0 2 2]
#  [0 0 2 2]]

# OR 연산
# ▶▶▶ numpy.bitwise_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
print(np.bitwise_or(13, 16)) # 29
x1 = np.array([2, 5, 255, 2147483647], dtype=np.int32)
x2 = np.array([4, 4, 4, 2147483647], dtype=np.int32)
print(np.bitwise_or(x1, x2).__repr__())
# array([         6,          5,        255, 2147483647], dtype=int32)

x1 = np.array([2, 5, 255])
x2 = np.array([4, 4, 4])
print(x1 | x2) # [  6   5 255] 

# XOR 연산
# ▶▶▶ numpy.bitwise_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])


x1 = np.array([(True, True, False, True), (True, True, True, True)])
x2 = np.array([(False, True, True, True)])

print(np.bitwise_xor(x1, x2)) # == x1 ^ x2
# [[ True False  True False]
#  [ True False False False]]


# NOT 연산
# ▶▶▶ numpy.invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
print(np.bitwise_not is np.invert) # True
x1 = np.invert(np.array(13, dtype=np.uint16))
print(np.binary_repr(x1, width=16)) # 1111111111110010

x1 = np.invert(np.array(13, dtype=np.int8))
print(x1)  # -14
print(np.binary_repr(x1, width=8))  # 11110010

x1 = np.array((True, False, True, False))
print(~x1) # [False  True False  True]






