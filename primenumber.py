lowernumber = int(input("Enter a lower range: "))
uppernumber = int(input("Enter an upper range: "))

print("Prime numbers between", lowernumber, "and", uppernumber, "are:")

for num in range(lowernumber, uppernumber + 1):

    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
            break