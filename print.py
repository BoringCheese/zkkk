

#可以输出字符串、数字和含有运算符的表达式
print(213)
print('helloworld')
print(1+2)

#可以将数据输出到文件中。注意！所指定的盘符存在，使用file=fp
fp = open('D:/text.txt', 'a+')
print('helloworld', file=fp)
fp.close()
