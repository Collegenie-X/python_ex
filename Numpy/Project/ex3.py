import numpy as np

# 예시: 3개의 자산에 대한 수익률 (연간 수익률)
returns = np.array([0.1, 0.15, 0.2])  # 각 자산의 연간 수익률
cov_matrix = np.array([   # 각 자산 간의 공분산 행렬
    [0.005, -0.002, 0.001],
    [-0.002, 0.008, 0.003],
    [0.001, 0.003, 0.010]
])

# 포트폴리오 가중치 (각 자산에 투자하는 비율)
weights = np.array([0.4, 0.4, 0.2])

# 포트폴리오의 기대 수익률
portfolio_return = np.sum(weights * returns)
print("포트폴리오 기대 수익률:", portfolio_return)

# 포트폴리오의 리스크 (표준편차)
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
portfolio_volatility = np.sqrt(portfolio_variance)
print("포트폴리오 리스크 (표준편차):", portfolio_volatility)
