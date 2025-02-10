import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 예시: 고객 데이터 (나이, 연간 지출)
customer_data = np.array([
    [25, 2000],
    [45, 4000],
    [35, 3000],
    [50, 5000],
    [23, 1800],
    [30, 2400],
    [60, 6000]
])

# KMeans 클러스터링
kmeans = KMeans(n_clusters=2, random_state=0).fit(customer_data)

# 클러스터링 결과 출력
print("클러스터 레이블:", kmeans.labels_)

# 클러스터의 중심
print("클러스터 중심:", kmeans.cluster_centers_)

# 클러스터 시각화
plt.scatter(customer_data[:, 0], customer_data[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='x')
plt.xlabel("Age")
plt.ylabel("Annual Spend")
plt.title("Customer Segmentation")
plt.show()
