# 문제 3

import pandas as pd
import glob

# 각 지역별 csv 파일 전국 파일로 결합시키기
file_paths = glob.glob('C:/Users/user/OneDrive/Study/휴먼-자바 파이썬 AI/NCS/소상공인시장진흥공단_상가(상권)정보_20230630/상가(상권)정보_20230630/*.csv')

data_merge = pd.DataFrame()

for file_path in file_paths:
    data = pd.read_csv(file_path, encoding='utf-8')
    data_merge = pd.concat([data_merge, data], ignore_index=True)

data_merge.to_csv('소상공인시장진흥공단_상가(상권)정보_202106.csv', index=False, encoding='utf-8-sig')

print("전국 파일 생성 완료")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

data = pd.read_csv('C:/KDY/Machine_Deep/Machine-Deep-Learning/소상공인시장진흥공단_상가(상권)정보_202106.csv', encoding='utf-8')

convenience_stores = ['GS25', 'CU', '세븐일레븐']

counts = {}
for store in convenience_stores:
    counts[store] = data[data['상호명'].str.contains(store)].shape[0]

for store, count in counts.items():
    print(f"{store} 편의점 총 갯수: {count}")