# from typing import List

# def sum_of_elements(numbers: List[int]) -> int : 
#     return sum(numbers) 


# print(sum_of_elements([1,10,3,2,6]))

from typing import Dict

def get_age(data: Dict[str, int]) -> int:
    return data['age']

# 잘못된 데이터 타입 예시
data = {'name': 'John', 'age': '30'}  

# 'age'는 문자열인데 'int'여야 합니다.
result = get_age(data)
print(result)
