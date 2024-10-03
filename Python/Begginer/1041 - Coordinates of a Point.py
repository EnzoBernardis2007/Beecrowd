x, y = [float(x) for x in input().split(" ")]
message = ""

if x == y and y == 0:
    message = "Origem"
elif x == 0 and y != 0:
    message = "Eixo Y"
elif y == 0 and x != 0:
    message = "Eixo X"
elif x > 0:
    message = "Q1" if y > 0 else "Q4"
else:
    message = "Q2" if y > 0 else "Q3"
    
print(message)
