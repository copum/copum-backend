import pymysql
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='./config/.env')
env = os.environ

con = pymysql.connect(host=env.get('DATABASE_HOST'), user=env.get('DATABASE_USER'), password=env.get('DATABASE_PASSWORD'), database=env.get('DATABASE_NAME'), charset='utf8')

cur = con.cursor()

categories = [
    'Python',
    'Java',
    'JavaScript',
    'C',
    'C++',
    'Flutter',
    'Kotlin',
    'Swift',
    'Dart',
    'PHP',
    'TypeScript',
    'Go',
    'MySQL',
    'PostgreSQL',
    'MariaDB',
    'Oracle',
    'MySQL',
    'Redis',
    'MongoDB',
    'CS',
    'etc'
]

def category_generator():
    is_table = "show tables like 'categories'"
    cur.execute(is_table)
    row = cur.fetchone()
    if row is None :
        print("categories 테이블을 먼저 생성하세요...")
        return
    row = None
    select_category = "SELECT * FROM `Categories` limit 1"
    cur.execute(select_category)
    row = cur.fetchone()
    if row:
        return

    print("카테고리 생성 시작..")

    sql = "INSERT INTO `categories` VALUES "
    for category in categories:
        sql +="(null, '{}'), ".format(category)
    sql = sql[0: len(sql) -2]
    sql += ';'
    print(sql)
    cur.execute(sql)
    con.commit()
    con.close()
    print("카테고리 생성 끝..")

def create_media_dir():
    if(os.path.isdir('./media') == False):
        os.mkdir('./media')

def init():
    category_generator()
    create_media_dir()