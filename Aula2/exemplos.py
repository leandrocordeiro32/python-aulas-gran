# Imagine que um programador tenha que construir um programa que leia o salário bruto de um # empregado, calcule e informe sua gratificação (com base em seu salário bruto) e seu # salário líquido com base na tabela a seguir.
# Faixa salarial (R$) Gratificação (R$)
# Menor que 2000 5%
# De 2000 a 2500 10%
# Maior que 2500 e menor ou igual a 3000 15%
# Maior que 3000 20%

salario_bruto = float(input('Digite o valor do seu salário bruto: R$ '))
if salario_bruto < 2000:
    gratificacao = salario_bruto * 0.05
elif salario_bruto >= 2000 and salario_bruto <= 2500:
    gratificacao = salario_bruto * 0.10
elif salario_bruto > 2500 and salario_bruto <= 3000:
    gratificacao = salario_bruto * 0.15
else:
    gratificacao = salario_bruto * 0.20

salario_liquido = salario_bruto + gratificacao

print(f'Seu salário líquido é de R$ {salario_liquido:.2f}')
print(f'Sua gratificação foi de R$ {gratificacao:.2f}')

print()

print('Semana utilizadno if/elif/else')
# Agora o programador precisa escrever um código que seja capaz de armazenar um valor 
# inteiro de 1 a 7, para representar o dia da semana, e, ao final, mostre na tela o dia da 
# semana correspondente ao valor armazenado.

semana = int(input('Digite um número de 1 a 7: '))
if semana == 1:
    print('Domingo')
elif semana == 2:
    print('Segunda')
elif semana == 3:
    print('Terça')
elif semana == 4:
    print('Quarta')
elif semana == 5:
    print('Quinta')
elif semana == 6:
    print('Sexta')
elif semana == 7:
    print('Sábado')
else:
    print('Dia inválido')

print()

print('Semana utilizando match')

semana_match = int(input('Digite um número de 1 a 7: '))
match semana_match:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Dia inválido')