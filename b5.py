raw_input = " nGuyen vaN aN ; 2004 "

while True:
    print("====== HỆ THỐNG XỬ LÝ THÀNH VIÊN ======")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=======================================")

    choice = input("Nhập lựa chọn của bạn (1-4):").strip()
    if choice == "1":
        print("\nChuỗi dữ liệu gốc hiện tại:")
        print("'", raw_input, "'")

    elif choice == "2":
        parts = raw_input.split(";")

        if len(parts) == 2:
            full_name = parts[0].strip().title()
            birth_year_str = parts[1].strip()

            birth_year = int(birth_year_str)
            current_age = 2026 - birth_year

            print("\n[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:")
            print("- Họ và tên:", full_name)
            print("- Tuổi hiện tại:", current_age, "tuổi")
            print("\n")

    elif choice == "3":
        parts = raw_input.split(";")

        if len(parts) == 2:
            full_name = parts[0].strip().title()
            birth_year_str = parts[1].strip()

            name_parts = full_name.split()

            if len(name_parts) >= 3:
                last_name = name_parts[0]
                middle_name = name_parts[1]
                first_name = name_parts[2]

                char_1 = last_name[0]
                char_2 = middle_name[0]

                raw_email = char_1 + char_2 + first_name
                generated_email = raw_email.lower() + "@company.com"

                year_suffix = birth_year_str[2:]
                generated_id = first_name.upper() + year_suffix

                print("\n-------------------------------------")
                print("           THÈ THÀNH VIÊN            ")
                print("-------------------------------------")
                print("Họ và tên:    ", full_name)
                print("Mã ID:        ", generated_id)
                print("Email:        ", generated_email)
                print("-------------------------------------\n")

    elif choice == "4":
        print("\nChương trình đã đóng!\n")
        break

    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại!\n")