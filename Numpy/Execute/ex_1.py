import numpy as np

# 예시 데이터
data = np.array([23, 12, 45, 67, 34, 89, 22, 65, 44, 55])

# 평균, 표준편차, 최대값, 최소값 계산
mean_val = np.mean(data)
std_val = np.std(data)
max_val = np.max(data)
min_val = np.min(data)

print("평균:", mean_val)
print("표준편차:", std_val)
print("최대값:", max_val)
print("최소값:", min_val)
