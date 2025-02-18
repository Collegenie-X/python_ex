def gcd (a,b) : 
    
    while b: 
        a, b = b, a%b 
        print ("a:",a, "b:",b)
    return a 

num1,num2 = map (int, input("두 개의 숫자로 ex> 15 45 으로 입력해 주세요. ").split())
print(gcd(num1, num2))