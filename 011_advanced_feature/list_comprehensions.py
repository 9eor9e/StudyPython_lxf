# 列表生成式
# List Comprehensions ,是python内置的非常简单却强大的可以用来创建list的生成式。
# 例如，要生成 list[1,2,3,4,5,6,7,8,9,10] 可以用 list(range(1,11)):
print(list(range(1,11)))
# 但如果要生成 [1x1,2x2,3x3,...,10x10],方法一是循环：
L = []
for x in range(1,11):
    L.append(x * x)
print(L)
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list:
print([x * x for x in range(1,11)])

## 写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把 list 创建出来，
## 十分有用，多写几次，很快就可以熟悉这种语法。

# for 循环后面还可以加上 if 判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1,11) if x % 2 == 0 ])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

# 三层和三层以上的循环就很少用到了。
# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入 os 模块
print([d for d in os.listdir('.')]) # os.listdir 可以列出文件和目录

# for 循环其实可以同时使用两个甚至多个变量,
# 比如  dict 的 items() 可以同时迭代 key 和 value:
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)
# 因此，列表生成式也可以使用两个变量来生成list：
d = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k,v in d.items()])

# 把一个 list 中所有的字符串变成小写：
L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

# if...else
# 使用列表生成式的时候，经常搞不清楚 if...else 的用法
# 例如，以下代码正常输出偶数：
print([x for x in range(1,11) if x % 2 == 0])
# 但是，我们不能在最后的 if 加上 else :
# print([x for x in range(1,11) if x % 2 == 0 else 0])
# >>> [x for x in range(1, 11) if x % 2 == 0 else 0]
#   File "<stdin>", line 1
#     [x for x in range(1, 11) if x % 2 == 0 else 0]
#                                               ^
# SyntaxError: invalid syntax
# 这是因为跟在 for 后面的 if 是一个筛选条件，不能带 else ，否则如何筛选？

# 另外有人发现把 if 写在 for 前面必须加 else ,否则报错：
# >>> [x if x % 2 == 0 for x in range(1, 11)]
#   File "<stdin>", line 1
#     [x if x % 2 == 0 for x in range(1, 11)]
#                        ^
# SyntaxError: invalid syntax
# 这是因为 for 前面的部分是一个表达式，它必须根据 x 计算出一个结果。因此，考察表达式：
# x if x % 2 == 0 ,它无法根据 x 计算出结果，因为缺少 else ，必须加上 else:
print([x if x % 2 == 0 else -x for x in range(1,11)])
# 上述 for 前面的表达式 x if x % 2 == 0 else -x 才能根据 x 计算出确定的结果。
# 可见，在一个列表生成式中，for 前面的 if...else 是表达式，而 for 后面的 if 是过滤条件，
# 不能带 else 。

# 练习
# 如果list中即包含字符串，又包含整数，由于非字符串类型没有 low() 方法，所以列表生成式会报错：
# >>> L = ['Hello', 'World', 18, 'Apple', None]
# >>> [s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'
# 使用内建的 isinstance 函数可以判断一个变量是不是字符串：
x = 'abc'
y = 123
print(isinstance(x,str))
print(isinstance(y,str))
# 请修改列表生成式，通过添加 if 语句保证列表生成式能正确地执行：
L1 = ['Hello','World',18,'Apple',None]
# print([L1 if isinstance(L1,str) else L1.pop() for L2 in L1])
print([L2 for L2 in L1 if isinstance(L2,str) == True])