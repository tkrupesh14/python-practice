num = int(input("Enter Number : "))

ans = 0 
while num>0:
    rev = int(num%10)
    num = int(num/10)
    ans = (ans*10) + rev

print(ans)