# 상품 목록과 가격 (리스트로 변경)
products = [
    {"id": 1, "name": "상품1", "price": 1000},
    {"id": 2, "name": "상품2", "price": 1500},
    {"id": 3, "name": "상품3", "price": 2500},
    {"id": 4, "name": "상품4", "price": 3000},
    {"id": 5, "name": "상품5", "price": 4000},
    {"id": 6, "name": "상품6", "price": 4500},
    {"id": 7, "name": "상품7", "price": 5500},
]


# 장바구니 추가 (filter 활용)
def add_to_cart(cart, product_id):
    product = next(filter(lambda item: item["id"] == product_id, products), None)
    if product:
        cart.append(product)
        print(f"✅ {product['name']}이(가) 장바구니에 추가되었습니다.")
    else:
        print("⚠ 잘못된 상품 번호입니다. 다시 시도해주세요.")


# 장바구니 출력 (map 활용)
def show_cart(cart):
    if cart:
        print("\n🛒 *** 장바구니 ***")
        cart_items = list(
            map(lambda product: f"{product['name']} - {product['price']} 원", cart)
        )
        print("\n".join(cart_items))
    else:
        print("⚠ 장바구니가 비어 있습니다.")


# 결제 처리 (map 활용)
def checkout(cart):
    if cart:
        total_price = sum(map(lambda item: item["price"], cart))
        print(f"\n💳 결제 금액: {total_price} 원")
        cart.clear()
        print("✅ 결제가 완료되었습니다. 장바구니가 비워졌습니다.")
    else:
        print("⚠ 장바구니에 담긴 상품이 없습니다. 상품을 담아주세요.")


# 프로그램 메인 루프
def shopping_program():
    cart = []
    while True:
        print("\n🛍 *** 장바구니 프로그램 ***")
        print("1. 상품 목록 보기")
        print("2. 장바구니에 상품 추가")
        print("3. 장바구니 보기")
        print("4. 결제하기")
        print("5. 종료하기")

        user_choice = input("원하는 작업을 선택하세요 (1, 2, 3, 4, 5): ")

        if user_choice == "1":
            print("\n📌 *** 상품 목록 ***")
            product_list = list(
                map(lambda p: f"{p['id']}. {p['name']} - {p['price']} 원", products)
            )
            print("\n".join(product_list))

        elif user_choice == "2":
            try:
                product_id = int(input("🛒 장바구니에 추가할 상품 번호를 입력하세요: "))
                add_to_cart(cart, product_id)
            except ValueError:
                print("⚠ 잘못된 입력입니다. 숫자를 입력해주세요.")

        elif user_choice == "3":
            show_cart(cart)

        elif user_choice == "4":
            checkout(cart)

        elif user_choice == "5":
            print("🔚 프로그램을 종료합니다.")
            break

        else:
            print("⚠ 잘못된 선택입니다. 다시 시도해주세요.")


if __name__ == "__main__":
    # 프로그램 시작
    shopping_program()
