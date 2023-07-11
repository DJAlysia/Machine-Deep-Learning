# 수학 영어 국어 3개의 값의 평균을 구하는 함수
# 소수점 반올림 소수 2째 자리에서 
# 60.4567 -> 60.5

def sub_mean():
    math = float(input("수학 점수 값을 입력해주세요: "))
    english = float(input("영어 점수 값을 입력해주세요: "))
    language = float(input("국어 점수 값을 입력해주세요: "))
    total_mean = (math + english + language)/3
    
    return round(total_mean, 1)

print("3 과목의 평균은", sub_mean(), "입니다.") 
    
# --------------------------------------------------------
