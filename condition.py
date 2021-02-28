for times in range(3):
    pwd = input('Please Enter you password')
    if pwd == 'password':
        print('You are Correct')
        break
    else:
        print('Error! Try again. You have', 2 - times, 'chances')
else:
    print('Sorry! Your account has been locked')

for item in range(1,51):
    if item%5==0:
        print(item)

# use continue
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)

# 9*9乘法表
for i in range (1,10,1):
    item=''
    for j in range (1,i+1,1):
        item += str(i)+'*'+str(j)+'='+str(i*j) + ' '
    print(item)

for i in range(1, 10, 1):
    item = ''
    for j in range(1, i + 1, 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()
