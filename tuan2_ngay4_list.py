print("===== LÀM VIỆT VỚI LÍT =====")
# tẠO list
mon_hoc = ["Toán", "Lý", "Hoá", "Văn", "Anh"]
print("Danh sách môn học:", mon_hoc)
print("Môn đầu tiên:", mon_hoc[0])
print("môn cuối cùng:", mon_hoc[-1])
print("Số lượng môn:", len(mon_hoc))
# Thêm môn học
mon_hoc.append("Sinh")
print("\nSau khi thêm Sinh:", mon_hoc)
# Xoá môn học
mon_hoc.remove("Lý")
print("sau khi xoá Lý:", mon_hoc)
# Duyệt list bằng for
print("\nDanh sách môn học hiện tại:")
for mon in mon_hoc:
    print("-", mon)