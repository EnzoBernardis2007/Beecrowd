input1 = input().split(" ")
A = float(input1[0])
B = float(input1[1])
C = float(input1[2])
PI = 3.14159

print(f"TRIANGULO: {A * C / 2:.3f}")
print(f"CIRCULO: {pow(C, 2) * PI:.3f}")
print(f"TRAPEZIO: {((A + B) / 2) * C:.3f}")
print(f"QUADRADO: {pow(B, 2):.3f}")
print(f"RETANGULO: {A * B:.3f}")
