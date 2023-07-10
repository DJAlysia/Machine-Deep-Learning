# 사전형 자료를 정의해서
# 게시판 한 개의 정보를 저장하기
# 쇼핑몰 공지사항
# 게시물 번호 bno
# 게시물 제목 속성명 bname
# 게시물 작성 속성명 bwrite
# 게시물 조회 속성명 bhit
# print(notice) 출력

notice = {
            'bno': 1,
            'bname': '쇼핑몰 공지사항',
            'bwrite': '작성자',
            'bhit': 10
         }

print(notice)

# 키 값만 출력
for key in notice.keys():
    print(key, end=' ')
print()

# 값만 출력
for value in notice.values():
    print(value, end=' ')
print()

# 키, 값하고 모두 출력
for key, value in notice.items():
    print(key, value)