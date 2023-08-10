def print_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# 다이아몬드 출력
n = 6  # 다이아몬드의 높이 설정
print_diamond(n)
