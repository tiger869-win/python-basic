def thong_tin(ho_ten, tuoi, thanh_pho):
    print("Ho ten:", ho_ten)
    print("Tuổi:", tuoi)
    print("Thành phố:", thanh_pho)
    print("-" * 30)
thong_tin("Lê văn Đấu", 40, "Hà Nội")
thong_tin("Nguyễn Văn A", 25, "TP.HCM")
def chao_hoi(ten, loi_chao="Xin chào"):
    print(loi_chao + ",", ten + "!")
chao_hoi("Đấu")
chao_hoi("Đấu", "Good morning")
chao_hoi("Python", "Hello")
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao ** 2)
    return round(bmi, 2)
bmi1 = tinh_bmi(85, 1.65)
bmi2 = tinh_bmi(70, 1.75)
print("BMI 1 =", bmi1)
print("BMI 2 =", bmi2)  