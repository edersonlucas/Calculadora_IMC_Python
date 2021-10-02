'''
 Recebe os dados
'''

ano_Atual = 2021
nome = input('Qual seu nome? ')
# Laço ano
while True:
    ano_Nascimento = input('Em que ano você nasceu? ')
    if ano_Nascimento.isdigit() == False or int(ano_Nascimento) >= 2022:
        print('Digite um ano valido!')
        continue
    else:
        ano_Nascimento = int(ano_Nascimento)
        if ano_Nascimento <= 1906:
            print('A Calculadora de IMC é somente para menores de 115 anos, porém receba nossos parabéns, com essa idade você é a pessoa mais velha do mundo.')
            continue
        else:
            break
# Laço altura
while True:
    altura = input('Qual sua altura? ')
    if altura.isalnum() == True and altura.isdigit() == False or float(altura) <= 0.2:
        print('Digite uma altura valida!')
        continue
    else:
        altura = float(altura)
        if altura >= 2.72:
            print('A Calculadora de IMC é somente para pessoas com menos de 2.72 metros de altura, porém receba nossos parabéns, com essa altura você é um gigante.')
            continue
        else:
            break
# Laço peso
while True:
    peso = input('Qual seu peso? ')
    if peso.isalnum() == True and peso.isdigit() == False  or float(peso) <= 0.2:
        print('Digite um peso valido!')
        continue
    else:
        peso= float(peso)
        break
imc = peso/(altura*altura)
idade = ano_Atual - ano_Nascimento

'''
 Imprime na tela
'''

print('-='*35)
print('{}, nasceu em {}, tem {} anos de idade e seu IMC é {:.2f}'.format(nome, ano_Nascimento, idade, imc,));
print('-='*35)
print('Status do seu IMC')

'''
 Condições
'''

if imc < 16:
    print('Você está com Magreza Grave. Consulte um médico.');
elif imc >= 16 and imc < 17:
    print('Você está com Magreza Moderada. Consulte um médico.');
elif imc >= 17 and imc < 18.5:
    print('Você está com Magreza Leve. Consulte um médico.');
elif imc >= 18.5 and imc < 25:
    print('Você está Saudável, Parabéns! Siga assim.');
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso. Consulte um médico.');
elif imc >= 30 and imc < 35:
    print('Você tem Obesidade Grau 1. Consulte um médico.');
elif imc >= 35 and imc < 40:
    print('Você tem Obesidade Grau 2(Severa). Consulte um médico.');
elif imc >= 40:
    print('Você tem Obesidade Grau 3(Mórbida). Consulte um médico.');
print('-='*35)

