cod, num = [x for x in input().split()]
prices = (4.0, 4.5, 5.0, 2.0, 1.5)

print(f"Total: R$ {prices[int(cod) - 1] * float(num):.2f}")
