# 1-N까지의 합을 구해서 출력하는 함수

def sum_cal(N):
    total_sum = 0
    
    for i in range(1, N+1):
        total_sum += i
    print("합은", total_sum)
sum_cal(50)
    
#---------------------------------------------------------    
def calculate_sum(N):
    total_sum = 0
    for num in range(1, N+1):
        total_sum += num
    # print("1부터", N, "까지의 합은", total_sum, "입니다.")
    return total_sum

# 함수 호출 및 출력
N=100
result = calculate_sum(N)
# calculate_sum(10)
print(result)
