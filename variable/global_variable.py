x = 10 

def print_global_variables(): 
    print (f"전역 변수 x의 값 : {x}")
    
def modify_global_variables() : 
    # global x 
    x = 20
    print(f"전역 변수 x를 수정한 값 : {x}")
    

print_global_variables()
modify_global_variables() 
print_global_variables()