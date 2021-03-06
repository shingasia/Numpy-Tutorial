import numpy as np
import math
# ================================================================================================================================
# 서로 다른 배열을 함께 쌓기 -> 모든 array가 가능한 것은 아니고 차원(axis)에 따라서
# ================================================================================================================================

a = np.array(((10, 11), (12, 13)))
b = np.array([[100, 101], [102, 103], [104, 105]])
c = np.arange(-10, -14, -1).reshape(2, 2)

print(a.__repr__())
# array([[10, 11],
#        [12, 13]])
print(b.__repr__())
# array([[100, 101],
#        [102, 103],
#        [104, 105]])
print(c.__repr__())
# array([[-10, -11],
#        [-12, -13]])
print(repr(np.vstack((a, b, c)))) # v = 아마도 vertical
# array([[ 10,  11],
#        [ 12,  13],
#        [100, 101],
#        [102, 103],
#        [104, 105],
#        [-10, -11],
#        [-12, -13]])

# ================================================================================================================================
# 함수 column_stack은 1차원 array를 2차원 의 열로 쌓는다. 이것은 2차원 한에서만 hstack과 동일하게 동작한다
# 반면에 모든 입력 배열에 대해 row_stack과 vstack은 동일하다 실제로 row_stack은 vstack의 별칭이다.
# ================================================================================================================================

a = np.linspace(0, 2*np.pi, 8, dtype=np.float64).reshape(2, 4)
a = np.sin(a)
b = np.linspace(0, -2*np.e, 4).reshape(1, 4)
print(a[0])  # [0.         0.78183148 0.97492791 0.43388374]
print(a[1])  # [-4.33883739e-01 -9.74927912e-01 -7.81831482e-01 -2.44929360e-16]
print(b[0])  # [ 0.         -1.81218789 -3.62437577 -5.43656366]
print(a[0].ndim == a[1].ndim == b[0].ndim)    # True
print(a[0].shape == a[1].shape == b[0].shape) # True -> 전부다 1차원
print(a[0].shape) # (4,)

print(np.column_stack((a[0], b[0], a[1]))) # 보면 옆으로 붙이는 것이 확인된다.
# [[ 0.00000000e+00  0.00000000e+00 -4.33883739e-01]
#  [ 7.81831482e-01 -1.81218789e+00 -9.74927912e-01]
#  [ 9.74927912e-01 -3.62437577e+00 -7.81831482e-01]
#  [ 4.33883739e-01 -5.43656366e+00 -2.44929360e-16]]

a = np.linspace(1, 10, 12).reshape(2, 2, 3)
b = np.linspace(1, 100, 12).reshape(2, 2, 3)

print(a)
# [[[ 1.          1.81818182  2.63636364]
#   [ 3.45454545  4.27272727  5.09090909]]

#  [[ 5.90909091  6.72727273  7.54545455]
#   [ 8.36363636  9.18181818 10.        ]]]
print(b)
# [[[  1.  10.  19.]
#   [ 28.  37.  46.]]

#  [[ 55.  64.  73.]
#   [ 82.  91. 100.]]]
print(np.row_stack((a, b))) # np.vstack((a, b)) 와 같다
# [[[  1.           1.81818182   2.63636364]
#   [  3.45454545   4.27272727   5.09090909]]

#  [[  5.90909091   6.72727273   7.54545455]
#   [  8.36363636   9.18181818  10.        ]]

#  [[  1.          10.          19.        ]
#   [ 28.          37.          46.        ]]

#  [[ 55.          64.          73.        ]
#   [ 82.          91.         100.        ]]]
print(id(np.row_stack), id(np.vstack), np.row_stack is np.vstack) # 289172616 289172616 True

a = np.arange(2 * 8).reshape(2, 8)
print(a)
# [[ 0  1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14 15]]

print(np.hsplit(a, 4))
# [array([[0, 1],
#        [8, 9]]), 
#  array([[ 2,  3],
#        [10, 11]]), 
#  array([[ 4,  5],
#        [12, 13]]), 
#  array([[ 6,  7],
#        [14, 15]])]

a = np.arange(3 * 10).reshape(3, 10)
print(a)
# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]]

print(np.vsplit(a, 3))
# [array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]), 
#  array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]), 
#  array([[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])]

print(np.hsplit(a, 2))
# [array([[ 0,  1,  2,  3,  4],
#        [10, 11, 12, 13, 14],
#        [20, 21, 22, 23, 24]]), 
#  array([[ 5,  6,  7,  8,  9],
#        [15, 16, 17, 18, 19],
#        [25, 26, 27, 28, 29]])]






