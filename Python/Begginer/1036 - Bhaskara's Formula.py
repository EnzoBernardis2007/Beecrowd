import math

A, B, C = [float(x) for x in input().split(' ')]

delta = B ** 2 - 4 * A * C

if A != 0 and delta > -1:
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")
