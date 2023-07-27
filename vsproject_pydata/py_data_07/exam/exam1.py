import numpy as np
import pandas as pd

# 1번: csv 파일 읽기
csv_file = 'vsproject_pydata/data/movies.csv'
df = pd.read_csv(csv_file, encoding='utf-8')
# movieId, title, genres
# 인덱스 번호
# print(df)
# 제목에서 (연도) 정보를 추출해서 새로운 컬럼을 만드시오
# print(df['title'].str.extract(r'(\d[4])'))
# print(df['title'].str[-5:-1])

years = []
for title in df['title']:
    years.append( title[-5:-1] )

df_years = pd.DataFrame(years, columns=['mov_year'])
df = pd.concat([df, df_years], axis=1)
print(df)

# 2번: 장르 종류 가져오기
# print(df['genres'].count())
# # print(df['genres'].str.split("|"))
# print(df.loc[10,:'genres'])
genres = [] # 장르의 정보를 저장
for gen in df['genres'] :
    genres.extend(gen.split('|')) # 입력 없으면 공백으로 분리    
# print(genres)
# print(len(genres))

# 3번: 장르들이 중복됨 - 중복제거
uni_genres = pd.unique(genres)
print(len(uni_genres))

# 4번: 장르별로 영화가 몇 개씩 인가? 
zero_result = np.zeros( len(uni_genres)) # 20개의 영화갯수 np
result=pd.DataFrame(zero_result, index=uni_genres, columns=['갯수'])
# print(result)
# for gen in df['genres'] : 이거 대신 아래 처럼 코드가 된 이유? 
for g in genres: # 장르를 | 로 분리해서 다 저장한 목록
    result.loc[g] += 1
print(result)






