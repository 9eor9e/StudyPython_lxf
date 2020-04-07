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
#
