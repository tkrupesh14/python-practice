num = int(input("Enter Number : "))

ans = 2
n = 0
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1:
            ans = 2
        else:
            ans = (ans*10)+2
    else:
        n = n + ans

print(n)