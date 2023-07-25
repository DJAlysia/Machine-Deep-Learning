# 문제 2
# 넘파이 사용해서 구구단 출력하기

import numpy as np

numbers = np.arange(1, 10)
print(numbers)

prob2 = numbers[:, np.newaxis] * numbers

print(prob2)
