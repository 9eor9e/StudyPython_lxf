# 迭代
# 如果给定一个 list 或 tuple ，我们可以通过 for 循环来遍历这个 list 或 tuple ，这种遍历我们称为
# 迭代( iteration )。
# 在python中，迭代是通过 for...in 来完成的，而很多语言比如C语言，迭代list是通过下标完成的
# 比如，JAVA 代码：
# for (i=0;i<list.length;i++){
#     n = list[i];
# }
# 可以看出，pyton的 for 循环抽象程度要高于C的 for 循环，因为python的 for 循环不仅可以用在 list
# 或 tuple 上，还可以作用在其他可迭代对象上。

# list 这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，
# 都可以迭代，比如 dict 就可以迭代：
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是 key 。如果要迭代 value ，可以用 for value in d.values() ，如果
# 同时迭代 key 和 value ，可以用 for k,v in d.items() 。

# 由于字符串也是可迭代对象，也可以作用于 for 循环：
for ch in 'ABC':
    print(ch)

# 所以，当我们使用 for 循环时，只要作用于一个可迭代对象， for 循环就可以正常运行，而我们不太关心该
# 对象究竟是 list 还是其他数据类型。

## 如何判断一个对象是可迭代对象，方法是通过 collections 模块的 Iterable 类型判断：
from collections.abc import Iterable # python3.8中将弃用 from collections import Iterable
print(isinstance('abc',Iterable)) # str 是否可迭代
print(isinstance([1,2,3],Iterable)) # list 是否可迭代
print(isinstance(123,Iterable)) # 整数是否可迭代

# 如果要对 list 实现类似Java那样的下标循环，python内置的 enumerate 函数可以把一个 list 变成
# 索引-元素对，这样就可以在 for 循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print(i,value)
# 上面的 for 循环里，同时引用了两个变量，在python里是很常见的，比如：
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    # 使用for循环取出L内所有元素
    for i in L:
        x = min(L) # 把L中最小的元素赋值给x
        y = max(L) # 把L中最大的元素赋值给y
    return (x,y)
L = (1,2,3,4,5,6,7,8)
print(findMinAndMax(L))