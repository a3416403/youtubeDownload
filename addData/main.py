import pymysql
import time
import re
 
def get_raw_label(rece):
 re1 = r'"([\s\S]*?)": "'           #-------------正则表达式
 reg1 = re.compile(re1)            # ------------编译一下
 str1 = reg1.findall(rece)
 return str1
 
def get_detail(rece):
 re2 = r'": "([\s\S]*?)",'           #-------------正则表达式
 reg1 = re.compile(re2)            # ------------编译一下
 str2 = reg1.findall(rece)
 return str2
 
def a_file(file,cur):
 model1= 29
 f = open(file, 'r', encoding='UTF-8')
 lines = f.readlines()    #readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表,该列表可以由 Python 的 for... in ... 结构进行处理.保存给lines
 
 for line in lines:     #循环执行每一行的内容
  model1+=1
  raw_label1 = get_raw_label(line)
  detail1 = get_detail(line)
 
  # 插入数据
  sql = """insert into renwu(create_time,model_id,keyWord,text) values (now(),%s,%s,%s)"""
  cur.execute(sql,[model1,raw_label1,detail1])
  db.commit()
 
db = pymysql.Connect(
    host='49.235.198.9',
    port=3306,
    user='root',
    passwd='3416403Ad/',
    db='doc_xiaoshuo',
    charset='utf8'
) #直接连入newdatabase库
cur = db.cursor() #获取游标
 
a_file("d:/doc/a.txt",cur)
 
db.close()