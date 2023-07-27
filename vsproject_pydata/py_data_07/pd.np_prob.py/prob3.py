# 문제3

# 중복되지 않는 2자리 숫자 만드는 함수 generate_num()
# (예시) 34, 78(ok) 77, 99(x)
import random

def generate_num():
    while True:
        num = random.randint(1, 100)
        if len(set(str(num))) == 2:
            return num

print(generate_num())
