import tiktoken
text = "Akwirw ier"
tokenizer = tiktoken.get_encoding("gpt2")
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers) # 打印词元ID


print(tokenizer.decode(integers))
print([tokenizer.decode([id]) for id in integers])