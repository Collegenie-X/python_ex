import numpy as np
# 1D 배열
arr = np.array([1, 2, 3, 4, 5, 6])

# 2D 배열로 reshape
reshaped_arr = arr.reshape(2, 3)  # 2행 3열로 변환
print("2D 배열:\n", reshaped_arr)

# 배열의 전치 (행과 열 바꾸기)
transposed_arr = reshaped_arr.T
print("전치된 배열:\n", transposed_arr)
