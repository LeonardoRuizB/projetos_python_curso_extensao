# -*- coding: utf-8 -*-

a1 = float(input('Informe a Primeira nota: '))
a2 = float(input('Informe a Segunda nota: '))

media = (a1 + a2 ) / 2

print(f'A média do aluno é: {media}')

if media >= 7.0:
    print('Aluno aprovado!!')
    if media >= 9.0:
        print('Parabéns, você foi esplêndido esse semestre!!')
else:
    print('Aluno reprovado!!')

#Em Python, não usamos {}, utilizamos os dois pontos : e pelo fato de não usarmos
#os {} o espaçamento por TAB é muito importante

print('Fim do programa')