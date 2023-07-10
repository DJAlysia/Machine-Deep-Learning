# 택시기사가 매일 10명의 손님을 받아서 영업하는 데, 손님의 요금은 정해져있지 않다. 
# (매일 혹은 매 시간 책정되는 요금이 다름)
# 요금을 입력 받아 총합을 구하여라. 

total_fare = 0

for i in range(10):
    fare = float(input("손님의 요금을 입력하세요: "))
    total_fare += fare

print("오늘의 총 요금은", total_fare, "원입니다.")

# 택시기사가 오늘 받을 손님수를 입력하고 N
# N 번 만큼 손님의 요금을 input 받아서
# 오늘의 총 수입을 출력하시오

total_fare = 0
N = int(input("오늘 받은 손님의 수를 입력하세요: "))

for i in range(N):
    fare = float(input("손님의 요금을 입력하세요: "))
    total_fare += fare
    
print("오늘 총 손님수는", N,"명,", "오늘의 총 요금은", total_fare, "원입니다." )


