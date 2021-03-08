"""
날짜 : 2021/03/04
이름 : 김철학
내용 : 파이썬 SQLite 실습하기 교재 p291
"""

import sqlite3

try:
    conn = sqlite3.connect('./data/sqlite_db')

    cur = conn.cursor()

    sql = """
              CREATE TABLE IF NOT EXISTS `goods` (
                `code`  INTEGER    PRIMARY KEY,
                `name`  TEXT(30)   UNIQUE NOT NULL,
                `su`    INTEGER    DEFAULT 0,
                `dan`   REAL       DEFAULT 0.0
              );  
          """
    cur.execute(sql)
    
    # 레코드 추가
    cur.execute("insert into `goods` values(1, '냉장고', 2, 850000)")
    cur.execute("insert into `goods` values(2, '세탁기', 3, 550000)")
    cur.execute("insert into `goods` (`code`, `name`) values(3, '전자레인지')")
    cur.execute("insert into `goods` (`code`, `name`, `dan`) values(4, 'HDTV', 1500000)")
    conn.commit()

    # 레코드 추가 2차
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su   = int(input('su 입력 : '))
    dan  = int(input('dan 입력 : '))

    sql = f"INSERT INTO `goods` VALUES ({code}, '{name}', {su}, {dan})"
    cur.execute(sql)
    conn.commit()

    # 레코드 수정
    code = int(input('수정 code 입력 : '))
    su = int(input('수정 su 입력 : '))
    dan = int(input('수정 dan 입력 : '))



    # 레코드 삭제
    # 레코드 조회
    # 상품명 조회

except Exception as e:
    print('예외발생')
    conn.rollback()

finally:
    cur.close()
    conn.close()

