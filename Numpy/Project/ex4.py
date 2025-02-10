import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 예시: 월별 광고비와 매출
ad_spend = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)  # 광고비
sales = np.array([12, 24, 35, 46, 58])  # 매출

# 선형 회귀 모델 학습
model = LinearRegression()
model.fit(ad_spend, sales)

# 예측
predictions = model.predict(ad_spend)

# 시각화
plt.scatter(ad_spend, sales, color='blue', label='실제 데이터')
plt.plot(ad_spend, predictions, color='red', label='예측 직선')
plt.xlabel('광고비')
plt.ylabel('매출')
plt.title('광고비와 매출의 관계')
plt.legend()
plt.show()

print("예측된 매출:", predictions)
