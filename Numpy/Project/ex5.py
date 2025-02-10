import numpy as np
from scipy.spatial.distance import cdist

# 예시: 각 창고와 고객의 위치 (x, y 좌표)
warehouses = np.array([[1, 1], [4, 4], [7, 7]])  # 창고 위치
customers = np.array([[2, 3], [5, 6], [8, 8]])   # 고객 위치

# 창고와 고객 간의 유클리디언 거리 계산
distances = cdist(warehouses, customers, metric='euclidean')

# 각 창고에서 가장 가까운 고객 찾기
closest_customers = np.argmin(distances, axis=1)

print("가장 가까운 고객:", closest_customers)
print("각 창고와 고객 간의 거리:\n", distances)
