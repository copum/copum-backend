import glob
import os
import shutil
import re
import pymysql
from dotenv import load_dotenv

load_dotenv(dotenv_path='./config/.env')
env = os.environ
con = pymysql.connect(host=env.get('DATABASE_HOST'), user=env.get('DATABASE_USER'), password=env.get('DATABASE_PASSWORD'), charset='utf8')

cursor = con.cursor()
cursor.execute("drop database if exists {}".format(env.get("DATABASES")))
print('Database dropped[ {} ]'.format(env.get("DATABASES")))
cursor.execute("create database {}".format(env.get("DATABASES")))
print('Database created [ {} ]'.format(env.get("DATABASES")))

con.close()


files = glob.glob('./**/migrations/**', recursive=True)

reg = "migrations/$"
reg = re.compile(reg)
reg2 = "migrations/__init__.py$"
reg2 = re.compile(reg2)

for file in files:
    result = reg.findall(file)
    result2 = reg2.findall(file)
    if result or result2:
        continue
    if(os.path.exists(file)):
        os.remove(file) if os.path.isfile(file) else shutil.rmtree(file)
        print("{} 를 삭제합니다.".format(file))



os.system('python3 manage.py makemigrations')
os.system('python3 manage.py migrate')
