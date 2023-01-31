n = s = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos valores foi {s} e a quantidade de numeros digitados foi {c}')