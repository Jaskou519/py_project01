# 获取键盘上输入的数据 -- input(...)
name = input("请输入您的姓名: ")
age = input("请输入您的年龄: ")

print(f"您的姓名是 {name} , 年龄为: {age}")


# 案例: 银行卡ATM取款
# 总金额
total = 10000

# 1. 输入密码
password = input("请输入您的银行卡密码: ")
print(f"密码正确, {password}")

# 2. 输入取款金额
num = input("请输入您的取款金额: ")

# 3. 计算余额并输出 --> num 转为 int类型 ---> int(..)
print(f"取款后银行卡余额为: {total - int(num)}")


# 案例：简单计算器
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2

print(add, sub, mul)