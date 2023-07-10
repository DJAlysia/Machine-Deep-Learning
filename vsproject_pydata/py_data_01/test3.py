# 어떤 반에 학생 5명 있고
# 각 사람의 자바 javas 는 80 60 70 90 75 일때
# 각 사람의 학점을 출력하시오.

# 각 학생의 점수만 추출
javas = [80, 60, 70, 90, 75]

for score in javas:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print("학점:", grade)


# 학생 이름도 같이 추출
students = ['학생1', '학생2', '학생3', '학생4', '학생5']
javas = [80, 60, 70, 90, 75]

for name, score in zip(students, javas):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(name, "의 학점:", grade)

