# str = input("请输入一段字符串")
# if str.isdigit():
#     print("纯数字")
# elif   str.isalpha():
#     print("纯字母")
# elif str.isalnum():
#     print("数字＋字母")
# else:
#     print("包含特殊符号")


# secret = input("请输入你的密码")
# if len(secret) < 6:
#     print("密码怎么跟你一样短，杂鱼~杂鱼~")
# elif secret.isdigit():
#     print("杂鱼~杂鱼~，这密码怎么跟你一样不堪一击")
# elif secret.isalpha():
#     print("怎么只有字母啊，杂鱼~杂鱼~，依旧跟你的功能一样不堪一击呦")
# elif secret.isalnuma():
#     print("哼……别、别以为这样就算赢了！我只是……暂时配合你一下而已！")
# else:
#     print("你犯规了吧，这是什么啊")


s = input("请输入一段话:")
words = s.split()
print(words)
words.reverse()
result = "".join(words)
print(result)