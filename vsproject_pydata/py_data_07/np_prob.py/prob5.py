# 문제 5

# 1~45까지 랜덤하게 shuffle
# 데이터를 저장(중복불가)하고 잘 섞어서
# 인덱스 0~5까지만 출력

import numpy as np

numbers = np.arange(1, 46)

np.random.shuffle(numbers)

result = numbers[:6]
print(result)

