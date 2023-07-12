# 문제 4. 샘플 문자열에서
# text = 'In Brazil, the; Superior Electoral* Court bars former~ president'
# 특수문자들은 제거하고 단어를 분리해서 총 몇개가 있는지 출력하시오

import re

text = 'In Brazil, the; Superior Electoral* Court bars former~ president'
comp = re.sub('[^a-zA-Z\s]', '', text)
word_list = comp.split()

count = len(word_list)
print(count)

