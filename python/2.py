temp = input("玲儿猜猜我心里想的是什么数字?")
guess = int(temp)
while guess != 8:
    temp = input("错了哦，再试一试吧：")
    guess = int(temp)
    if guess == 8:
        print("猜对了呢，玲儿")
    else:
        if guess > 8:
            print("大了哦")
        else:
            print("小了哦")
print("再见了，玲儿.")          
      
      
