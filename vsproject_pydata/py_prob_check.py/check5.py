# 문제 5

def even_check_list(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

data = [4, 3, 5, 6, 9, 5, 3, 2, 6, 8]

result = even_check_list(data)
print(result)
