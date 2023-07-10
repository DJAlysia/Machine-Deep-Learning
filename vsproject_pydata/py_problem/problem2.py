# 2차원 R행(5) C열(5) 로 이루어진 리스트 배열을 선언하고 1~25까지 값을 대입한 후 저장된 값을 출력하시오


array = [[0] * 5 for _ in range(5)]  
value = 1
for i in range(5):
    for j in range(5):
        array[i][j] = value
        value += 1

# 출력
for row in array:
    for x in row:
        print(x, end=' ')
    print()
