print("===== CHƯƠNG TRÌNH QUẢN LÝ CÔNG VIỆC =====")

cong_viec = ["Học Python", "Làm bài tập", "Đọc sách"]

while True:
    print("\n----- MENU -----")
    print("1. Xem danh sách công việc")
    print("2. Thêm công việc")
    print("3. Xóa công việc")
    print("4. Thoát")
    
    chon = input("Chọn chức năng (1-4): ")
    
    if chon == "1":
        print("\nDanh sách công việc:")
        if len(cong_viec) == 0:
            print("Chưa có công việc nào.")
        else:
            for i, viec in enumerate(cong_viec, 1):
                print(i, ".", viec)
    
    elif chon == "2":
        moi = input("Nhập công việc mới: ")
        cong_viec.append(moi)
        print("Đã thêm thành công!")
    
    elif chon == "3":
        if len(cong_viec) == 0:
            print("Danh sách trống, không thể xóa.")
        else:
            for i, viec in enumerate(cong_viec, 1):
                print(i, ".", viec)
            so = int(input("Nhập số thứ tự muốn xóa: "))
            if 1 <= so <= len(cong_viec):
                da_xoa = cong_viec.pop(so - 1)
                print("Đã xóa:", da_xoa)
            else:
                print("Số thứ tự không hợp lệ.")
    
    elif chon == "4":
        print("Tạm biệt!")
        break
    
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")