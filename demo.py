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
