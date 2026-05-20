print (" --- HỆ THỐNG GỬI EMAIL THƯỜNG TẾT---")

# Vòng Lặp chạy dúng 3 Lần cho 3 nhân viên
for employee_number in range(1, 4):
    print(" --- Đang xử lý nhân vien số", employee_number, " -- ")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input ("Nhập số ngày công trong thang: "))

    # Kiểm tra diều kiện
    if working_days == 0:
        print ("CANH BAO: Nhan vien nghi ca thang. Khong xet duyet thuong.")
        continue

    bonus_amount = working_days * 200000
    print("-> Đã gui Email: Chúc mừng nhận dược", bonus_amount, "VNĐ tiên thưởng!")

print ("Đa hoan tat qua trình duyet thưởng cho 3 nhan viên!")