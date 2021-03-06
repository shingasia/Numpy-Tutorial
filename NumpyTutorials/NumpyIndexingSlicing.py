import random
import numpy as np

# ================================================================================================================================
# 1차원 array는 Python의 리스트, 기타 시퀀스 처럼 인덱싱, 슬라이싱, 이터레이팅 가능하다
# 다차원 array는 차원당 하나의 인덱스를 가질 수 있다. 이러한 인덱스들은 콤마로 구분된 튜플에 제공된다
# ================================================================================================================================

a = np.power(np.arange(10), 3)  # 물론 a = np.arange(10) ** 3 이렇게도 가능
print(a)          # [  0   1   8  27  64 125 216 343 512 729]
print(a[2])       # 8
print(a[-5])      # 125
print(a[::-1])    # [729 512 343 216 125  64  27   8   1   0]

a[:6:2] = 1000    # 이렇게 값 변경도 가능
print(a)          # [1000    1 1000   27 1000  125  216  343  512  729]


def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=np.int64)
print(b)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]

print(b[2, 3])    # 23
print(b[0:5, -3]) # [ 1 11 21 31 41]   각 행의 2 번째 요소  b[:, -3] 와 같다
print(b[:-2])     # 콤마가 없으므로 1차원을 슬라이싱 한 결과가 나온다
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]]

del a, b
# ================================================================================================================================
# dots(...)은 여러개의 콜론(:)이 필요할 때 대신 사용할 수 있다.
# 예를 들어 x가 5차원 배열일 때 
# x[1, 2, ...]    는 x[1, 2, :, :, :]
# x[..., 3]       는 x[:, :, :, :, 3]
# x[4, ..., 5, :] 는 x[4, :, :, 5, :] 이다
# ================================================================================================================================
a = np.arange(1 * 2 * 3 * 4 * 7).reshape(1, 2, 3, 4, 7)
print(a[...])          # a
# [[[[[  0   1   2   3   4   5   6]
#     [  7   8   9  10  11  12  13]
#     [ 14  15  16  17  18  19  20]
#     [ 21  22  23  24  25  26  27]]

#    [[ 28  29  30  31  32  33  34]
#     [ 35  36  37  38  39  40  41]
#     [ 42  43  44  45  46  47  48]
#     [ 49  50  51  52  53  54  55]]

#    [[ 56  57  58  59  60  61  62]
#     [ 63  64  65  66  67  68  69]
#     [ 70  71  72  73  74  75  76]
#     [ 77  78  79  80  81  82  83]]]


#   [[[ 84  85  86  87  88  89  90]
#     [ 91  92  93  94  95  96  97]
#     [ 98  99 100 101 102 103 104]
#     [105 106 107 108 109 110 111]]

#    [[112 113 114 115 116 117 118]
#     [119 120 121 122 123 124 125]
#     [126 127 128 129 130 131 132]
#     [133 134 135 136 137 138 139]]

#    [[140 141 142 143 144 145 146]
#     [147 148 149 150 151 152 153]
#     [154 155 156 157 158 159 160]
#     [161 162 163 164 165 166 167]]]]]
print(a[0, 0, :,:,:])  # a[0, 0, ...]
# [[[ 0  1  2  3  4  5  6]
#   [ 7  8  9 10 11 12 13]
#   [14 15 16 17 18 19 20]
#   [21 22 23 24 25 26 27]]

#  [[28 29 30 31 32 33 34]
#   [35 36 37 38 39 40 41]
#   [42 43 44 45 46 47 48]
#   [49 50 51 52 53 54 55]]

#  [[56 57 58 59 60 61 62]
#   [63 64 65 66 67 68 69]
#   [70 71 72 73 74 75 76]
#   [77 78 79 80 81 82 83]]]
print(a[..., 3, -5:-3])   # a[:, :, :, 3, -5:-3]
# [[[[ 23  24]
#    [ 51  52]
#    [ 79  80]]

#   [[107 108]
#    [135 136]
#    [163 164]]]]
print(a[..., ::-1, 1:4, 5:7])
# [[[[[ 68  69]
#     [ 75  76]
#     [ 82  83]]

#    [[ 40  41]
#     [ 47  48]
#     [ 54  55]]

#    [[ 12  13]
#     [ 19  20]
#     [ 26  27]]]


#   [[[152 153]
#     [159 160]
#     [166 167]]

#    [[124 125]
#     [131 132]
#     [138 139]]

#    [[ 96  97]
#     [103 104]
#     [110 111]]]]]

print(a[0, 0, 2])         # a[0, 0, 2, ...] 또는 a[0, 0, 2, :, :] 와 같다
# [[56 57 58 59 60 61 62]
#  [63 64 65 66 67 68 69]
#  [70 71 72 73 74 75 76]
#  [77 78 79 80 81 82 83]]


# ================================================================================================================================
# 다차원 배열에 대해 반복문을 수행하면 첫 번째 차원을 기준으로 수행된다.
# 그러나 배열의 각 요소에 대해 작업을 수행하려는 경우 방법 중 하나는 flat 속성을 사용하는 것이다.
# ================================================================================================================================
a = np.arange(3 * 4).reshape(3, 4)
for row in a:
    print(a)
print(len(a))   # 3


for element in a.flat:
    print(element, end=' ')  # 0 1 2 3 4 5 6 7 8 9 10 11
print()

# ================================================================================================================================
# Shape Manipulation (배열의 shape 형태를 조작)
# ================================================================================================================================

a = np.arange(3 * 4).reshape(3, 4)
print(repr(a.ravel()))   # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
print(repr(a.T))
# array([[ 0,  4,  8],
#        [ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11]])

a = np.arange(2 * 2 * 3).reshape(2, 2, 3)
print(a.T)
# [[[ 0  6]
#   [ 3  9]]

#  [[ 1  7]
#   [ 4 10]]

#  [[ 2  8]
#   [ 5 11]]]
print(a.T.shape)  # (3, 2, 2)


