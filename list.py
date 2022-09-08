# 列表的创建
lst = ['hello', 'world', 98]
lst1 = list([31, 213, 33])
print(lst)
print(lst[0])
# 索引，找到目标元素第一个所在位置的下标
print(lst.index('hello'))
print(lst.index(98, 1, 3))  # 从下标1开始找，找到下标3的前一个
# start=1(没写默认为0），stop=6（没写默认结束位置），step=2（没写表示步长为1）表示从下标1开始到下标6不包括6每次2步输出
lst2 = [10, 20, 30, 40, 50, 60, 70, 80]
lst3 = lst2[1:6:2]
print(lst3)
# 用in ，not in判断元素在列表中是否存在
for item in lst2:  # 遍历列表
    print(item)

# 用append在列表末端添加一个元素
lst2.append(90)
print(lst2)
# 用extend在列表末端至少添加一个元素
lst2.extend(lst3)
print(lst2)
# 用insert在列表任意位置添加一个元素
lst3.insert(1, 90)
print(lst3)
# 用切片在任意位置添加元素
lst2[1:] = lst3
print(lst2)

# 用remove删除第一个元素
lst2.remove(20)
print(lst2)
# 用pop删除指定索引上的元素，没有索引值时默认为最后的元素
lst2.pop(1)
print(lst2)
# 使用切片
new_list = lst3[1:3]
print(new_list)
lst2[1:2] = []
print(lst2)
# 使用del删除列表

# 修改列表的值
lst0 = [10, 20, 30, 40, 50, 60, 70]
lst0[2] = 90
print(lst0)
lst0[1:3] = [100, 200, 300, 400]
print(lst0)

# 使用sort将列表中所有元素按照默认值从小到大的顺序进行排序（sorted可以产生新的排序过的列表）
lst0.sort()
print(lst0)
lst0.sort(reverse=True)  # 降序排序
print(lst0)

list1 = [i * i for i in range(1, 10)]  # 列表生成式
print(list1)
