# 다음 문자열의 불필요한 문자나 숫자를 제거하는 문제
# text_org = '**[세일]** 치와와 강아지 건식 소프트 5종 10000원 ....'
# 결과와 같이 문자열 처리하시오
# 결과 [치와와, 강아지, 건식, 소프트]

text_org = '**[세일]** 치와와 강아지 건식 소프트 5종 10000원 ....'

word_list = text_org.split()
result = [word for word in word_list if word.isalpha()]
print(result)
