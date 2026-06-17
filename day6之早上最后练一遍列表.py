raw = "Python入门:39.8,50;数据结构:45.5,30;算法导论:68.0,20;网络爬虫:52.3,0;机器学习:79.9,15"
data = []
for i in raw.split(";"):
    name,price_stock = i.split(":")
    price,stock = price_stock.split(",")
    price = float(price)
    stock = int(stock)
    a = [name]+ [price] + [stock]
    data.append(a)
for i in data:
    print(f"书名：{i[0]},价格：{i[1]}元,剩余{i[2]}本")
min_name = None
max_name = None
max_price = 0
min_price = float("inf")
for i in data:
    if i[1] > max_price:
        max_price = i[1]
        max_name = i[0]
    if i[1] < min_price:
        min_price = i[1] 
        min_name = i[0]  
print(f"最贵的是：{max_name},价格为：{max_price}元")        
print(f"最便宜的是：{min_name},价格为：{min_price}元")
all_stock = []
all_price = []
for s in data:
    all_stock.append(s[2])
    all_price.append(s[2]*s[1])
print(sum(all_price))
print(sum(all_stock))
has_out_of_stock = False  
for n in data:
    if n[2] == 0:
        print(f"{n[0]}没有了")
        has_out_of_stock = True
if has_out_of_stock:
    print("存在缺货图书")
else:
    print("全部都有库存")
add_name,add_stock = input("请输入您要添加的书籍名称以及要添加的数量（请用逗号隔开）").split(",")
found = False
add_stock = int(add_stock)
for i in data:
    if add_name == i[0]:
        i[2] = i[2] + add_stock
        print(f"{i[0]}已添加{add_stock}个，变为{i[2]}个。")
        found = True
        break
if not found:
    print("未找到此书")     
        