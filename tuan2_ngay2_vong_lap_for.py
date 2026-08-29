print("===== IN SỐ TỪ 1 ĐẾN 10 =====")
for i in range(1, 11):
    print(i)
print("\n===== TÍNH TỔNG TỪ 1 ĐẾN n =====")
n = int(input("Nhập số n: "))
tong = 0
for i in range(1, n + 1):
    tong = tong + 1
print("tổng từ 1 đến", n, "=", tong)
print("\n===== BẢNG CỨU CHƯƠNG 5 =====")
for i in range(1,11):
    print("5 x", i, "=",5 * i)        