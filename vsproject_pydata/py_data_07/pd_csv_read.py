# xlsx 파일 - openpyxl 라이브러리
# csv 파일 - 텍스트 파일로 데이터 저장

import pandas as pd
import numpy as np

df = pd.read_csv('data/students.csv', encoding='utf-8')
# 일반적으로 utf-8 기본인데 프로그램에 따라 ms:cp949, euc-kr
print(df)

