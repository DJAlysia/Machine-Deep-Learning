import pandas as pd
import glob

# CSV 파일들의 경로 가져오기
file_paths = glob.glob('C:/Users/user/OneDrive/Study/휴먼-자바 파이썬 AI/NCS/소상공인시장진흥공단_상가(상권)정보_20230630/상가(상권)정보_20230630/*.csv')  # 실제 파일 경로에 맞게 수정

# 빈 DataFrame 생성
data_merge = pd.DataFrame()

# 각 파일을 읽어와서 데이터 결합
for file_path in file_paths:
    data = pd.read_csv(file_path, encoding='utf-8')
    data_merge = pd.concat([data_merge, data], ignore_index=True)

# 전체 데이터를 하나의 CSV 파일로 저장
data_merge.to_csv('소상공인시장진흥공단_상가(상권)정보_202106.csv', index=False, encoding='utf-8-sig')

print("전국 파일 생성 완료")

# CSV 파일 읽어오기
data = pd.read_csv('C:/KDY/Machine_Deep/Machine-Deep-Learning/소상공인시장진흥공단_상가(상권)정보_202106.csv', encoding='utf-8')

# 편의점 브랜드명 리스트
convenience_stores = ['GS25', 'CU', '세븐일레븐']

# 편의점 브랜드별 총 갯수 구하기
brand_counts = {}
for store in convenience_stores:
    brand_counts[store] = data[data['상호명'].str.contains(store)].shape[0]

# 결과 출력
for store, count in brand_counts.items():
    print(f"{store} 편의점 총 갯수: {count}")