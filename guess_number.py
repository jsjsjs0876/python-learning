import random

secret = random.randint(1, 100)
chances = 7
count = 0

print("我已经想好了1-100之间的数，你有7次机会")

while chances > 0:
    guess = int(input("猜猜数字："))
    count = count + 1
    
    if guess == secret:
        print(f"猜中了，恭喜你,就是{guess}")
        break
    elif guess < secret:
        print("小了")
        chances -= 1
    elif guess > secret:
        print("大了")
        chances -=1

else:
    print("机会用完了，正确答案是", secret)