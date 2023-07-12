# 1 파이썬에서 정규 표현식을 활용: re 모듈
import re

text = 'python is good for data'

mat = re.search('python', text)

result = mat.group()
print(result) 