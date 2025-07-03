# 首先是下载原始文本/数据集
import urllib.request
import os

url = ("https://raw.githubusercontent.com/rasbt/" 
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/" 
     "the-verdict.txt") 
file_path = "the-verdict.txt"
# 下载下来然后读取
if not os.path.exists(file_path):
    urllib.request.urlretrieve(url, file_path)

# 读取
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of characters in raw text: ", len(raw_text)) # 包含了所有字符（一个字节就是一个字符）
print(raw_text[:99])

# 获取词元列表
import re 
# text = "Hello,  world. This, is a test." 
# result = re.split(r'(\s)', text) 
# print(result)
# # ['Hello,', ' ', 'world.', ' ', 'This,', ' ', 'is', ' ', 'a', ' ', 'test.'] 为什么 ' ' 也包含在分割结果了
# result =re.split(r'([,.?!"()\']|--|\s)', text)
# print(result)
# # 删除空格，就是遍历列表删除空格，为什么要删除空格？什么情况下训练数据里的空格是有意义的？
# result = [item for item in result if item.strip()]
# print(result)

preprocessed = re.split(r'([,.:;?—_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
print(len(preprocessed))

# 清单 2-1 的末尾添加
if __name__ == "__main__":
    pass
