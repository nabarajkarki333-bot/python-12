# 第5回 課題：数当てゲーム
import random

kotae = random.randint(1, 100)

print("1から100の数を当ててください")

# --- Lv.1 【必須】60点 ---
# while で当たるまでくり返します。
# input() は文字列なので int() で変換するのを忘れずに。
# 当たったら break で終わります。
while True :
    kotae_input =int(input())
    if kotae_input < kotae:
        print("もっと大きい")
    elif kotae_input > kotae:
        print("もっと小さい")
    else:
        print("正解")
        break

# --- Lv.2 【標準】+20点 ---
# 何回目で当たったかを数えて表示する
import random

kotae = random.randint(1, 100)

print("1から100の数を当ててください")
count = 0
while True :
    kotae_input =int(input())
    count += 1
    if kotae_input < kotae:
        print("もっと大きい")
    elif kotae_input > kotae:
        print("もっと小さい")
    else:
        print(f"{count}回で正解!")
        break





# --- Lv.3 【挑戦】+20点 ---
# 10回までの制限をつける。超えたら答えを表示して終了
import random
from random import randint


kotae = randint(1, 100)
print("1から100の数を当ててください")

count = 0
while count < 10:                       
    kotae_input = int(input())
    count += 1
    if kotae_input < kotae:
        print("もっと大きい")
    elif kotae_input > kotae:
        print("もっと小さい")
    else:
        print(f"{count}回で正解！")
        break

if kotae_input != kotae:                
    print(f"残念、答えは{kotae}でした")