num = int(input("Enter any number : "))

check=0
while num>0:
    num = int(num/10)
    check += 1

print(check)