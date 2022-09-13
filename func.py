# 函数创建和调用 def 函数名([输入参数]):
#                  函数体
#                  return xxx
#
def calc(a, b):
    c = a + b
    return c


'''
没有返回值，return可以不写
一个返回值，直接返回类型
二个以上的返回值，则返回元组
'''

summ = calc(10, 20)
print(summ)
'''
函数调用所进行的传参
如果是不可变对象，函数体内的修改不会影响到实参的值
如果是可变对象，函数体内的修改会影响到实参的值
'''


def fun(*args):  # 关键字不确定时候，形参变为元组,只能有一个
    print(args)


fun(10)
fun(10, 29)


def fun1(**args):  # 形参变为字典,只能有一个
    print(args)





def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n - 1)


print(jiecheng(5))


fun1(a=10)
fun1(a=10, b=29)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums)
n1 = nums[0:n - k]
n2 = nums[n - k:]
n1.reverse()
n2.reverse()
n3 = n1 + n2
n3.reverse()
print(n3)
