# Chương trình thông tin cá nhân nâng cao
ho_ten = input("Nhập họ và tên của ban: ")
nam_sinh = input("Nhập năm sinh: ")
chieu_cao = input("Nhập chiều cao (mét): ")
can_nang = input("Nhập câng nặng (kg): ")
# Chuyển đổi kiểu dữ liệu
nam_sinh = int(nam_sinh)
chieu_cao = float(chieu_cao)
can_nang = float(can_nang)
tuoi = 2026 - nam_sinh
bmi = can_nang / (chieu_cao ** 2)
print("\n===== THÔNG TIN CỦA BẠN =====")
print("Họ và tên:", ho_ten)
print("tuổi:", tuoi)
print("chiều cao:", chieu_cao, "mét")
print("Cân nặng:", can_nang, "kg")
print("Chỉ số BMI:", round(bmi, 2))