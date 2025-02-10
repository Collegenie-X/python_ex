# 예시 데이터
import numpy as np

arr = np.array([12, 56, 43, 87, 24, 67, 99])

# 50보다 큰 값만 선택
filtered_arr = arr[arr > 50]
print("50보다 큰 값들:", filtered_arr)
