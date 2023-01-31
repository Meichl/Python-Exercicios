n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} como nota, sua media foi {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('Aluno está APROVADO')
elif 7 > media >= 5:
    print('Aluno está em recuperação')
elif media < 5:
    print('Aluno está reprovado')