# ==================================
# HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG
# ==================================

raw_batch = (
    " LAP-VN-23-001 ; mou-us-24-012 ; "
    "KEY-vn-23-abc ; lap-JP-22-045 ; "
    "MOn-vn-24-099 "
)


def decode_products():
    """
    Trả về danh sách sản phẩm đã chuẩn hóa
    """
    products_data = []

    products = raw_batch.split(";")

    for product in products:

        product = product.strip().upper()

        parts = product.split("-")

        product_code = parts[0]
        country = parts[1]
        year = "20" + parts[2]
        serial = parts[3]

        if serial.isdigit():
            status = "Pass"
        else:
            status = "Lỗi Serial - Reject"

        products_data.append(
            {
                "product_code": product_code,
                "country": country,
                "year": year,
                "serial": serial,
                "status": status
            }
        )

    return products_data


while True:

    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    # Chức năng 1
    if choice == "1":
        print("\nDỮ LIỆU GỐC:")
        print(raw_batch)

    # Chức năng 2
    elif choice == "2":

        products = decode_products()

        valid_count = 0
        total_count = len(products)

        print("\nBÁO CÁO KIỂM KÊ")
        print("-" * 70)

        print(
            f"{'MÃ SP':<10}"
            f"{'XUẤT XỨ':<10}"
            f"{'NĂM SX':<10}"
            f"{'SERIAL':<10}"
            f"{'TRẠNG THÁI'}"
        )

        print("-" * 70)

        for product in products:

            if product["status"] == "Pass":
                valid_count += 1

            print(
                f"{product['product_code']:<10}"
                f"{product['country']:<10}"
                f"{product['year']:<10}"
                f"{product['serial']:<10}"
                f"{product['status']}"
            )

        print("-" * 70)
        print(
            f"Đã giải mã thành công {valid_count} sản phẩm hợp lệ / "
            f"Tổng số {total_count} sản phẩm."
        )

    # Chức năng 3
    elif choice == "3":

        search_serial = input(
            "Nhập 2 số cuối của Serial cần tìm: "
        ).strip()

        products = decode_products()

        found = False

        for product in products:

            if product["serial"][-2:] == search_serial:

                print("\nTHÔNG TIN SẢN PHẨM")
                print("MÃ SP:", product["product_code"])
                print("XUẤT XỨ:", product["country"])
                print("NĂM SX:", product["year"])
                print("SERIAL:", product["serial"])
                print("TRẠNG THÁI:", product["status"])

                found = True

        if not found:
            print("Không tìm thấy sản phẩm phù hợp")

    # Chức năng 4
    elif choice == "4":
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break

    # Edge Case nhập sai menu
    else:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")