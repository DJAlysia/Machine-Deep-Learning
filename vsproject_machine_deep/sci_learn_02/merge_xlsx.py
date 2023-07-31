import pandas as pd

df_price = pd.read_excel('data/stock price.xlsx')
df_value = pd.read_excel('data/stock valuation.xlsx')

print(len(df_price))
print(len(df_value))
df_join = pd.merge(df_price, df_value) # 공동 컬럼 자동으로 찾음

# 공동 컬럼이 필수
print(df_join[['price','per']])


