# invoking function 调用函数
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数 abs ，只有一个参数。
# 可以上python官网查看文档，也可以在交互命令行通过 help(abs) 查看 abs 函数的帮助信息。
print(abs(100))
print(abs(-10))
print(abs(12.34))

# 调用函数的时候，如果传入的参数数量不对，会报 TypeError 的错误，并且python会明确地告诉你 abs() 有且仅有1个参数。
# 但给出了两个：
# >>> abs(1, 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: abs() takes exactly one argument (2 given)
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报 TypeError 的错误，并且给出错误信息：
# str 是错误的参数类型：
# >>> abs('a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for abs(): 'str'

# 而 max 函数 max() 可以接收任意多个参数，并返回最大的那个：
print(max(1,2))
print(max(2,3,1,-5))

# 数据类型转换
# python内置的常用函数还包括数据类型转换函数，比如 int() 函数可以把其他数据类型转换为整数：
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个”别名“：
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用 abs 函数

# 练习 ， 利用python内置的 hex() 函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))