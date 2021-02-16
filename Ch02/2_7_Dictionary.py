"""
날짜 : 2021/02/16
이름 : 김철학
내용 : 파이썬 딕셔너리 자료구조 실습하기
"""

#딕셔너리 생성
dic1 = {1: 'C++', 2: 'Java', 3: 'Python'}
dic2 = {
    'kor': '한국',
    'usa': '미국',
    'jpn': '일본',
    'chi': '중국'
}

dic3 = {
    101: [1, 2, 3, 4, 5],
    102: ('한국', '미국', '일본', '중국'),
    103: {'p1': '김유신', 'p2': '김춘추', 'p3': '장보고'}
}

#딕셔너리 데이터 출력
print('dic1 :', dic1)
print('dic1[1] :', dic1[1])
print('dic1[3] :', dic1[3])

print('dic2 :', dic2)
print("dic2['kor'] :", dic2['kor'])
print("dic2['usa'] :", dic2['usa'])

print('dic3 :', dic3)
print('dic3[101][2] :', dic3[101][2])
print('dic3[102][1] :', dic3[102][1])
print("dic3[103]['p3'] :", dic3[103]['p3'])

#딕셔너리 응용
dic_list = [dic1, dic2, dic3]

r1 = dic_list[0][3]
r2 = dic_list[1]['kor']
r3 = dic_list[2][103]['p1']

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)