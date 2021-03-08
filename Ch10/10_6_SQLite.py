"""
날짜 : 2021/03/04
이름 : 김철학
내용 : 파이썬 SQLite 실습하기 교재 p289
"""
import sqlite3

conn = sqlite3.connect('./data/sqlite_db')
cur = conn.cursor()

sql = "CREATE TABLE IF NOT EXISTS `test_table` ("
sql += "`name` text(10),"
sql += "`phone` text(15),"
sql += "`addr` text(50)"
sql += ");"

cur.execute(sql)
cur.execute("INSERT INTO `test_table` VALUES ('홍길동', '010-1111-1111', '서울시');")
cur.execute("INSERT INTO `test_table` VALUES ('이순신', '010-2222-2222', '해남시');")
cur.execute("INSERT INTO `test_table` VALUES ('강감찬', '010-3333-3333', '평양시');")
conn.commit()


conn.close()