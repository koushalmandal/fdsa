def sumofdigits(number):
    if number == 0:
        return 0
    else:
     return number % 10 + sumofdigits(number // 10)
num = int(input("Enter a number: "))
result = sumofdigits(num)
print(f"{result}"
