print("===== TÍNH CHU VI & DIỆN TÍCH HÌNH CHỮ NHẬT =====")
chieu_dai = float(input("Nhập chiều dài (m): "))
chieu_rong = float(input("Nhập chiều rộng (m): "))
chu_vi = (chieu_dai + chieu_rong) * 2
dien_tich = chieu_dai * chieu_rong
print("\nkết quả:")
print("Chu vi =", chu_vi, "mét")
print("Diện tích =", dien_tich, "mét vuông")
print("\n===== ĐỔI TIỀN USD -> VND =====")
usd = float(input("Nhập số tiền USD: "))
ty_gia = 25000
vnd = usd * ty_gia
print(usd, "USD =", vnd, "VND")