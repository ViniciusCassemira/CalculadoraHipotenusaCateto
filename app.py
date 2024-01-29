from math import sqrt
import os
from time import sleep
from msvcrt import getch

def pressione_para_sair():
    print('Pressione qualquer tecla para sair')
    getch()

def linha(a):
    print('_' * a)

def menu():
    print('CALCULADORA DE CATETO E HIPOTENUSA')
    linha(30)
    print('[1] Calcular Hipotenusa')
    print('[2] Calcular Cateto')
    print('[3] Sair')
    print('')
    dec = input('Digite sua opção: ')
    return dec

dec = menu()

while dec not in ['1', '2', '3']:
    os.system('cls')
    print("Opção inválida, tente novamente")
    print('')
    dec = menu()

if dec == '1':
    #calcular hipotenusa: C²=A²+B²
    os.system('cls')
    print(' Opção 1: Calcular Hipotenusa')
    linha(30)
    while True:

     cateto1 = input('Digite o valor do primeiro cateto: ')
    
     if cateto1.strip() == "":
           os.system('cls')
           print("Por favor, insira um valor válido.")
           continue
    
     if not cateto1.replace(".", "", 1).isdigit():
          os.system('cls')
          print("Por favor, insira um valor numérico.")
          continue
    
     a = float(cateto1)
     break

    while True:
     cateto2 = input('Digite o valor do segundo cateto: ')
    
     if cateto2.strip() == "":
         os.system('cls')
         print("Por favor, insira um valor válido.")
         continue
    
     if not cateto2.replace(".", "", 1).isdigit():
          os.system('cls')
          print("Por favor, insira um valor numérico.")
          continue
    
     b = float(cateto2)
     break

    c = sqrt(a**2 + b**2)

    print('O valor da hipotenusa é de {:.2f}'.format(c))
    pressione_para_sair()

if dec == '2':
    #calcular cateto: b²=c²-a²
    os.system('cls')
    print(' Opção 2: Calcular Cateto')
    linha(27)

    while True:
     hipotenusa = input('Digite o valor da hipotenusa: ')

     if hipotenusa.strip() == '':
           os.system('cls')
           print('Por favor, insira um valor válido.')
           continue

     if not hipotenusa.replace('.','',1).isdigit():
           os.system('cls')   
           print('Por favor, digite um valor numérico.')
           continue

     c = float(hipotenusa) 
     break

    while True:
     cateto = input('Digite o valor do cateto: ')

     if cateto.strip() == '':
          os.system('cls')  
          print('Digite um valor válido. ')
          continue
     
     if not cateto.replace('.','',1).isdigit():
         os.system('cls') 
         print('Por favor, digite um valor númerico. ')
         continue
     
     if cateto >= hipotenusa:
         os.system('cls')
         print('O cateto não pode ser igual ou maior do que a hipotenusa!')
         print('Valor da hipotenusa: {}'.format(hipotenusa))
         continue
  
     a = float(cateto)
     break

    b = sqrt(c**2 - a**2)
    print('O valor do segundo cateto é de {:.2f}'.format(b))
    input("Pressione ENTER para encerrar")

if dec == '3':
    os.system('cls')
    print('Você escolheu sair')
    print('fechando em 3')
    sleep(1)
    os.system('cls')
    print('Você escolheu sair')
    print('fechando em 2')
    sleep(1)
    os.system('cls')
    print('Você escolheu sair')
    print('fechando em 1')
    sleep(1)
    exit()