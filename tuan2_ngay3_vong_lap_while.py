print("===== ĐẾM TỪ 1 ĐẾN 10 BẰNG WHILE =====")
i = 1
while i <= 10:
    print(i)
    i = i + 1
print("\n===== TRÒ CHƠI ĐOÁN SỐ =====")
so_bi_mat = 7
doan = 0
while doan != so_bi_mat:
    doan = int(input("Đoán một số từ 1 đến 10: "))
    if doan < so_bi_mat:
        print("Bạn đoán thấp quá!")
    elif doan > so_bi_mat:
        print("Bạn đoán cao quá!")
    else:
        print("Chúc mừng bạn đoán đúng rồi!")        