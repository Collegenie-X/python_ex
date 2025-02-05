products = [
    {"id": 1, "name": "상품 1", "price":1000},
    {"id": 2, "name": "상품 2", "price":2000},
    {"id": 3, "name": "상품 3", "price":3000},
    {"id": 4, "name": "상품 4", "price":4000},
    {"id": 5, "name": "상품 5", "price":5000},
    {"id": 6, "name": "상품 6", "price":6000},
    {"id": 7, "name": "상품 7", "price":7000},
]

carts = []

product = next(item for item in products if item['id'] ==1)
carts.append(product) 

total_price = sum (item['price'] for item in products)
print("total_price:", total_price)

print("carts:",carts)