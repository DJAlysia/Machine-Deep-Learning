# 방법 1
# 나의 애완 동물
# 이름: 구름, 하늘, 별
# 몸무게: 4.3 / 3.4 / 2.5
# 개월 수: 12 / 8 / 2 

names = ["구름", "하늘", "별"]
weights = [4.3, 3.4, 2.5]
age_in_months = [12, 8, 2]

print("# 나의 애완 동물")
for i in range(len(names)):
    print("# 이름:", names[i])
    print("# 몸무게:", weights[i], "kg")
    print("# 개월 수:", age_in_months[i], "개월")


# 방법 2
names = ["구름", "하늘", "별"]
weights = [4.3, 3.4, 2.5]
age_in_months = [12, 8, 2]

for i in names:
    print(i, end=' ')
    
