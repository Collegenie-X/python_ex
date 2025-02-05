# checkout.py

def checkout(cart):
    if cart:
        total_price = sum(item['price'] for item in cart)
        print(f"결제 금액: {total_price} 원")
        cart.clear()
        print("결제가 완료되었습니다. 장바구니가 비워졌습니다.")
    else:
        print("장바구니에 담긴 상품이 없습니다. 상품을 담아주세요.")
