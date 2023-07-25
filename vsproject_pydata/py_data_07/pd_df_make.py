# 컬럼명
# rank [1,2,3,4,5]
# title ['제목1',....]
# album, 
# link_url
# 멜론차트에서 5개의 정보를 df 자료형으로 정의

import pandas as pd
data = {
    'rank': [1,2,3,4,5],
    'title': ['super shy','세븐','ETA','Queencard','말해요'],
    'album': ['뉴진스','세븐틴','뉴진스','필','얼론'],
    'link_url': ['youtube.com?s=s','youtube.com?s=s','youtube.com?s=s','youtube.com?s=s','youtube.com?s=s']
}
df = pd.DataFrame(data)
df.rename(columns = 
          {'rank':'순위','title':'제목','album':'앨범','link_url':'링크'})
print(df)

