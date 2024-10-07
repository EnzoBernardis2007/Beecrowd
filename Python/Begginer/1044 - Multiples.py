numbers = [int(x) for x in input().split(" ")]
numbers.sort()

print("Sao Multiplos" if numbers[1] % numbers[0] == 0 else "Nao sao Multiplos")
