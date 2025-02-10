import numpy as np
import matplotlib.pyplot as plt

# 예시: 10x10 크기의 단순 이미지 생성 (0~255 값)
image = np.random.randint(0, 256, (10, 10))

# 이미지 표시
plt.imshow(image, cmap='gray', interpolation='nearest')
plt.title("Random Image")
plt.show()

# 이미지에 노이즈 추가
noise = np.random.normal(0, 20, image.shape)  # 평균 0, 표준편차 20인 노이즈
noisy_image = np.clip(image + noise, 0, 255)  # 노이즈를 더하고, 0-255 범위로 제한

# 노이즈가 추가된 이미지 표시
plt.imshow(noisy_image, cmap='gray', interpolation='nearest')
plt.title("Noisy Image")
plt.show()
