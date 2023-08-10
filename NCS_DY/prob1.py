def solution(a, b, c):
    answer = 0

    if a == b == c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif a == b or b == c or a == c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        answer = a + b + c
    
    return answer

# 주어진 세 숫자로 점수 계산
a, b, c = 2, 2, 3  # 예시 입력
result = solution(a, b, c)
print("계산된 점수:", result)
