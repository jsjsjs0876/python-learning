# s1 = "hello"
# s2 = "word"
# s3 = "123"
# s4 = "你好"
# s1[0]
# print(s1[-1])
# print(s1[0])
# print(s1[0:4])
# print(s1[:3])
# print(s1[:])
# print(s1[::2])
# print(s1[::-1])

#1. .find() — 从左找，返回索引
# s = "hello world"
# print( s.find("1"))
# print(s.find("l"))
# first_l = s.find("l")
# print(s.find("l", first_l+ 1))
# print(s.find("l"))

#2. .replace() — 替换
# s = "我是个笨蛋"
# s1= s.replace("笨蛋","帅哥 天才")
# s2 = "hello world"
# s3= s2.replace("hello","hi")
# print(s1,s3)

#3. .split() — 切分成列表
# s = "apple banana cheery"
# print (s.split())
# s2 = "s,,b,,c"
# print(s2.split(",",1))


#4.strip() — 去掉两端空格/换行
# s = " hello "
# print(s.strip())
# print(s)

#5. "x".join() — 用x连接列表
# words = ["apple","banana", "cheery"]
# print("和".join(words))
# print(" love ".join(words))

#6. .isdigit() — 是否全数字
# print("123".isdigit())
# print("ssss".isdigit())

# 7. .isalpha() — 是否全字母
# "abc".isalpha()     # True
# "abc123".isalpha()  # False
# "你好".isalpha()    # True（中文也算）

# 8. .isalnum() — 是否全数字或字母（无特殊符号）
# "abc123".isalnum()  # True
# "abc 123".isalnum() # False（有空格）
# "abc!@#".isalnum()  # False（有特殊符号）

#9. .lower() / .upper() — 大小写转换
# "HELLO".lower()
# print("hello".upper())

#六、遍历字符串（用 for 循环）
s = "hello"
for ch in s:
    print(ch)