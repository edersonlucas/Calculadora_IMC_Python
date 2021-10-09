'''
Calculadora IMC
Autor: Ederson Lucas
'''


#Entrada do Nome

nome = input('Qual seu nome? ')

# Laço ano

while True:
    idade = input('Qual sua idade? ')
    if idade.isdigit() == False or int(idade) <= 0:
        print('Digite uma idade valida!')
        continue
    else:
        idade = int(idade)
        if idade >= 115:
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

#Imprime na tela

print('-='*35)
print('{}, tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc,));
print('-='*35)
print('Status do seu IMC')

# Condições

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
