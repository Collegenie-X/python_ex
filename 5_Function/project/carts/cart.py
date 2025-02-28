# cart.py

def add_to_cart(cart, product_id, products):
    try:
        product = next(item for item in products if item["id"] == product_id)
        cart.append(product)
        print(f"{product['name']}이(가) 장바구니에 추가되었습니다.")
    except StopIteration:
        print("잘못된 상품 번호입니다. 다시 시도해주세요.")

def show_cart(cart):
    if cart:
        print("\n*** 장바구니 ***")
        for product in cart:
            print(f"{product['name']} - {product['price']} 원")
    else:
        print("장바구니가 비어 있습니다.")
