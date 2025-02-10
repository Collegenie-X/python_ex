import numpy as np 

# 두 벡터
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

# 코사인 유사도 계산 (내적 / (벡터1의 크기 * 벡터2의 크기))
cosine_similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
print("코사인 유사도:", cosine_similarity)
