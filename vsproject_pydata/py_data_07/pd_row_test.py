

# 행추가 5 연구 1500
df.loc[4] = [5, '연구', 1500]
# 행추가 6 홍보 1600
# 데이터프레임 간에 합칠 때 : append() 사라질 것임: 비추천
# 데이터프레임 + 데이터프레임에는 가능함

# df = pd.concat([df,df])
df = df.append(df, ignore_index=True)

# 총무 mng_id 를 NaN -> 1600 변경
df.loc[3, 'mng_id'] = 1600

# 정수로 변경
df['mng_id'] = df['mng_id'].astype(int)

print(df)

