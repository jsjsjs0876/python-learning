"""
拼尽全力
无法战胜
"""
# score = [["张三",85,92,78],["李四",88,76,95],["王五",90,84,79],["赵六",60,65,70]]
# sc = score.split()
# score = "张三:85,92,78;李四:88,76,95;王五:90,84,79;赵六:60,65,70"
# sc = score.split(";")
# students = []
# for student in sc:
#     name,score_str = student.split(":")
#     scores = (int(b) for b in score_str.split(","))
#     result = [name + scores]    
#     print(result)    

#任务一
# a = "张三-13812345678,李四-13912345678,王五-13712345678"
# b = a.split(",")
# result = []
# for x in b:
#      name,phone = x.split("-")
#      result.append([name,phone])
# r = "|".join([f"姓名：{name},电话：{phone}" for name,phone in result])
# print(r)

#任务二
# scores = [85, 42, 78, 90, 55, 88, 61, 39]
# jige = [x for x in scores if x >=60]
# no_jige = [x for x in scores if x <60]
# av = [sum(scores)/len(scores) for x in scores]
# print(av)
# s = int(input("输入数字，看看它在不在里面:"))
# if s in (x for x in scores):
#     print("在的呢")
# else:
#     print("不在")
# for i in range(3):
#     num = int(input(f"添加第{i+1}个数据:"))
#     scores.append(num)
# print(scores)


#任务三
# students = [
#     ["张三", [85, 92, 78]],
#     ["李四", [88, 76, 95]],
#     ["王五", [90, 84, 79]],
#     ["赵六", [60, 65, 70]]
# ]
# max_total = -1
# max_name = ""
# max_score = []
# for x in students:
#     name = x[0]
#     score = x[1]
#     average = sum(score) // len(score)
#     total = sum(score)
#     print(f"{name}:总分:{total}，平均分{average}")
#     if total > max_total:
#         max_total = total
#         max_name = name
#         max_score = score 
# print(f"the score max student is{max_name},he get {max_total} points")
# print(f"and he all subject points is{max_score}")

#拼尽全力，这次一定可以
# raw_data = "张三:85,92,78;李四:88,76,95;王五:90,84,79;赵六:60,65,70;孙七:55,58,62"
# data = raw_data.split(";")
# new_data = data[1]
# result = []
# for i in data:
#     name,score = i.split(":")
#     scores = [int(s) for s in score.split(",")]
#     total = sum(scores)
#     av = round(total/len(scores))
#     result.append([name,av])
# print("学生平均分:",result)
# all_scores = []
# all_name = []    
# for a in data:
#     name,score = a.split(":")
#     scores = [int(s) for s in score.split(",")]
#     all_scores.extend(scores)
#     all_name.append(name)
# print(all_name)
# name_scores = []
# for n in data:
#      name,score = n.split(":")
#      scores = [int(s) for s in score.split(",")]
#      for s in scores:
#           name_scores.append([name,s])
           
# max_score = all_scores[0]
# min_score = all_scores[0]
# max_name = all_name[0]
# for i in all_scores:
#         if i > max_score:
#             max_score = i
#         # print(max_score)
#         if i < min_score:
#             min_score = i
# print(f"最高{max_score}")
# print(f"最低{min_score}")
