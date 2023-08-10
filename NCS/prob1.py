# 문제 1

# 함수 생성
def solution(a, b, c):
    answer = 0

    if a == b == c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif a == b or b == c or a == c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        answer = a + b + c
    
    return answer

# ---------------------------------------------------------------------------------------
# 임의의 숫자 예시로 입력
a, b, c = 2, 3, 4
result = solution(a, b, c)
print("점수:", result)
