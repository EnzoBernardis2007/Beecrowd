input1 = input().split(" ")
input2 = input().split(" ")

units1 = int(input1[1])
units2 = int(input2[1])
price1 = float(input1[2])
price2 = float(input2[2])

print(f"VALOR A PAGAR: R$ {units1 * price1 + units2 * price2:.2f}")
