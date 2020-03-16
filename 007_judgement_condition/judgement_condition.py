# 条件判断 ，计算机之所以能做很多自动化的任务，因为它可以自己做条件判断
# python程序中 ， 用if语句实现条件判断 if+条件
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

# python缩进规则，如果 if 语句判断是True ， 就执行缩进的语句块，否则，什么都不做
# 也可以给 if 添加一个 else 语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# 可以在if...else语句中加入 elif 做更细致的判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式如下
# if <条件判断1>:
#    <执行1>
# elif <条件判断2>:
#      <执行2>
# elif <条件判断3>:
#      <执行3>
# else:
#      <执行4>
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age>=6:
    print('teenager')
elif age >=18:
    print('adult')
else:
    print('kid')

# if 判断条件还可以简写
#if x:
#    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False

# input()函数返回的数据是str类型，str不能直接和int做对比较，如需做比较，需要先把srt转成int
s = input('birth:')
birth = int(s)
if birth <= 2000:
    print('00前')
else:
    print('00后')

# int()函数如果接收到的是字符串，而不是合法的数字时，就会报错，程序就会退出
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖
high = input('请输入你的身高：')
wight = input('请输入你的体重')
h = float(high)
w = int(wight)
bmi = w/(h*h)
if bmi > 32:
    print('严重过胖')
elif 32 <= bmi >= 28:
    print('肥胖')
elif 28 <= bmi >= 25:
    print('过重')
elif 25 <= bmi >= 18.5:
    print('正常')
else:
    print('过轻')
