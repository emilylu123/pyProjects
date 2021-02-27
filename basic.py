print('Python:')
print('hello world')

# do not change new line
print('Python:', 'Hello', 'World')

# write to document
''' multiple line comments or  ' * 3 or " * 3
fp = open('./output.txt', 'a+')
print('Multiple','Line', 'Commets', '!', file=fp)
fp.close()
'''

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

print('Decimal:', 1000, type(1000))
print('Float:', -1000.0, type(-1000.0))
print('Binary 0b1000:', 0b1000)  # 二进制
print('Octal 0o1000:', 0o1000)  # 八进制
print('Hexadecimal 0x1000:', 0x1000)  # 十六进制
print()

# float operations may not be accurate
a = 1.1
b = 2.2
print('1.1 + 2.2 =', a + b)
# solution
from decimal import Decimal

print('Use Decimal: ', Decimal('1.1') + Decimal('2.2'))

# boolean 可做运算 变int
f1 = True
f2 = False
f3 = f1 + 1
f4 = f2 + 1
print(f1, type(f1))  # True <class 'bool'>
print(f2, type(f2))  # False <class 'bool'>
print(f3, type(f3))  # 2 <class 'int'>
print(f4, type(f4))  # 1 <class 'int'>

# str using 'str1' "str2" or '''multiple lines'''
print('single quote string:')
print("double quotes sting:")
print('''Triple 

    quotes''')

# change data type -> str() int() float()
print('float -> str:', str(3.14), type(str(3.14)))
print('bool -> int:', int(True), type(int(True)))
print('str -> int  :', int('123'))
print('float -> int:', int(3.14))
print('str -> float:', float('123'))
print('int -> float:', float(123))
# error int('3.14')

# input
name = input("What's your name?")
print('My name is', name)

# Example input1 + input2
result = int(input("Enter 1st number")) * int(input("Enter 2nd number"))
print('Result is ', result)

