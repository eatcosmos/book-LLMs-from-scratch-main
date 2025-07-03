import re    
from 代码清单_2_2_创建词汇表 import vocab

class SimpleTokenizerV2:
    def __init__(self, vocab): # __init__是初始化函数
        self.str_to_int = vocab # 将词典赋值给类属性
        # vocab是一个字典，key是单词，value是数字
        # vocab = {"hello":0,"world":1} 就是词汇转换为索引
        self.int_to_str = {i:s for s,i in vocab.items()} # 将词典的key和value互换,vocab是{"hello",number}
        # {0:"hello",1:"world"} 就是索引转换为词汇
    
    def encode(self, text): # 处理输入文本、将其转换为次元ID
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text) # 使用正则表达式将文本分割成单词，就是按照特殊符号分割单词，得到的是一个列表
        # preprocessed = re.split(r"([,.?!_\"'()]|--|\s)", text)
        print(len(preprocessed))
        preprocessed = [
            # token两边可能是有空格的，所以再处理下，就是不考虑空格
            item.strip() for item in preprocessed if item.strip()
        ]
        print(len(preprocessed))
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed] # 就是遍历列表，得到对应的索引列表
        return ids # ids再传个decode
    
    def decode(self, ids): # 输入的是id列表
        # 这里用的是空格" "来拼接的，导致标点符号也带上了空格，所以要把标点符号之前的空格删除
        text = " ".join([self.int_to_str[id] for id in ids]) # vacab = {"hello":0,"world":1} 是一个词典
        
        text = re.sub(r'\s+([,.:;?!"()]\'])', r'\1', text) # 移除特定标点符号前的空格
        return text


# 调用
text1 = "Hello, do you like tea?" 
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join([text1, text2]) # 注意 <|endoftext|>两边有空白
print(text)
# 导入vocab

tokenizer = SimpleTokenizerV2(vocab)
# tokenizer.encode(text) # 编码得到id列表
ids = tokenizer.encode(text)
print(ids)

print(tokenizer.decode(ids))