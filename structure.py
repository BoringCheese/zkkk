money = 1000
# s = int(input('请输入你的成绩'))
s = 78
if 100 >= s >= 90:
    print('优秀')
elif 90 > s >= 80:
    print('良好')
elif 80 > s >= 60:
    print('及格')
elif 60 > s >= 0:
    print('不及格')
else:
    print('成绩输入错误')

# 条件表达式
a, b = 10, 20
print('a>b' if a >= b else 'b>a')

# pass语句，什么也不做，只是一个占位符，用在语法需要语句的地方
if s >= 80:
    pass
else:
    pass

# range()函数
r = range(10)  # 从0到10步长为1,不包括10
print(list(r))
r = range(1, 10)  # 从1到10步长为1,不包括10
print(list(r))
r = range(1, 10, 2)  # 从1到10步长为2,不包括10
print(list(r))
# 判断指定整数在序列中是否存在用 in, not in
print(10 in r)

# while
# else在下面表示循环正常结束时执行
sum1 = 0
a = 2
while a < 101:
    sum1 += a
    a += 2
else:
    print(sum1)

# for-in-
# for 自定义变量 in 可迭代变量 :
# else在下面表示循环正常结束时执行
for item in 'Python':  # 依次取出里面的值给item
    print(item)
for i in range(10):
    print(i)
for _ in range(5):  # 没有自定义变量用_代替
    print('没有自定义变量用_代替')
for i in range(100, 1000, 1):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    if i == a * a * a + b * b * b + c * c * c:
        print(i)
else:
    print('循环结束')

# break语句，用于结束循环结构，通常和if分支结构一起使用
# continue语句，用于结束当前循环，进入下一次循环。通常和if分支结构一起使用
