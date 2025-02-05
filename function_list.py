def process_data(*args):
    total = sum(sum(lst) for lst in args)  
    count = sum(len(lst) for lst in args)  
    avg = total / count if count > 0 else 0  
    
    return total, count, avg

result = process_data([10, 20, 30], [40, 50, 60], [70, 80])

total, count, avg = result
print(f"Total: {total}, Count: {count}, Average: {avg}")
