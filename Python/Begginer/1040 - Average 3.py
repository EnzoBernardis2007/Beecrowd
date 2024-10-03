A, B, C, D = [float(x) for x in input().split(" ")]
average = (A * 2 + B * 3 + C * 4 + D) / (2 + 3 + 4 + 1)

print(f"Media: {average:.1f}")
if average >= 7:
    print("Aluno aprovado.")
elif average < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")
    average = (average + exam) / 2
    message = "Aluno aprovado." if average >= 5 else "Aluno reprovado."
    print(message)
    print(f"Media final: {average:.1f}")
