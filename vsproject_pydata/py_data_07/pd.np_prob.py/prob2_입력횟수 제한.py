# 문제2 check2.py
# 함수구현: 랜덤한 숫자를 맞추는 함수 guessNum() : 리턴값 카운트 횟수
#     숫자를 입력을 했는데
#     맞는 경우
#         함수가 끝나면서 결과를 리턴
#     틀리는 경우
#         다시 입력을 받아서 확인
#         랜덤숫자 55 > 40 : 숫자를 더 올려라 (UP)
#         랜덤숫자 55 < 90 : 숫자를 더 내려라 (DOWN)

# 테스트 결과물: 입력횟수: 5번 정답: 55 출력하고 게임 OVER


# ----------------------------------------------
# 입력횟수를 5로 제한하여 게임을 진행
# ----------------------------------------------
import random

def guessNum():
    random_number = random.randint(1, 101)
    attemp = 0
    max_attemp = 5

    while attemp < max_attemp:
        re_attemp = max_attemp - attemp
        try:
            user_input = int(input(f"1부터 100까지의 숫자를 입력하세요. (남은 기회: {re_attemp}번): "))
            attemp += 1

            if user_input == random_number:
                print(f"정답! 입력 횟수={attemp}번 / 정답={random_number}")
                break
            elif user_input < random_number:
                print("숫자를 더 올려라(UP)")
            else:
                print("숫자를 더 내려라(DOWN)")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    if attemp >= max_attemp:
        print(f"입력 횟수 {max_attemp}회가 끝났습니다. 정답은 {random_number}. 게임 OVER")

guessNum()

