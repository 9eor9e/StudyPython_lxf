# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在python中，这种一边循环一边计算的机制，
# 称为生成器： generator。

# 要创建一个 generator ,又有很多种方法。第一种方法很简单，只要把一个列表生成式的 [] 改成 () ，
# 就创建了一个 generator:
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# 创建 L 和 g 的区别仅在于最外层的 [] 和 () ，L 是一个list，而 g 是一个 generator。
# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
# 一个一个打印出来，可以通过 next() 函数获得 generator 的下一个返回值：
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# >>> next(g)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# generator 保存的是算法，每次调用 next(g) ,就计算出 g 的下一个元素的值，直到计算到最后一个
# 元素，没有更多的元素时，抛出 StopIteration 的错误。

# 上面这种不断调用 next(g) 实在是太变态了，正确的方法是使用 for 循环，因为 generator 也是可迭代对象：
g = (x*x for x in range(10))
for n in g:
    print(n)
# 所以，创建了一个 generator 后，基本上永远不会调用 next() ，而是通过 for 循环来迭代它
# ，并且不需要关心 StopIteration 的错误。
## generator 非常强大。如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，
# 还可以用函数来实现。
# 比如，著名的裴波拉契(Fibonacci)，除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1，1，2，3，5，8，13，21，34，...
# 裴波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却是很容易：
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
# 上面的函数可以输出裴波拉契的前N个数：
fib(6)
# 仔细观察，可以看出， fib 函数实际上是定义了裴波拉契数列的推算法则，可以从第一个元素开始，
# 推算出后续任意的元素，这种逻辑其实非常类似 generator。
# 当然，上面这种不断调用 next(g) 实在太变态了，正确的方法是使用 for 循环，因为 generator 也是可迭代对象：
g = (x * x for x in range(10))
for n in g:
    print(n)
# 所以，我们创建了一个 generator 后，基本上永远不会调用 next() ，而是通过 for 循环来迭代它，并且不需要关心
# StopIteration 的错误。
# generator 非常强大。如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，还可以用函数来实现。
# 比如，著名的裴波拉契数列 (Fibonacci) ,除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1，1，2，3，5，8，13，21，34，...
# 裴波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
# 上面的函数可以输出裴波拉契数列的前N个数：
fib(6)
# 仔细观察，可以看出，fib 函数实际上是定义了裴波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑
# 其实非常类似 generator 。
# 也就是说，上面的函数和 generator 仅一步之遥。要把 fib 函数变成 generator ，只需要把 print(b) 改为 yield b 就可以了：
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'
# 这就是定义 generator 的另一种方法。如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个
# generator :
f = fib(6)
print(f)
# 这里，最难理解的就是 generator 和函数的执行流程不一样。函数是顺序执行，遇到 return 语句或者最后
# 一行函数语句就返回。而变成 generator 的函数，在每次调用 next() 的时候执行，遇到 yield 语句返回，
# 再次执行时从上次返回的 yield 语句处继续执行。

# 例子，定义一个 generator ，依次返回数字1,3,5:
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
# 调用该 generator 时，首先要生成一个 generator 对象，然后用 next() 函数不断获得下一个返回值：
o = odd()
print(next(o))
print(next(o))
print(next(o))
# 可以看到， odd 不是普通函数，而是 generator ，在执行过程中，遇到 yield 就中断，下次又继续执行。
# 执行3次 yield 后，已经没有 yield 可以执行了，如果第4次继续调用 next(o) 就会报错。

# 回到 fib 的例子，我们在循环过程中不断调用 yield ，就会不断中断。当然要给循环设置一个条件来退出
# 循环，不然就会产生一个无限数列出来。

# 同样的，把函数改成 generator 后，我们基本上从来不会用 next() 来获取下一个返回值，而是直接使用
# for 循环来迭代：
for n in fib(6):
    print(n)
# 但是用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句的返回值。如果想要拿到
# 返回值，必须捕获 StopIteration 错误，返回值包含在 StopIterarion 的 value 中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# 练习
# 例子，杨辉三角定义如下：
#          1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator,不断输出下一行的list：
def triangles():
    pass
