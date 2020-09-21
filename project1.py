m = input('请输入一个奇数')
if int(m) % 2 == 0:
    print("宁输错了")
else:
    i = 0
    while i < int(m):
        j = 0
        while j < int(m) - i - 1:
            print(' ',end="")
            j = j + 1
        j = 0
        while j < 1 + 2 * i:
            print('*',end="")
            j=j+1
        print("\n",end="")
        i = i + 1
        print("git测试")