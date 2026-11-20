# 第3回 課題：BMI計算機
# BMI = 体重(kg) / 身長(m) ** 2

# --- Lv.1 【必須】60点 ---
print("身長を入力してください（m）")
shincho = float(input())

print("体重を入力してください(kg)")
taiju=float(input())

bmi=taiju / (shincho ** 2)
print(f"BMIは {bmi:.1f} です")
# ここから下を自分で書きます
# 1. 体重を聞く（float に変換するのを忘れずに）
# 2. BMI を計算する
# 3. 小数第1位まで表示する   →  f"BMIは {bmi:.1f} です"


# --- Lv.2 【標準】+20点 ---
# BMI から判定を出す（18.5未満=やせ / 25未満=標準 / それ以上=肥満）
# 条件は「狭いほう（小さいほう）」から順に書くこと
if bmi < 18.5:
    print("判定: やせ")
elif bmi < 25:
    print("判定: 標準")
else:
    print("判定: 肥満")

# --- Lv.3 【挑戦】+20点 ---
# 身長を cm で入力できるようにする
# BMI 22 のときの体重（目標体重）と、今の体重との差を表示する


shincho = float(input("身長を入力してください（cm）"))
taiju = float(input("体重を入力してください（kg）"))

shincho_m = shincho / 100

bmi = taiju / (shincho_m ** 2)

print(f"BMI は {bmi:.1f} です")

if bmi < 18.5:
    print("判定：やせ")
elif bmi < 25:
    print("判定：標準")
else:
    print("判定：肥満")

mokuhyo_taiju = 22 * (shincho_m ** 2)
sa = mokuhyo_taiju - taiju

print(f"目標体重は {mokuhyo_taiju:.1f} kg です（あと {sa:.1f} kg）")