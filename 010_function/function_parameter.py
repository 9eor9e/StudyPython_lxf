# 函数的参数
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道
# 如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

# python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用 默认参数 、 可变参数 和
# 关键字参数 ，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 位置参数
# 例子 ， 计算x平方的函数
def power(x):
    return x * x
# 对于 power(x) 函数，参数 x 就是一个位置参数。
# 当我们调用 power 函数时，必须传入有且仅有的一个参数 x
print(power(5))
print(power(15))

# 如果要计算x的三次方，四次方，五次方，就需要修改 power(x) 函数，修改为 pow(x,n) ，用来计算x的n次方
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 对于这个修改后的 power(x,n) 函数，可以计算任意n次方
print(power(5,2))
print(power(5,3))
# 修改后的 power(x,n) 函数有两个参数： x 和 n ，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序
# 依次赋给参数 x 和 n

# 默认参数
# 新的 power(x,n) 函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少
# 一个参数而无法正常调用
# >>> power(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: power() missing 1 required positional argument: 'n'
# python的错误信息很明确：调用函数 power() 缺少了一个位置参数 n
# 这个时候，默认参数就派上用场了，由于我们经常计算x的平方,完全可以把第二个参数n的默认值设定为2
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 当我们调用 power(5) 时，相当于调用 power(5,2)
print(power(5))
print(power(5,2))
# 而对于 n > 2 的其他情况，就必须明确地传入 n ，比如 power(5,3)

# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则python的解释器会报错
# 二是如何设置默认参数
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数的好处就是能降低调用函数的难度。

# 例子 ， 一年级小学生注册的函数，需要传入 name 和 gender 两个参数
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
# 调用 enroll() 函数只需要传入两个参数
print(enroll('Sarah','F'))
# 如果要继续传入年龄、城市等信息，这样会使得调用函数的复杂度大大增加
# 我们可以把年龄和城市设为默认参数
def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数
print(enroll('Sarah','F'))
# 只有与默认参数不符的学生才需要提供额外的信息
print(enroll('Bob','M',7))
print(enroll('Adam','M',city='Tianjin'))
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
# 无论是简单调用还是复杂调用，函数只需要定义一个。

# 有多个默认参数时，调用的时候，即可以按顺序提供默认参数，比如调用 enroll('Bob','M',7) ,意思是， city 参数用
# 传进去的值，其他默认参数继续使用默认值。

# 默认参数很有用，但只用不当，也会掉坑里。
# 默认参数有个最大的坑
# 例子：
def add_end(L=[]):
    L.append('END')
    return L
# 当你正常调用时，结果似乎不错：
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
# 当你使用默认参数调用时，一开始结果也是对的：
print(add_end())
# 但是，再次调用 add_end() 时，结果就不对了：
print(add_end())
print(add_end())
# 默认参数时 [] ，但是函数似乎每次都“记住了”上次添加了 'END' 后的list
# 原因如下 ， python函数在定义的时候，默认参数 L 的值就被计算出来了，即 [] ，因为默认参数 L 也是一个变量，
# 它指向对象 [] ，每次调用该函数，如果改变了 L 的内容，则下次调用时，默认参数的内容就变了，不再是函数定义
# 时的 [] 了。

### 定义默认参数要牢记一点：默认参数必须指向不变对象！！

# 要修改上面的例子，我们可以用 None 这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 现在，无论调用多少次，都不会有问题：
print(add_end())
print(add_end())

### 为什么要设计 str 、 None 这样的不变对象？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了
### 由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
### 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

# 可变参数
# 在python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，
# 还可以是0个。
# 以数学题为例，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a,b,c...作为一个list或
# tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 但是调用的时候，需要先组装出一个list或tuple：
print(calc([1,2,3]))
print(calc([1,3,5,7]))
# 如果利用可变参数，调用函数的方式可以简化成这样：
# print(calc(1,2,3))
# print(calc(1,3,5,7))
# 在早期版本中这么写可能是可行的，但在python3.7版本中这么写会报 TypeError 错误
# Traceback (most recent call last):
#   File "/home/joker/PycharmProjects/StudyPython_lxf/010_function/function_parameter.py", line 130, in <module>
#     print(calc(1,2,3))
# TypeError: calc() takes 1 positional argument but 3 were given

# 我们把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 定义可变参数和定义一个 list 或 tuple 参数相比，仅仅在参数前面加一个 * 号。在函数内部，参数 numbers 接收到一
# 个 tuple ，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
print(calc(1,2))
print(calc())
# 如果已经有一个 list 或 tuple ，要调用一个可变参数，可以这么做：
num = [1,2,3]
print(calc(num[0],num[1],num[2]))
# 这种写法当然是可行的，问题时太繁琐，所以python允许你在 list 或 tuple 前面加一个 * 号，把 list 或 tuple的
# 元素变成可变参数传进去：
nums = [1,2,3]
print(calc(*nums))
# *nums 表示把 nums 这个 list 的所有元素作为可变参数传进去。这种写法相当有用，而且很常见！！！

# 关键字参数

