import numpy as np

# <비교 연산> ====================================================================================================================

# x1과 x2의 요소별로 진리값(x1 > x2)을 반환
# ▶▶▶ numpy.greater(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
# -> 당연히 x1.shape 와 x2.shape 가 다르다면 공통 모양으로 브로드캐스트 할 수 있는 형태만 가능하다
# -> dtype=object가 전달되지 않는 한 일반적으로 bool 타입이다. x1, x2 둘 다 스칼라 값이면 결과도 스칼라 값이다

print(np.greater([10, 15, 20, 35], [19, 18, 17, 16])) # [False False  True  True]

x1 = np.arange(2 * 4).reshape(2, 4)
x2 = np.array((5, 5, 5, 5))
print(x1 > x2)
# [[False False False False]
#  [False False  True  True]]

# x1과 x2의 요소별로 진리값(x1 >= x2)을 반환
# ▶▶▶ numpy.greater_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

x1 = np.arange(3 * 3).reshape(3, 3)
x2 = np.array([5, 9, 3])
print(np.greater_equal(x1, x2)) # x1 >= x2 와 같다
# [[False False False]
#  [False False  True]
#  [ True False  True]]

# x1과 x2의 요소별로 진리값(x1 < x2)을 반환
# ▶▶▶ numpy.less(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

x1 = np.array([[2, 4, 6, 8], [10, 12, 14, 16]], dtype=np.float64)
print(np.less(x1, 9.3452))
# [[ True  True  True  True]
#  [False False False False]]

# x1과 x2의 요소별로 진리값(x1 <= x2)을 반환
# ▶▶▶ numpy.less_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

x1 = np.array([3, 4, 9])
x2 = np.array([[4, 4, 8], [10, 10, 9]])
print(np.less_equal(x1, x2))
# [[ True  True False]
#  [ True  True  True]]

# x1과 x2의 요소별로 진리값(x1 == x2)을 반환
# ▶▶▶ numpy.equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

x1 = np.array(((3.14, 3.14, 3.14, 3.14),(2.918, 2.918, 2.918, 2.918)), dtype=np.float64)
x2 = np.array((3.14, 3.14, 2.918, 2.918), dtype=np.float64)
print(np.equal(x1, x2)) # x1 == x2 또는 x1.__eq__(x2) 와 결과가 같다
# [[ True  True False False]
#  [False False  True  True]]

# x1과 x2의 요소별로 진리값(x1 != x2)을 반환
# ▶▶▶ numpy.not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

x1 = np.array(((3.14, 3.14, 3.14, 3.14),(2.918, 2.918, 2.918, 2.918)), dtype=np.float64)
x2 = np.array((3.14, 3.14, 2.918, 2.918), dtype=np.float64)
print(np.not_equal(x1, x2))
# [[False False  True  True]
#  [ True  True False False]]


# <논리 연산> ====================================================================================================================

# ================================================================================================================================
# logical_and -> x1 AND x2의 진리값을 계산  -> ex1) np.logical_and(x>1, x<4)
#                                              ex2) np.logical_and([True, False], [False, False])
# logical_or  -> x1 OR x2의 진리값을 계산   -> ex1) np.logical_or(x < 1, x > 3)
#                                              ex2) np.logical_or([True, False], [False, False])
# logical_xor -> x1 XOR x2의 진리값을 계산  -> ex1) np.logical_xor(x < 1, x > 3)
#                                              ex2) np.logical_xor([True, True, False, False], [True, False, True, False])
# logical_not -> NOT x의 진리값을 계산      -> ex1) np.logical_not(x<3)
#                                              ex2) np.logical_not([True, False, 0, 1])
# ================================================================================================================================





