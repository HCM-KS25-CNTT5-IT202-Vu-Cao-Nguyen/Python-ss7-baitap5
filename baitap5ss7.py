# ==================================
# HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG
# ==================================

raw_batch = (
    " LAP-VN-23-001 ; mou-us-24-012 ; "
    "KEY-vn-23-abc ; lap-JP-22-045 ; "
    "MOn-vn-24-099 "
)


def decode_products():
    products_data = []

    products = raw_batch.split(";")

    for product in products:

        product = product.strip()

        if not product:
            continue

        product = product.upper()

        parts = product.split("-")

        if len(parts) != 4:
            products_data.append(
                {
                    "product_code": "N/A",
                    "country": "N/A",
                    "year": "N/A",
                    "serial": "N/A",
                    "status": "Sai định dạng - Reject"
                }
            )
            continue

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


products_cache = decode_products()

while True:

    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if choice == "1":

        print("\nDỮ LIỆU GỐC:")
        print(raw_batch)

    elif choice == "2":

        valid_count = 0
        total_count = len(products_cache)

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

        for product in products_cache:

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

    elif choice == "3":

        while True:

            search_serial = input(
                "Nhập 2 ký tự cuối của Serial cần tìm: "
            ).strip()

            if len(search_serial) == 2:
                break

            print("Vui lòng nhập đúng 2 ký tự.")

        found = False

        for product in products_cache:

            if product["serial"][-2:] == search_serial.upper():

                print("\nTHÔNG TIN SẢN PHẨM")
                print("MÃ SP:", product["product_code"])
                print("XUẤT XỨ:", product["country"])
                print("NĂM SX:", product["year"])
                print("SERIAL:", product["serial"])
                print("TRẠNG THÁI:", product["status"])

                found = True

        if not found:
            print("Không tìm thấy sản phẩm phù hợp")

    elif choice == "4":

        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break

    else:

        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
