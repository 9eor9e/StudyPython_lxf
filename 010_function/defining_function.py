# 定义函数
# 在python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号 ： ，然后，在缩进块中编写函数体，
# 函数的返回值用 return 语句返回。

# 例如，我们定义一个求绝对值的 my_abs 函数为例：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
# 注意，函数体内部的语句在执行时，一旦执行到 return 时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环
# 可以实现非常复杂的逻辑。
# 如果没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None 。return None 可以简写为 return
# 在python交互环境中定义函数时，注意python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下

# 如果你已经把　my_abs() 的函数定义保存为　abstest.py 文件了，那么，可以在该文件的当前目录下启动python解释器，用
#　from abstest import my_abs 来导入　my_abs() 函数，注意　abstest 是文件名(不含　.py 扩展名)

# 空函数　，　如果想定义一个什么事也不做的空函数，可以用　pass　语句
def nop():
    pass
# pass 可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个　pass ，让代码能运行起来。

#　pass　还可以用在其他语句里
#if age >= 18:
#   pass
# 缺少了　pass ,代码运行就会有语法错误

#　参数检查　，　调用函数时，如果参数个数不对，python解释器会自动检查出来，并抛出　TypeError
# >>> my_abs(1, 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: my_abs() takes 1 positional argument but 2 were given

# 但是如果参数类型不对，python解释器就无法帮我们检查。
# >>> my_abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in my_abs
# TypeError: unorderable types: str() >= int()
# 系统自带绝对值函数　abs()
# >>> abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for abs(): 'str'
# 当传入了不恰当的参数时，内置函数　abs 会检查出参数错误，而我们定义的　my_abs 没有参数检查，会导致　if　语句出错，
# 出错信息和　abs　不一样。所以，这个函数定义不够完善。

#　修改 my_abs() 函数的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数　isinstance()　
# 实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误
# >>> my_abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in my_abs
# TypeError: bad operand type

# 返回多个值
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
# import math 语句表示导入　math　包，并允许后续代码引用　math　包里的　sin 、cos 等函数
x,y = move(100,100,60,math.pi /6)
print(x,y)
# 但其实这只是一种假象，python函数返回的仍然是单一值
r = move(100,100,60,math.pi / 6)
print(r)
# 原来返回值是一个tuple!但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#　所以，python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 定义函数时，需要确定函数名和参数个数
# 如果有必要，可以先对参数的数据类型做检查
# 函数体内部可以用 return 随时返回函数结果
# 函数执行完毕也没有 return 语句时，自动 return None
# 函数可以同时返回多个值，但其实就是一个tuple

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax2+bx+c=0ax^2+bx+c=0ax2+bx+c=0 的两个解。
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    #g= (-b +- math.sqrt(b*b-4*a*c))/2*a
    d = math.sqrt(b*b - 4*a*c)
    x1 = ((-b) + d)/2*a
    x2 = ((-b) - d)/2*a
    return x1,x2
f = quadratic(2,1,3)
print(f)