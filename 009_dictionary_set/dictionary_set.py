# python内置了字典，在其他语言中也称map，使用键-值（key-value）存储，具有极快的查找速度
# dict(dictionary) , 使用 {key1:value1,key2:value2,...keyN:valueN} 表示
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

# dict查找速度快，因为dict的实现原理和查字典一样，给定一个名字，dict在内部就可以直接计算出该名字对应的存放的元素
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# 如果key不存在，dict就会报错！
# 要避免key不存在的错误，有两种办法，一是通过 in 判断key是否存在
'Thomas' in d
# 二是通过dict提供的 get() 方法，如果key不存在，可以返回 None
print(d.get('Thomas'))
# 或者自己指定value
print(d.get('Thomas',-1))
# 注意，返回 None 的时候python的交互环境不显示结果！

# 要删除一个key，用 pop(key) 方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较，dict有以下几个特点：
# 1.查找和插入的速度极快，不会随着key的增加而变慢
# 2.需要占用大量的内存，内存浪费多
# 而list的特点正好相反：
# 1.查找和插入速度随着元素的增加而增加
# 2.占用空间小，浪费内存很少
# 所以，dict是空间来换取时间的一种方法
# dict可以用在需要高速查找的很多地方，在python代码中几乎无处不在，正确使用dict非常重要，
# 需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash),要保证hash的正确性，作为key的对象就不能变。
# 在python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key

# set ，和dict类似，也是一组key的集合，但不存储value。所以set中，没有重复的key
s = set([1,2,3])
print(s)
# 注意，传入的参数[1,2,3]是一个list，而显示的{1,2,3}只是告诉你这个set内部有1，2，3这三个元素，
# 显示的顺序也不表示set是有序的。
# 重复元素在set中自动被过滤
s = set([1,1,2,2,3,3])
print(s)
# 通过 add(key) 方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)

# 通过 remove(key) 方法可以删除元素
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# str是不变对象，而list是可变对象
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c','b','a']
a.sort()
print(a)
# 而对于不可变对象，比如str，对str进行操作
a = 'abc'
print(a.replace('a','A'))
print(a)
# 虽然字符串有个 replace() 方法，但变量 a 最后仍是 'abc'
a = 'abc'
b = a.replace('a','A')
print(b)
print(a)
# 要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，
# a本身是一个变量，它指向的对象的内容才是'abc'
# 当我们调用 a.replace('a','A') 时，实际上调用方法replace是作用在字符串对象'abc’上的，而这个方法虽然名字
# 叫做 replace ，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用
# 变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串‘Abc'了
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象
# 并返回，这样，就保证了不可变对象本身永远是不可变的。

# 使用key-value存储结构的dict在python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

# 例如，tuple虽然是不变对象，但试试把（1，2，3）和（1，[2,3])放入dict或set中，并解释结果。
