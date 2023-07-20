# 문제 3

def convert_weight(weight, unit):
    conv = {
        'kg': 1,
        'g': 1000,
        'ton': 0.001,
        'pound': 2.204
    }
    return weight * conv[unit]

# 입력
input = input("입력: ")
weight, unit = input.split()

# 출력
result = convert_weight(float(weight), unit)
print(result)
