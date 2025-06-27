def sumofnaturals(n):
    sum = (n*(n+1))/2
    return sum

if __name__ == "__main__":
    n = int(input("Enter the number to know the sum of it from 1 to given number: "))
    print(sumofnaturals(n))