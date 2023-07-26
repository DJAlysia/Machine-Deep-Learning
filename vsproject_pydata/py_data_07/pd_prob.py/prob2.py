#문제 2 
# 위의 데이터 프레임에서 "현재가"와 "동락률" 컬럼을 인덱싱하기 

import pandas as pd

data = [
    ['3R', 1510, 7.36],
    ['3SOFT', 1790, 1.65],
    ['ACTS', 1185, 1.28]
]

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['종목코드', '현재가', '등락률'])

# 인덱스명 변경
df.index = ['037730', '036360', '005760']

# "현재가"와 "동락률" 컬럼 인덱싱
current_price = df['현재가']
price_fluctuation_rate = df['등락률']

print(current_price)
print(price_fluctuation_rate)
