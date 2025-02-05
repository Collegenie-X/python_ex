text = input()

if text.isupper() : 
    print(text,": 대문자")
    
elif text.islower():
    print(text,": 소문자")

else:
    print(text,": 대소문자 혼합")