n = int(input("Enter a Number :"))
reversed_num = 0

while n != 0:
    digit = n % 10
    reversed_num = (reversed_num * 10) + digit
    n = n // 10

print("Reversed Number :", reversed_num)
