
import jieba
import jieba.posseg as pseg
import pymysql
import re
import codecs

def split_text(paragraphs):
  
    result = []
    current_paragraph = ''

    # 遍历每个段落
    for p in paragraphs:
        # 如果当前段落加上新段落的长度小于等于500，则合并到当前段落
        if len(current_paragraph) + len(p) <= 500:
            if current_paragraph:
                current_paragraph += '\n'
            current_paragraph += p
        # 否则，重新分段，并将当前段落添加到结果列表中
        else:
            result.append(current_paragraph)
            current_paragraph = p

    # 将最后一个段落添加到结果列表中
    if current_paragraph:
        result.append(current_paragraph)

    return result
# 连接数据库
conn = pymysql.connect(host='49.235.198.9', port=3306, user='root', passwd='3416403Ad/', db='chinese_text_db', charset='utf8')
cursor = conn.cursor()

# 打开文件并读取内容
file_path = 'e:/myProject/反正我是超能力者.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 按段落分割文本
paragraphs = paragraphs = re.split('\n+', content)
paragraphs = split_text(paragraphs)
print("共有", len(paragraphs), "段落：\n")

# 分词，提取名词，并存入数据库
for para in paragraphs:
    # 分词
    wtxt=re.sub(r"\s+", "", para)
    # 提取名词
    words = pseg.cut(wtxt)
    nouns = [word.word for word in words if word.flag.startswith('n')]
    # 将文本和名词存入数据库
    text = para.strip()
    keywords = ','.join(nouns)
    encoded_string = codecs.encode(text, 'utf-8')
    sql = "INSERT INTO cachetext (text, keywords) VALUES (%s, %s)"
    cursor.execute(sql, (encoded_string, keywords))
    conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()

