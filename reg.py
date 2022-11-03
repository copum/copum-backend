import re


mysetting_file = open('./config/my_settings.py','r')
data = mysetting_file.read()
reg = "env\(\'[A-Za-z_-]*\'\)"
reg = re.compile(reg,re.MULTILINE)
result = reg.findall(data)
env_file = open('./config/.env','w')
result = [re.sub('\'|env\(|\)', '', i) for i in result]
for i in result:
    env_file.write(i+"=\n")
env_file.close()
mysetting_file.close()