# 문제 4

while True:
    print("원하는 연산을 선택하세요.")
    print("p. 덧셈")
    print("m. 뺄셈")
    print("c. 곱셈")
    print("d. 나눗셈")
    print("0. 나가기")

    choice = input("선택 (p/m/c/d/0): ")

    if choice == '0':
        print("프로그램을 종료합니다.")
        break
    elif choice in ['p', 'm', 'c', 'd']:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        if choice == 'p':
            result = num1 + num2
            operation = '+'
        elif choice == 'm':
            result = num1 - num2
            operation = '-'
        elif choice == 'c':
            result = num1 * num2
            operation = '*'
        else:
            if num2 != 0:
                result = num1 / num2
                operation = '/'
            else:
                print("잘못된 연산 입니다.")
                continue
        
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("잘못된 선택 입니다.")