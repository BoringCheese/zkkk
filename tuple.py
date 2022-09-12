# 元组的创建
t = ('python', 'world', 99)  # 可以省略小括号，只有1个元素时需要加括号并在后面加个逗号
print(t)
t1 = tuple(('pdas', 'dsa', 122))
print(t1)
# 遍历元组
for item in t:
    print(item)

# 集合的创建
j = {'python', 'world', 97, 97}  # 集合内的元素不能重复
print(j)
j1 = set([2, 3, 1, 4, 2, 4])
print(j1)
j1 = set(range(6))
print(j1)
j1 = {2, 3, 1, 4, 2, 46}
print(j1)
j2 = set()  # 空集合
# 用in ，not in判断元素在集合中是否存在

#  增 集合元素新增用add加一个，用update至少加一个
j1.add(9)
print(j1)
j1.update({200, 3000, 400})
print(j1)
#  删 调用remove()删除指定元素，没有弹出错误,discard()删除指定元素，没有不弹出错误,pop()随机删除一个元素
#     clear()清空集合

# 集合的关系
# 用==和!=判断是否相等
s1 = {20, 30, 40, 50}
s2 = {30, 40, 50, 90}
print(s1 == s2)
# issubset()一个集合是否是另个集合的子集
print(s2.issubset(s1))
# issubset()一个集合是否是另个集合的超集
print(s1.issuperset(s2))
# isdisjoint()2个集合是否 没有交集
print(s1.isdisjoint(s2))

# 集合的数组操作
a1 = {10, 20, 30, 40, 50}
a2 = {20, 30, 40, 50, 60}
print(a1.intersection(a2))  # 2个集合的交集
print(a1 & a2)

print(a1.union(a2))  # 2个集合的并集
print(a1 | a2)

print(a1.difference(a2))  # a1集合减a2集合
print(a1 - a2)

print(a1.symmetric_difference(a2))  # 除去交集部分的数
print(a1 ^ a2)
