def complex_analysis(data, params) :
    # 데이터와 매개변수를 언팩킹하여 처리
    total = sum(data)
    count = len(data)
    avg = total / count if count > 0 else 0
    min_val = min(data)
    max_val = max(data)
    
    # 결과를 딕셔너리로 반환
    result = {
        'total': total,
        'count': count,
        'average': avg,
        'min': min_val,
        'max': max_val,
        'params': params
    }
    
    return result

# 리스트와 딕셔너리를 혼합하여 전달
data = [10, 20, 30, 40, 50]
params = {'filter': 'positive', 'operation': 'sum'}

result = complex_analysis(data, params)

# 반환된 딕셔너리 언팩킹하여 사용
total, count, avg, min_val, max_val, params = \
    result['total'], result['count'], result['average'], \
    result['min'], result['max'], result['params']
    
print(f"Total: {total}, Count: {count}, \
        Average: {avg}, Min: {min_val}, Max: {max_val}")
print(f"Parameters: {params}")

