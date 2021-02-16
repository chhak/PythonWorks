"""
날짜 : 2021/02/16
이름 : 김철학
내용 : 파이썬 튜플 자료구조 실습하기
"""

# Tuple 생성
tuple1 = (1, 2, 3, 4, 5)
tuple2 = 1, 2, 3, 4, 5
tuple3 = ('한국', '미국', '일본', '중국', '호주')

print('typle1 type :', type(tuple1))
print('typle2 type :', type(tuple2))
print('typle3 type :', type(tuple3))

print('tuple1[0] :', tuple1[0])
print('tuple2[2] : %d' % tuple2[2])
print('tuple3[0] : %s' % tuple3[0])
print('tuple3[1] : %s' % tuple3[1])

#튜플은 원소 수정, 삭제 안됨 
tuple1[0] = 7
del tuple2[1]