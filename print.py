from decimal import Decimal
# #号可以单行注释三引号可以多行注释

# print可以输出字符串、数字和含有运算符的表达式
print(213)
# 单引号双引号只能一行三引号可以多行
print('helloworld')
print(1 + 2)
n1 = 123
print(n1, type(n1))

# 可以将数据输出到文件中。注意！所指定的盘符存在，使用file=fp
fp = open('D:/text.txt', 'a+')
print('helloworld', file=fp)
fp.close()
# 用浮点型数进行计算，可能出现小数点位数不确定的情况
n1 = 1.1
n2 = 2.2
print(n1 + n2)
print(Decimal('1.1') + Decimal('2.2'))

name = '张三'
age = 23
print('我叫' + name + '今年' + str(age) + '岁')
