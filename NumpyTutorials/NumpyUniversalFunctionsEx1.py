import numpy as np
# ================================================================================================================================
# Universal Functions의 Optional Keyword arguments (선택적으로 쓸 수 있는 키워드 인자)
# out, where, axes, axis, dtype, order 등등 자세한 설명은 구글의 있는 문서를 읽어보든 예제로 습득하든 하자
# ================================================================================================================================

# <수학 연산> ====================================================================================================================
# ▶▶▶ numpy.add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) -> ndarray or scalar
# np.add(x1, x2) 대신 x1 + x2 이렇게 연산자도 가능
print(np.add(1.11, 3.456)) # 4.566
x1 = np.arange(9.0).reshape((3,3))
x2 = np.arange(3.0)
print(x1.__repr__())
# array([[0., 1., 2.],
#        [3., 4., 5.],
#        [6., 7., 8.]])
print(repr(x2))
# array([0., 1., 2.])

print(repr(np.add(x1, x2))) # np.add(x1, x2) == x1 + x2
# array([[ 0.,  2.,  4.],
#        [ 3.,  5.,  7.],
#        [ 6.,  8., 10.]])

# ▶▶▶ numpy.subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) -> ndarray 만약 x1,x2 둘 다 스칼라 값이면 결과도 스칼라 값이다.

print(repr(np.subtract(100, 10))) # 90
x1 = np.arange(12.0).reshape(3, 4)
x2 = np.arange(4.0)
print(x1)
# [[ 0.  1.  2.  3.]
#  [ 4.  5.  6.  7.]
#  [ 8.  9. 10. 11.]]
print(x2)
# [0. 1. 2. 3.]
print(np.subtract(x1, x2).__repr__())
# array([[0., 0., 0., 0.],
#        [4., 4., 4., 4.],
#        [8., 8., 8., 8.]])

# ▶▶▶ numpy.multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) -> ndarray 마찬가지로 x1, x2 둘 다 스칼라 값이면 결과도 스칼라 값이다.
print(np.multiply(1.123, 2.345))  # 2.6334350000000004
x1 = np.array([
    (2, 2, 2, 2),
    (3, 3, 3, 3),
    (4, 4, 4, 4)
])

x2 = np.array([
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
])
print(x1.__repr__())
print(x2.__repr__())
x3 = np.multiply(x1, x2)
print(x3.__repr__())
# array([[ 2,  2,  2,  2],
#        [ 6,  6,  6,  6],
#        [12, 12, 12, 12]])

print((x3 * np.array([10, 10**2, 10**3, 10**4])).__repr__())
# array([[    20,    200,   2000,  20000],
#        [    60,    600,   6000,  60000],
#        [   120,   1200,  12000, 120000]])

# ▶▶▶ numpy.matmul(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis]) -> 각 x1과 x2의 마지막 2개의 차원으로 2차원 행렬의 곱셈 연산을 한다
x1 = np.ones([9, 5, 7, 4])
x2 = np.ones([9, 5, 4, 3])
print(np.dot(x1, x2))          # 4로 이루어진 (9, 5, 7, 9, 5, 3) 모양의 ndarray
print(np.dot(x1, x2).shape)    # (9, 5, 7, 9, 5, 3)

print(np.matmul(x1, x2).shape) # (9, 5, 7, 3)
# np.matmul(x1, x2) -> x1과 x2의 각각 마지막 2개의 차원 을 행렬곱 연산을 한다
# (n, k), (k, m) -> (n, m)    n is 7, k is 4, m is 3

x1 = np.arange(2 * 2 * 4).reshape((2, 2, 4))
x2 = np.arange(2 * 2 * 4).reshape((2, 4, 2))
print(np.matmul(x1, x2).shape)    # (2, 2, 2) == (x1 @ x2).shape
print(x1 @ x2)
# [[[ 28  34]
#   [ 76  98]]

#  [[428 466]
#   [604 658]]]

x1 = np.arange(2 * 2 * 3 * 2).reshape(2, 2, 3, 2)
x2 = np.arange(2 * 2 * 2 * 3).reshape(2, 2, 2, 3)
print(np.matmul(x1, x2))
# [[[[  3   4   5]
#    [  9  14  19]
#    [ 15  24  33]]

#   [[ 99 112 125]
#    [129 146 163]
#    [159 180 201]]]


#  [[[339 364 389]
#    [393 422 451]
#    [447 480 513]]

#   [[723 760 797]
#    [801 842 883]
#    [879 924 969]]]]



# ▶▶▶ numpy.divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
# ▶▶▶ numpy.true_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
# ▶▶▶ numpy.floor_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
x1 = np.arange(5)
print(np.true_divide(x1, 4))  # [0.   0.25 0.5  0.75 1.  ]
print(x1 / 4)                 # [0.   0.25 0.5  0.75 1.  ]
print(np.floor_divide(x1, 4)) # [0 0 0 0 1]
print(x1 // 4)                # [0 0 0 0 1]

# 수학시간에 배운 자연상수e(대략 2.718281)의 지수연산    [자연상수e = 자연로그의 밑]
# ▶▶▶ numpy.exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
# 자연수 2의 지수연산
# ▶▶▶ numpy.exp2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
x1 = np.arange(2 * 2 * 3).reshape(2, 2, 3)
print(np.exp(x1))
# [[[1.00000000e+00 2.71828183e+00 7.38905610e+00]
#   [2.00855369e+01 5.45981500e+01 1.48413159e+02]]

#  [[4.03428793e+02 1.09663316e+03 2.98095799e+03]
#   [8.10308393e+03 2.20264658e+04 5.98741417e+04]]]
print(np.exp2(x1))
# [[[1.000e+00 2.000e+00 4.000e+00]
#   [8.000e+00 1.600e+01 3.200e+01]]

#  [[6.400e+01 1.280e+02 2.560e+02]
#   [5.120e+02 1.024e+03 2.048e+03]]]

# 모든 요소에 - 또는 + 를 붙인 것과 같다
# ▶▶▶ numpy.negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
# ▶▶▶ numpy.positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

x1 = np.array([(1, -2,), (3, -4)])
print(np.negative(x1))      # -x1 와 같다
# [[-1  2]
#  [-3  4]]
print(np.positive(x1))      # +x1
# [[ 1 -2]
#  [ 3 -4]]


# 거듭제곱 연산
# ▶▶▶ numpy.power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
# ▶▶▶ numpy.square(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) -> 요소별 제곱을 반환
x1 = np.array(([1,2,3,3,2,1], [1,2,3,3,2,1]))
x2 = np.arange(6)
print(np.power(x1, x2))     # x1 ** x2 와 같다
# [[ 1  2  9 27 16  1]
#  [ 1  2  9 27 16  1]]
print(np.power(x2, x1))     # x2 ** x1 와 같다
# [[ 0  1  8 27 16  5]
#  [ 0  1  8 27 16  5]]
print(np.power(x1, 2))      # 음수의 거듭제곱은 ValueError 발생
# [[1 4 9 9 4 1]
#  [1 4 9 9 4 1]]

print(np.power(x1, -10+2J, dtype=np.complex128)) # dtype을 복소수타입으로 하면 음수도 되고 복소수도 됨
# [[ 1.00000000e+00+0.00000000e+00j  1.79157202e-04+9.59988028e-04j
#   -9.92827879e-06+1.37195656e-05j -9.92827879e-06+1.37195656e-05j
#    1.79157202e-04+9.59988028e-04j  1.00000000e+00+0.00000000e+00j]
#  [ 1.00000000e+00+0.00000000e+00j  1.79157202e-04+9.59988028e-04j
#   -9.92827879e-06+1.37195656e-05j -9.92827879e-06+1.37195656e-05j
#    1.79157202e-04+9.59988028e-04j  1.00000000e+00+0.00000000e+00j]]


# ▶▶▶ numpy.log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])   -> 밑이 e인 로그를 취한다
# ▶▶▶ numpy.log2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])  -> 밑이 2인 로그를 취한다
# ▶▶▶ numpy.log10(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) -> 밑이 10인 로그를 취한다.

x1 = np.array([1, np.e, np.e**2, 0])
print(np.log(x1))   # [  0.   1.   2. -inf]
x1 = np.array([0, 1, 2, 2**4])
print(np.log2(x1))  # [-inf   0.   1.   4.]
x1 = np.array([10E-3, 1.5E+4])
print(np.log10(x1)) # [-2.          4.17609126]


# ▶▶▶ numpy.sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])   -> 음이 아닌 요소별 제곱근을 반환
# ▶▶▶ numpy.cbrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])   -> 요소별 세제곱근(cube-root)을 반환

x1 = np.array([4-0J, 2+10J, -9J, 16J])
print(np.sqrt(np.power(x1, 2)))    # 제곱을 하고 다시 루트
# [4. +0.j 2.+10.j 0. +9.j 0.+16.j]

x2 = np.array([-1, -8, -27, -64])
print(np.cbrt(x2))
# [-1. -2. -3. -4.]




