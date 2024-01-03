def calculate_product(n):
    product = 1
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            product *= i
    else:
        for i in range(2, n + 1, 2):
            product *= i
    return product

N = int(input("Insert n: "))
result = calculate_product(N)
print(f"Product: ", result)  