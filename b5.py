""" 
1.1. Phân tích Input / Output
Input:
    Chuỗi thô cố định: raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-009 " (kiểu dữ liệu: str).
    Lựa chọn menu từ người dùng (1, 2, 3, hoặc 4) (kiểu dữ liệu nhập vào: str).
    Khi dùng chức năng 3: Nhập chuỗi 2 số cuối của Serial cần tìm (kiểu dữ liệu nhập vào: str).
Output:

    Giao diện menu.
    Chức năng 1: In ra chuỗi raw_batch gốc.
    Chức năng 2: Bảng báo cáo kiểm kê được định dạng căn lề đẹp mắt, kèm dòng tổng kết số lượng sản phẩm hợp lệ.
    Chức năng 3: Thông tin chi tiết của sản phẩm tìm thấy hoặc thông báo không tìm thấy.
    Chức năng 4: Thông báo thoát chương trình: "Đóng ca kiểm kho. Chào tạm biệt!".

1.2. Đề xuất giải pháp xử lý dữ liệu
    Tách dữ liệu: Dùng phương thức .split(';') để cắt chuỗi raw_batch thành danh sách các mã sản phẩm thô.
    Làm sạch dữ liệu: Sử dụng .strip() để loại bỏ khoảng trắng thừa ở hai đầu và .upper() để chuẩn hóa thành chữ in hoa.
    Tách thành phần mã: Dùng .split('-') dựa trên dấu gạch ngang để chia thành 4 phần: Mã SP, Mã Quốc Gia, Năm Sản Xuất, Số Serial.
"""
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-009 "

while True:
    print()
    print("===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ")
    user_choice = user_choice.strip()
    
    if user_choice == "1":
        print()
        print("*** Chức năng 1: Hiển thị dữ liệu gốc")
        print("Chuỗi mã vạch gốc:", raw_batch)
        
    elif user_choice == "2":
        print()
        print("*** Chức năng 2: Giải mã và in báo cáo kiểm kê")
        print("MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI")
        print("--------------------------------------------------")
        
        raw_list = raw_batch.split(";")
        total_products = 0
        valid_products = 0
        
        for item in raw_list:
            cleaned_item = item.strip()
            cleaned_item = cleaned_item.upper()
            
            if cleaned_item != "":
                total_products = total_products + 1
                parts = cleaned_item.split("-")
                
                product_code = parts[0]
                country = parts[1]
                manufacture_year = parts[2]
                serial = parts[3]
                
                if serial.isdigit() == True:
                    status = "Pass"
                    valid_products = valid_products + 1
                else:
                    status = "Lỗi Serial - Reject"
                
                full_year = "20" + manufacture_year
                
                print(f"{product_code} | {country} | {full_year} | {serial} | {status}")
                
        print("--------------------------------------------------")
        print(f"Đã giải mã thành công {valid_products} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")

    elif user_choice == "3":
        print()
        print("*** Chức năng 3: Tra cứu theo đuôi Serial")
        search_input = input("Người dùng nhập 2 số cuối của Serial cần tìm: ")
        cleaned_search = search_input.strip()
        
        raw_list = raw_batch.split(";")
        is_found = False
        
        for item in raw_list:
            cleaned_item = item.strip()
            cleaned_item = cleaned_item.upper()
            
            if cleaned_item != "":
                parts = cleaned_item.split("-")
                product_code = parts[0]
                country = parts[1]
                manufacture_year = parts[2]
                serial = parts[3]
                
                if serial.isdigit() == True:
                    length = len(serial)
                    last_two_digits = serial[length-2 : length]
                    
                    if last_two_digits == cleaned_search:
                        full_year = "20" + manufacture_year
                        print(f"[Tìm thấy] Sản phẩm: {product_code} | Quốc gia: {country} | Năm SX: {full_year} | Serial: {serial}")
                        is_found = True
                        
        if is_found == False:
            print("Thông báo: không tìm thấy sản phẩm phù hợp")

    elif user_choice == "4":
        print()
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break
        
    else:
        print()
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
