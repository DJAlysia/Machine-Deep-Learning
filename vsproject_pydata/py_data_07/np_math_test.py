# 2차원 데이터 4*4 형태로 선언
# math 데이터
# eng 데이터

# 두 과목의 합계를 구하고
# 평균, 최대값, 최소값, 합계

import numpy as np

math = [
    [90, 70, 60, 70],
    [80, 90, 60, 80],
    [100, 80, 90, 90],
    [80, 60, 70, 80]
]

eng = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

# 합계
sum = np.array(math) + np.array(eng)
print(sum)

# 평균
average = np.average(sum)
print(average)

# 최대값
max = np.max(sum)
print(max)

# 최소값
min = np.min(sum)
print(min)

