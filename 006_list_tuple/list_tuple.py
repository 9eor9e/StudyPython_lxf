# list（列表），list[数据1,数据2,...,数据n]，python内置的一种数据类型，是一种有序的集合，可以随时添加和删除其中的元素
print('list（列表），list[数据1,数据2,...,数据n]，python内置的一种数据类型，'
      '是一种有序的集合，可以随时添加和删除其中的元素')
classmates = ['Michael','Bob','Tracy']
print(classmates)

# len()函数可以获得list（列表）元素的个数
print('len()函数可以获得list（列表）元素的个数')
print(len(classmates))

# 用索引来访问list中每一个位置的元素，索引是从0开始
print('用索引来访问list中每一个位置的元素，索引是从0开始')
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 当索引超出范围时，python会报一个 IndexError 错误
print('当索引超出范围时，python会报一个 IndexError 错误')
#print(classmates[3])

# 索引最后位置元素，可以使用 [-1] 表示
print('索引最后位置元素，可以使用 [-1] 表示')
print(classmates[-1])
# 索引倒数第二位置元素
print('索引倒数第二位置元素')
print(classmates[-2])

# 使用 list.append() 方法，往list末尾追加元素
print('使用 list.append() 方法，往list末尾追加元素')
classmates.append('Adam')
print(classmates)

# 使用 list.insert() 方法，把元素插入指定位置
print('使用 list.insert() 方法，把元素插入指定位置')
classmates.insert(1,'Jack')
print(classmates)

# 使用 list.pop() 方法，删除list末尾的元素
classmates.pop()
print(classmates)

# 使用 list.pop(i) 方法，其中i是索引位置，用来删除指定位置的元素
classmates.pop(1)
print(classmates)

# 替换某个位置的元素，可以直接赋值给相应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素得到数据类型可以是不同的
L = ['Apple',123,True]
print(L)

# list元素也可以是另一个list
s = ['python','java',['asp','php'],'scheme']
print(len(s))
# 也可以写成如下格式
p = ['asp','php']
s = ['python','java',p,'scheme']
# 要拿到'php'可以写成p[1]或者s[2][1],s可以看成是一个二维数组
print(s[2][1])

# list中一个元素也没有，就是一个空的list，长度为0
L = []
print(len(L))

# tuple（元组） ,一种有序列表，和list类似，但tuple一旦初始化就不能修改
classmates_t = ('Michael','Bob','Tracy')
# tuple不能添加，插入，删除。因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

# tuple可以定义为空
t = ()
print(t)

# 如果tuple只有一个元素，则必须带上逗号，否则，python会解释为数字1
t = (1,)

# tuple的元素不可变指的是指向永远不变，而如果tuple里面的元素是list的话，list的元素会可变
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

