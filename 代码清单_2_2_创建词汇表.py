# 2.2 创建词汇表
# 导入清单 2-1 中的预处理结果
from 代码清单_2_1_通过_Python_读取短篇小说_The_Verdict_作为文本样本 import preprocessed

# 2.3 将词元转换为词元ID(token ID)
# all_words = sorted(set(preprocessed))
all_words = sorted(list(set(preprocessed)))
vocab_size = len(all_words)
print("Vocabulary size: ", vocab_size) # 1130

all_words.extend(["<|endoftext|>", "<|unk|>"])


vocab = {token: id for id, token in enumerate(all_words)}
print(len(vocab.items()))

for i, item in enumerate(list(vocab.items())[-5:]):
    print(i, item)

# 打印词典的前50个，包装为可迭代的即可
for i, item in enumerate(vocab.items()):
    # print(item)
    if i >= 50:
        break