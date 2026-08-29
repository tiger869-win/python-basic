print("===== XẾP LOẠI HỌC LỰC =====")
diem = float(input("Nhập điểm trung bình: "))
if diem < 5:
    xep_loai = "Yếu" 
elif diem < 6.5:
    xep_loai = "Trung binh"
elif diem < 8:
    xep_loai = "Khá"
elif diem < 9:
    xep_loai = "giỏi"
else:
    xep_loai = "Xuất sắc"
print("Điểm của bạn:", diem)
print("Xếp loại", xep_loai)
                       