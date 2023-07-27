# 문제 5

# 문제 4번 함수를 반복한 후 정답이 나오면
# 점수 출력 함수 get_score()
# 몇 번 시도했는가? 정답은 무엇인가? 출력 후 마무리.

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

def print_result(try_count, answer):
    print(f"시도한 횟수: {try_count}번")
    print(f"정답은 {answer}. 게임종료.")

def get_score(random_num):
    try_count = 0
    while True:
        try:
            user_input = int(input("두 자리 숫자 입력: "))
            if user_input < 1 or user_input > 101:
                print("두 자리 숫자 입력 요망")
                continue

            try_count += 1
            strike, ball = check_num(random_num, user_input)

            if strike == 2:
                print(f"{strike}S~! 정답!")
                print_result(try_count, random_num)
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

if __name__ == "__main__":
    import random

    def generate_random_number():
        return random.randint(1, 101)

    print('게임 시작!')
    answer = generate_random_number()
    get_score(answer)
