# 第3回 おまけ：映画館の料金計算
# 12歳以下=1000 / 13〜18歳=1300 / 19〜59歳=1900 / 60歳以上=1200

print("年齢を入力してください")
nenrei = int(input())

# ここから下を自分で書きます
print("年齢を入力してください")
nenrei = int(input())

if nenrei <= 12:
    ryoukin = 1000
elif nenrei <= 18:
    ryoukin = 1300
elif nenrei <= 59:
    ryoukin = 1900
else:
    ryoukin = 1200

print(f"料金は {ryoukin} 円です")