a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
c = int(input("Enter a Number : "))

if a > b and a > c:
    print(a,"is largest number")
elif b > a and b > c:
    print(b ,"is largest number")
elif c > a and c>b:
    print(c ,"is largest number")