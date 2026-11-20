# # # # # #練習1：whileの形
# # # # # zandaka=900
# # # # # while zandaka>0:
# # # # #     print(zandaka)
# # # # #     zandaka=zandaka-300
# # # # # print("払い終わった")

# # # # kaisu=5

# # # # while kaisu>0:
# # # #     print(kaisu)
# # # #     kaisu=kaisu-2

# # # # print("発射")    


# # # kaisu=10

# # # # while kaisu>0:
# # # #     print(kaisu)
# # # #     kaisu=kaisu-2

# # # # print("スタート")    

# # # # for i in range (1,11):
# # # #     if i == 4:
# # # #         break
# # # #     print(i)

# # # # while True:
# # # #     kotoba = input()
# # # #     if kotoba == "おわり":
# # # #         break
# # # #     print(kotoba)

# # # kaisu=0
# # # while True:
# # #     kaisu =kaisu +1 
# # #     print(kaisu)
# # #     if kaisu==3:
# # #         break
# # # print("おわり")    


# # # for i in range(1,6):
# # #     if i ==3:
# # #         continue
# # #     print(i)

# # goukei=0
# # while True:
# #     n= int(input())
# #     if n ==0:
# #         break
# #     goukei=goukei+n
# # print(goukei)

# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)


while True:
    n=int(input())
    if n ==0:
        break
    if n % 2==0:
        print(n,"は偶数")
    else:
        print(n,"は奇数")