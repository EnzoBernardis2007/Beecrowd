days  = int(input())
years = days // 365
months = (days % 365) // 30
days = (days % 365) % 30

print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")
