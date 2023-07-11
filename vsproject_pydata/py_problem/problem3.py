# 문제 1 사용자 함수를 정의하여 리스트 변수에 점수를 저장하고 
# 평균값과 맥스값을 구하는 코드를 작성하시오

#점수리스트배열
# score_list = []

# 점수를 입력해서 점수리스트에 저장하는 함수
# read_score()

#평균을 구하는 함수

#맥스값을 구하는 함수

# score_list = []
def read_score():
    score_list = []
    N = int(input("과목 수를 입력해주세요: "))
    for _ in range(N):
        score_list.append(int(input("과목 점수를 입력해주세요: ")))    
    return score_list

#평균을 구하는 함수
def mean_score(score_list):
    sum = 0
    for i in score_list:
        sum += i     
    return sum / len(score_list)

#맥스값을 구하는 함수
def max_score(score_list):
    return max(score_list)

score_list = read_score()
print("평균 점수는", mean_score(score_list), "점 입니다.")
print("맥스 점수는", max_score(score_list), "점 입니다.")

