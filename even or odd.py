def evenodd(n):
    #checking if the number is even or odd
    if n%2==0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print("Its a",evenodd(n), "number")