"""
날짜 : 2021/03/04
이름 : 김철학
내용 : 파이썬 데이터베이스 SQL 실습
"""
import pymysql

conn = pymysql.connect(host='192.168.10.114',
                       user='chhak',
                       password='1234',
                       db='chhak',
                       charset='utf8')

cur = conn.cursor()

sql = "DELETE FROM `USER1` WHERE `uid`='p101';"
cur.execute(sql)
conn.commit()

conn.close()

print('DELETE 완료...')

