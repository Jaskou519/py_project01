# 字面量
print(98)  # 整数(int)
print(3.14)  # 浮点数(float)
print(True)  # 布尔(bool)
print(False)  # 布尔(bool)
print("Hello Python")  # 字符串(str)
print(None)  # 空值(NoneType)

# 布尔类型本质也是整数类型（True + 1，False - 1）
print(True + 1)  # 2
print(False - 1)  # -1



# 变量 ----> Python是动态类型语言，一个变量可以存储不同的数据类型（但是项目开发中，推荐变量只存储一种类型的数据）
num = 134.15926
print(num)

num += 1
print(num)

num = "OK"
print(num)

num = True
print(num)



# 案例-------某视频基础播放量为20.7万，每月新增播放量为50万，请输出未来第n个月的播放总量
base,insr = 20.7,50

n = int(input("请输入未来第几个月："))    # input() 拿到的是字符串（str），必须用 int() 转成数字才能做乘法运算

print(f"未来第{n}个月的播放总量为{base + insr * n}万")    # f 前缀：告诉Python，这个字符串里的 {} 花括号不是普通字符，而是变量占位符，需要把变量的值填进去。



# 变量交换-------将两个变量值交换
a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)
