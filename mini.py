import time
qty_laptop = 0
qty_phone = 0
qty_tablet = 0
LINE = "="*30
while True:
    print("=== MENU === \n")
    print(
        "1. Xem báo cáo tồn kho \n"
        "2. Nhập kho \n"
        "3. Xuất kho \n"
        "4. Cảnh cáo hàng tồn kho thấp \n"
        "5. Thoát chương trình"
    )
    choose = int(input("Vui lòng nhập lựa chọn của bạn (1 -  5): "))
    match choose:
        case 1:
            print(LINE)
            print("\n=== Hệ thống sản phẩm ===")
            print(
                f"Laptop (Tồn kho: {qty_laptop}): {qty_laptop * "*"} \n"
                f"Điện thoại (Tồn kho: {qty_phone}): {qty_phone * "*"} \n"
                f"Máy tính bảng (Tồn kho: {qty_tablet}): {qty_tablet * "*"} \n"
            )
            print(LINE)
        case 2:
            wanna_to_up_item = int(input(
                "\nBạn muốn nhập hàng nào ! \n"
                "1 - Laptop \n"
                "2 - Phone \n"
                "3 - Tablet \n"
                "Lựa chọn của bạn: "
            ))
            match wanna_to_up_item:
                case 1:
                    while True:
                        qty_laptop_up = int(input("Vui lòng nhập số lượng laptop mà bạn muốn nhập: "))

                        if (qty_laptop_up < 0):
                            print("Số lượng không hợp lệ, vui lòng nhập lại !")
                            continue 
                        
                        qty_laptop +=  qty_laptop_up
                        print(f"Đã thêm được {qty_laptop_up} Laptop \n")
                        break
                case 2:
                    while True:
                        qty_phone_up = int(input("Vui lòng nhập số lượng Phone mà bạn muốn nhập: "))

                        if (qty_phone_up < 0):
                            print("Số lượng không hợp lệ, vui lòng nhập lại !")
                            continue 
                        
                        qty_phone +=  qty_phone_up
                        print(f"Đã thêm được {qty_phone_up} Phone \n")
                        break
                case 3:
                    while True:
                        qty_tablet_up = int(input("Vui lòng nhập số lượng Phone mà bạn muốn nhập: "))

                        if (qty_tablet_up < 0):
                            print("Số lượng không hợp lệ, vui lòng nhập lại !")
                            continue 
                        
                        qty_tablet +=  qty_tablet_up
                        print(f"Đã thêm được {qty_tablet_up} Tablet \n")
                        break
                case _:
                    print("Số bạn không hợp lệ ! sẽ thoát khỏi chức năng này !")
                    
        case 3:
            wanna_to_down_item = int(input(
                "\nBạn muốn xuất hàng nào ! \n"
                "1 - Laptop \n"
                "2 - Phone \n"
                "3 - Tablet \n"
                "Lựa chọn của bạn: "
            ))
            match wanna_to_down_item:
                case 1:
                    while True:
                        qty_laptop_down = int(input("Vui lòng nhập số lượng laptop mà bạn muốn nhập: "))

                        if (qty_laptop_down > qty_laptop):
                            print("Số lượng không hợp lệ, sẽ hủy giao dịch !")
                            break
                        
                        qty_laptop -=  qty_laptop_down
                        print(f"Đã xuất được {qty_laptop_down} Laptop \n")
                        break
                case 2:
                    while True:
                        qty_phone_down = int(input("Vui lòng nhập số lượng Phone mà bạn muốn nhập: "))

                        if (qty_phone_down > qty_phone):
                            print("Số lượng không hợp lệ, sẽ hủy giao dịch !")
                            break
                        
                        qty_phone -=  qty_phone_down
                        print(f"Đã xuất được {qty_phone_down} Phone \n")
                        break
                case 3:
                    while True:
                        qty_tablet_down = int(input("Vui lòng nhập số lượng Phone mà bạn muốn nhập: "))

                        if (qty_tablet_down > qty_tablet):
                            print("Số lượng không hợp lệ, sẽ hủy giao dịch !")
                            break
                        
                        qty_tablet -=  qty_tablet_down
                        print(f"Đã xuất được {qty_tablet_down} Tablet \n")
                        break
                case _:
                    print("Số bạn không hợp lệ ! sẽ thoát khỏi chức năng này !")
        case 4:
            print(LINE)
            print("=== HỆ THỐNG CẢNH CÁO TỒN KHO THẤP === \n")
            if(qty_laptop < 10):
                print(f"[CẢNH CÁO] Mặt hàng Laptop sắp hết (Chỉ còn {qty_laptop}) \n")
            if(qty_phone < 10 ):
                print(f"[CẢNH CÁO] Mặt hàng Phone sắp hết (Chỉ còn {qty_phone}) \n")
            if(qty_tablet < 10 ):
                print(f"[CẢNH CÁO] Mặt hàng Tablet sắp hết (Chỉ còn {qty_tablet}) \n")
            print(LINE)
            print()
        case 5:
            goodbye = "Cảm ơn vì đã sử dụng chương trình !"
            for letter in goodbye:
                print(letter, end = "", flush = True)
                time.sleep(0.05)
            break
        case _:
            print("Lựa chọn không hợp lệ :)")