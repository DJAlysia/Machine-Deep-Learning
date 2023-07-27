# 문제4

# 주제: 야구 숫자 게임
# 숫자 판별하는 함수 check_num()
# (예시) 34(랜덤숫자) - 입력 18 후 비교 후 - 없음
# (예시) 34(랜덤숫자) - 입력 32 후 비교 후 - 1S(스트라이크)
# (예시) 34(랜덤숫자) - 입력 35 후 비교 후 - 1S(스트라이크)
# (예시) 34(랜덤숫자) - 입력 43 후 비교 후 - 2B(2볼)
# (예시) 34(랜덤숫자) - 입력 34 후 비교 후 - 2S(2스트라이크)

def check_num(random_num, user_write):
    random_str = str(random_num)
    write_str = str(user_write)
    strike, ball = 0, 0

    for i in range(len(random_str)):
        if random_str[i] == write_str[i]:
            strike += 1
        elif random_str[i] in write_str:
            ball += 1

    return strike, ball

if __name__ == "__main__":
    import random

    def generate_random_number():
        return random.randint(1, 101)

    answer = generate_random_number()

    try_count = 0
    while True:
        try:
            user_input = int(input("두 자리 숫자 입력: "))
            if user_input < 1 or user_input > 101:
                print("두 자리 숫자 입력 요망")
                continue

            try_count += 1
            strike, ball = check_num(answer, user_input)

            if strike == 2:
                print(f"{strike}S~! 정답!")
                print(f"입력 횟수: {try_count}번")
                break
            elif strike == 0 and ball == 0:
                print("없음")
            else:
                result = ""
                if strike > 0:
                    result += f"{strike}S"
                if ball > 0:
                    result += f"{ball}B"
                print(result)

        except ValueError:
            print("두 자리 숫자 입력 요망")

