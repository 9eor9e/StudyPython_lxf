# python的循环有两种,for...in循环和while循环
# for...in循环，依次把list或tuple中的每个元素 迭代 出来,执行以下代码，会依次打印list中每个元素
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
# 所以for x in ...循环就是把每个元素带入变量x，然后执行缩进块的语句

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

# python提供range()函数，可以生成一个整数序列,range(5)能生成[0,1,2,3,4]
a = list(range(5))
print(a)

# range(101)可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环，只要条件满足，就不断循环，条件不满足时推出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)

# 练习
L = ['Bart','Lisa','Adam']
for x in L:
    print('Hello, ' + x + ' !')

# 在循环中，break语句可以提前退出循环
n =1
while n <= 100:
    print(n)
    n = n + 1
print('END')
# 使用break语句的效果
n = 1
while n <= 100:
    if n > 10: # 当n=11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 在循环中，可以通过continue语句，跳过当前的这次循环，直接开始下一轮循环
n = 0
while n < 10:
    n = n + 1
    print(n)
# 使用continue语句的效果
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# 循环是让计算机做重复任务的有效的方法
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
# 这两个语句通常都必须配合if语句使用。
# 不要滥用break和continue语句，break和continue会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句。