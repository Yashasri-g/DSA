def table(n):
    """Prints the multiplication table for a given number n."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
n = int(input("Enter a number to print its multiplication table: "))
table(n)