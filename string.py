# 字符串定义
a = 'python'
b = "python"
c = '''python'''
print(a, b, c)
# 字符串查询操作index()查找字符串第一次出现的位置，没有则报错。rindex()查找字符串最后一次出现的位置，没有则报错
#       *推荐*   find()查找字符串第一次出现的位置，没有返回-1。rfind()查找字符串最后一次出现的位置，没有返回-1
#             upper()转大写，lower()转小写，swapcase()大写变小写，小写变大写，capitalize()第一个字符大写，其他小写，title()每个单词第一个字符大写其他小写
#    s.center(20,'*')居中对齐      s.ljust(20,'*') s.rjust(20,'*')左右对齐s.zfill(20)右对齐多的用0填充
#   s.split()劈分默认是空格  使用s.split(sep='|')来确定劈分符号 用max-split来指定最大劈分的次数  s.rsplit()从右边开始劈分
#   isidentifier()是否是合法的标识符 isspace()是否是空白字符串 isalpha()是否全是字母 isdecimal()是否全是十进制数
#   isnumeric()是否全是数字 isalnum()是否全是由数字和字母组成
#   replace(,,)第一个是要被替换的字串，第二个是替换的字符串，第三个是替换的次数
s = 'hello,Python'
print(s.replace('Python', 'Java'))
# join()将列表或者元组中的字符串合并为一个
lst = ['hello', 'java', 'python']
print('|'.join(lst))

# 字符串比较操作 >,>=,<,<=,==,!=
print('apple' > 'app')

# 字符串的切片操作
s = 'hello,python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
news = s1 + s3 + s2
print(news)

# 格式化字符串的俩种方式：%s(字符串)，%i或%d(整数)，%f(浮点数)  或  {}作占位符
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))
print('我叫{0},今年{1}岁'.format(name, age))
print(f'我叫{name},今年{age}岁')

# 编码与解码
s = '奶茶店的成绩啊'
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
