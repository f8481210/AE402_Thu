import random
print('1~20 猜數字')

ans = random.randint(1,20) 
print(ans)
counter = 0 #計算答題次數
while counter <= 5: 
    guess = int(input("猜猜看："))
    counter += 1 
    if guess > ans : 
        print('太大', counter)
    elif guess < ans:
        print('太小', counter)
    else:
        print('答對' , counter)
        break
        
# 1 > 2 > 4 > 5 > 6 > 7 > 9~14 > 6