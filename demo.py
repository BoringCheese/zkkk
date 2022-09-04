# 输入函数input input括号里面属于提示词
a = int(input('输入一个加数 '))
# a=int(a)
b = int(input('输入另一个加数 '))
# b=int(b)
print(a + b)

print(1 + 1)  # 加法
print(2 - 1)  # 减法
print(2 * 4)  # 乘法
print(4 / 2)  # 除法
print(11 // 2)  # 整除 结果向下取整为int
print(11 % 2)  # 取余 余数=被除数-除数*商（商为整除结果）
print(2 ** 3)  # 2的3次方

a = b = c = 20  # 链式赋值
a, b, c = 20, 30, 40  # 解包赋值 可以用来进行交换二个变量的值
a, b = b, a

# 比较对象的标识使用    is
print(a is b)
print(a is not b)

#布尔类型比较 and or not（与 或 非）
#位运算&按位与，|按位或，>>右移运算符，<<左移运算符
