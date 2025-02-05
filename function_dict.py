def process_stats(data) : 
    
    total = sum(data['values'])
    count = len(data['values'])
    avg = total / count if count > 0 else 0
    
    
    return {'total': total, 'count': count, 'avg': avg }

data = {'values':[10,20,30,40,50]}
result = process_stats(data) 

total,count,avg = result['total'],result['count'],result['avg']
print(f"Toal:{total},Count:{count},Avg:{avg}")