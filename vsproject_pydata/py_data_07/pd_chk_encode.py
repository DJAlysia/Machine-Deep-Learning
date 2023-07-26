# 텍스트 파일 인코딩 방식 확인
# 데이터 분석 직접 아닌데

import chardet
import numpy as np
import pandas as pd

df = pd.read_csv('vsproject_pydata\data\students.csv', encoding='utf-8')
# df = pd.read_csv('vsproject_pydata\data\zipdoro.csv', encoding='cp949')
# 일반적으로 utf-8 기본인데 프로그램에 따라 ms:cp949, euc-kr

print(df)
# 1 각 과목별 평균
# 2 학생별 총점과 평균
# 3 총점이 가장 좋은 학생 출력


