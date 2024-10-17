num = int(input("Enter a Number: "))

if num <= 1:
    print(num, "is not a prime number")

elif num == 2:
    print(num, "is a prime number")

elif num % 2 == 0:
    print(num, "is not a prime number")

else:
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
