A, B, C = [float(x) for x in input().split(" ")]

if A < B + C and B < A + C and C < A + B:
    print(f"Perimetro = {A + B + C:.1f}")
else:
    print(f"Area = {(A + B) * C / 2:.1f}")
