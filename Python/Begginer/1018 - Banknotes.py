money = int(input())
banknotes = (100, 50, 20, 10, 5, 2, 1)

print(money)
for i in range(len(banknotes)):
    numOfNotes = money // banknotes[i]
    money %= banknotes[i]
    print(f'{numOfNotes} nota(s) de R$ {banknotes[i]:.2f}'.replace('.', ','))
