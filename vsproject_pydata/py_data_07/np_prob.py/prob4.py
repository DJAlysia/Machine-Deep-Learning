# 문제4

# 1~30까지 랜덤하게 데이터를 저장하고  
# 5보다 크고 10보다 작은 값을 모두 출력하시오.

import numpy as np

data = np.random.randint(1, 31, size=30)

result = data[(data > 5) & (data < 10)]
print(result)
