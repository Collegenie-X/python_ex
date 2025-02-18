# main.py

from products import get_products
from cart import add_to_cart, show_cart
from checkout import checkout

def shopping_program():
    cart = []
    products = get_products()
    
    while True:
        print("\n*** 장바구니 프로그램 ***")
        print("1. 상품 목록 보기")
        print("2. 장바구니에 상품 추가")
        print("3. 장바구니 보기")
        print("4. 결제하기")
        print("5. 종료하기")
        
        user_choice = input("원하는 작업을 선택하세요 (1, 2, 3, 4, 5): ")

        if user_choice == '1':
            print("\n*** 상품 목록 ***")
            for product in products:
                print(f"{product['id']}. {product['name']} - {product['price']} 원")
        elif user_choice == '2':
            try:
                product_id = int(input("장바구니에 추가할 상품 번호를 입력하세요: "))
                add_to_cart(cart, product_id, products)
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
        elif user_choice == '3':
            show_cart(cart)
        elif user_choice == '4':
            checkout(cart)
        elif user_choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

# 프로그램 시작
shopping_program()
