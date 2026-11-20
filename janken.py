# 第5回 おまけ：じゃんけんゲーム（3回勝負）
import random

# 1 = グー, 2 = チョキ, 3 = パー
print("じゃんけん！ 1=グー 2=チョキ 3=パー")

# ここから自分で書きます
for i in range(3):
    you = int(input("あなたの手は？ "))
    cpu = random.randint(1, 3)
    print("コンピュータ:", cpu)

    if you == cpu:
        print("あいこ")
    elif you == 1 and cpu == 2:
        print("勝ち！")
        win += 1
    elif you == 2 and cpu == 3:
        print("勝ち！")
        win += 1
    elif you == 3 and cpu == 1:
        print("勝ち！")
        win += 1
    else:
        print("負け")

print(win, "勝しました")