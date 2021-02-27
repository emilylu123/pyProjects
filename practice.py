print('Python:')
print('hello world')

# do not change new line
print('Python:', 'Hello', 'World')

# write to document
# fp = open('./output.txt', 'a+')
# print('Hello', 'World', '!', file=fp)
# fp.close()

#  escape character \ 转义字符 ->  \n \r \t \b \\ \' \"
print('http:\\\\yingyao.codes')
print('\'yingyao.codes\'')
print(r'\'yingyao.codes\'')  # r will keep \ without changing

# ',' will add one space
name = 'Yingyao'
last_name = 'Lu'
print('Name:', name, last_name)

name += last_name  # Name: Yingyao Lu
print('Name:', name)  # Name: YingyaoLu


