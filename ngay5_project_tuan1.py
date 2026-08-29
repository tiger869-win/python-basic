print("===== HỒ SƠ CÁ NHÂN + ĐÁNH GIÁ BMI =====")
#Nhập thông tin
ho_ten = input("Nhập họ tên: ")
nam_sinh = int(input("Nhập năm sinh: "))
chieu_cao = float(input("Nhập chiều cao (mét): "))
can_nang = float(input("Nhập cân nặng (kg): "))
# Tính toán
tuoi = 2026 - nam_sinh
bmi = can_nang / (chieu_cao ** 2)
# Đánh giá BMI
if bmi < 18.5:
   danh_gia = "Gầy"
elif bmi < 25:
   danh_gia = "Bình thường"
elif bmi < 30:
   danh_gia = "thừa cân"
else:
   danh_gia = "Béo phì"
# In kết quả
print("\n" + "="*40)
print("HỌ VÀ TÊN      :", ho_ten.upper())
print("TUỔI           :", tuoi)
print("CHIỀU CAO      :", chieu_cao, "mét")
print("CÂN NẶNG       :", can_nang, "kg") 
print("CHỈ SỐ BMI     :", round(bmi, 2))
print("ĐÁNH GIÁ       :", danh_gia)
print("="*40)                 