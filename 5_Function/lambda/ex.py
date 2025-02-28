is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("4:",is_even(4))  # Even
print("7:",is_even(7))  # Odd

# 두 수의 합
add = lambda x, y: x + y
print(add(3, 5))  # 8

# 두 수 중 더 큰 값 구하기
max_value = lambda x, y: x if x > y else y
print(max_value(10, 5))  # 10

#리스트의 각 요소 제곱하기
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]

# 문자열에서 길이가 5보다 긴 단어 필터링
words = ["apple", "banana", "kiwi", "cherry", "grape"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # ['banana', 'cherry']


#숫자가 홀수인지 짝수인지 판단하기 
is_odd = lambda x: x % 2 != 0
print(is_odd(3))  # True
print(is_odd(4))  # False
