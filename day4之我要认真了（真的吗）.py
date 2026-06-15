#任务一

# test_name = input("请输入你的名称")
# user_name = test_name.strip()
# if not user_name:
#     print("用户名不能为空")
# elif 3<=  len(user_name) <=10  and user_name.isalnum():
#     print("用户名有效")
# else:
#     print("请重新输入，要求在长度3-10之间")

# 任务二
# cs = ["SB", "笨蛋", "白痴", "傻瓜"]
# 话 = input("请输入一句话：")
# total = 0

# for 词 in cs:
#     times = 话.count(词)
#     total += times
#     话 = 话.replace(词, "***")

# print(话)
# print(f"共替换{total}处")

#任务三(有点小问题)
# id_card = input("请输入您的身份证号码")
# if len(id_card) != 18:
#     print("长度错误")
# else:
#     first_17 = id_card[:17]
#     end_char = id_card[-1]
#     if not first_17.isdigit():
#         print("输入有误,前十七位仅包含数字")
#     elif not (end_char.isdigit() or end_char !="X"):
#         print("请确保您的最后一位是正确的")
#     else:
#         print("正确的")
# brithday = id_card[6:14]
# print(f"您的生日是{brithday[0:4]}年.{brithday[4:6]}月,{brithday[6:8]}日")
# sex = id_card[-2]
# sex_int = int(sex)
# if sex_int%2 ==0:
#     print("您为女性")
# else:
#     print("您为男性")
# id = id_card[0:6] + "********" + id_card[-4:]  
# print(id)

# 任务三（完全正确版）
# id_card = input("请输入您的身份证号码：")

# if len(id_card) != 18:
#     print("长度错误")
# else:
#     first_17 = id_card[:17]
#     end_char = id_card[-1]
    
#     if not first_17.isdigit():
#         print("输入有误，前十七位仅包含数字")
#     elif not (end_char.isdigit() or end_char == "X"):
#         print("请确保您的最后一位是正确的")
#     else:
#         print("正确的")
        
#         birthday = id_card[6:14]
#         print(f"您的生日是{birthday[0:4]}年{birthday[4:6]}月{birthday[6:8]}日")
        
#         sex = id_card[-2]
#         sex_int = int(sex)
#         if sex_int % 2 == 0:
#             print("您为女性")
#         else:
#             print("您为男性")
        
#         id_hidden = id_card[0:6] + "********" + id_card[-4:]
#         print(id_hidden)