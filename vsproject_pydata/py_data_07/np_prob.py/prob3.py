# 문제 3
# 5*5 행렬에 1부터 ~25까지 차례대로 저장하고 15 값이 있는 위치를 출력하시오

import numpy as np

matrix = np.arange(1, 26).reshape((5, 5))

print(matrix)

place = np.where(matrix == 15)

print("15 위치:", list(zip(place[0], place[1])))
