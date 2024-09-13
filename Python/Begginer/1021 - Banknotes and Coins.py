reais, centavos = [int(x) for x in input().strip().split('.')]
reais = reais * 100 + centavos
banknotes = (10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1)
text = "nota"

print(text.upper() + "S:")
for x in banknotes:
    if x == 100:
        text = "moeda"
        print(text.upper() + "S:")
    print(f"{reais//x} {text}(s) de R$ {(x/100):.2f}")
    reais %= x
