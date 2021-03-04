"""
날짜 : 2021/03/04
이름 : 김철학
내용 : 파이썬 데이터베이스 프로그래밍
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='chhak',
                       password='1234',
                       db='chhak',
                       charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회')
    result = input('입력 : ')

    if result == '0':
        break
    elif result == '1':
        # 사용자 등록
        uid  = input('아이디 입력 : ')
        name = input('이름 입력 : ')
        hp   = input('휴대폰 입력 : ')
        age  = input('나이 입력 : ')

        cur = conn.cursor()
        sql = "INSERT INTO `USER1` VALUES ('%s', '%s', '%s', '%s');"
        cur.execute(sql % (uid, name, hp, age))
        conn.commit()

        print('사용자 등록 완료...')

    elif result == '2':
        # 사용자 조회

        cur = conn.cursor()
        sql = "SELECT * FROM `USER1`;"
        cur.execute(sql)

        for row in cur.fetchall():
            print('--------------------')
            print('아이디 :', row[0])
            print('이름 :', row[1])
            print('휴대폰 :', row[2])
            print('나이 :', row[3])
            print('--------------------')

        print('사용자 조회 완료...')

conn.close()

print('프로그램 종료...')

















