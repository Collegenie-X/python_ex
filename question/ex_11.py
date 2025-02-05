def sum_even_numbers(n) : 
    total = 0 
    for i in range(1,n+1): 
        
        if i % 2 == 0 : 
            # print("list:",[i for i in range(1,i+1) if i %2 == 0 ])
            total += i
            print("total:",total)
    return total 

n = int (input())
print("최종 sum:",sum_even_numbers(n)) 