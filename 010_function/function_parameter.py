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
