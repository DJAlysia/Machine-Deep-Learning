# 1 부터 100 까지 숫자 중에 짝수만 출력

# 짝수만 출력(줄 바꿈)
for num in range(1, 101):
    if num % 2 == 0:
        print(num)

# 짝수만 출력
for num in range(1, 101):
    if num % 2 == 0:
        print(num, end=' ')
        
# 홀수만 출력
for num in range(1, 101):
    if num % 2 == 1:
        print(num, end=' ')
        

t = (1,2,3)
print(type(t))
print(t)
