from math import sqrt #calcular a raiz quadrada
import os #limpar o terminal
from time import sleep #dar um temo antes de fechar o terminal
from msvcrt import getch #espera uma resposta do teclado para fechar o terminal

def aviso(txt): #dar a cor amarela nos aviso que podem aparecer, assim evito a repetição
    print('\033[93m'+txt+'\033[0m')
def calc_cat(x,y,z): #criei para evitar a repetição da tabela, deixando o código menor
    print(' _______________________________')
    print('|       CALCULAR CATETO         |')
    print('|-------------------------------|')
    print('|Hipotenusa:{}{}|'.format(x,' '*(20-len(str(x)))))
    print('|Primeiro cateto:{}{}|'.format(y,' '*(15-len(str(y)))))
    print('|Segundo cateto:{}{}|'.format(z,' '*(16-len(str(z)))))
    print('|_______________________________|')
def calc_hip(x,y,z): #criei para evitar a repetição da tabela, deixando o código menor
    print(' _______________________________')
    print('|      CALCULAR HIPOTENUSA      |')
    print('|-------------------------------|')
    print('|Primeiro cateto:{}{}|'.format(x,' '*(15-len(str(x)))))
    print('|Segundo cateto:{}{}|'.format(y,' '*(16-len(str(y)))))
    print('|Hipotenusa:{}{}|'.format(z,' '*(20-len(str(z)))))
    print('|_______________________________|')
def pressione_para_sair(): #aguarda uma resposta do teclado para fechar o programa
    print('Pressione qualquer tecla para sair')
    getch()
def menu():#menu onde o usuário vai selecionar oque deseja fazer
    print(' ________________________________')
    print('|          CALCULADORA           |')
    print('|--------------------------------|')
    print('|[1] Calcular Hipotenusa         |')
    print('|[2] Calcular Cateto             |')
    print('|[3] Sair                        |')
    print('|________________________________|')
    dec = input('Digite sua opção: ')
    return dec

dec = menu()

while dec not in ['1', '2', '3']:
    os.system('cls')
    aviso('Opção inválida, selecione uma existente.')
    dec = menu()

if dec == '1': #calcular a hipotenusa
    #calcular hipotenusa: C²=A²+B²
    os.system('cls')
   
    while True:
     calc_hip('','','')
     cateto1 = input('Valor do primeiro cateto: ')
    
     if cateto1.strip() == "": #caso esteja vazio a variável
           os.system('cls')
           aviso('Insira um valor numérico.')
           continue
    
     if not cateto1.replace(".", "", 1).isdigit(): 
          #usamos o replace para substituir um ponto(caso tenha no numero) por um espaço vazio, e pedimos
          #para analisar se é um dígito, caso tenha mais de um ponto não é aceito
          #palavras e símbolos são barrados aqui tbb
          os.system('cls')
          aviso('Insira um valor numérico.')
          continue
     
     a = float(cateto1) #passamos o valor para outra variável do tipo float somente para calcular
     os.system('cls')
     break

    while True:
     calc_hip(cateto1,'','')
     cateto2 = input('Valor do segundo cateto: ')
    
     if cateto2.strip() == "": #caso a variével esteja vazia
         os.system('cls')
         aviso('Insira um valor numérico.')
         continue
    
     if not cateto2.replace(".", "", 1).isdigit():
          #usamos o replace para substituir um ponto(caso tenha no numero) por um espaço vazio, e pedimos
          #para analisar se é numérico, caso tenha mais de um ponto não é aceito
          #palavras e símbolos são barrados aqui tb
          os.system('cls')
          aviso('Insira um valor numérico.')
          continue
     
     
     b = float(cateto2)#passamos o valor para outra variável do tipo float somente para calcular
     break
   
    h = sqrt(a**2 + b**2) #calculo para chegar no resultado
    h = round(h,2) #limitamos em duas casas decimais
    os.system('cls')
    calc_hip(cateto1,cateto2,h)
    pressione_para_sair()

if dec == '2': #calcular o cateto
    #calcular cateto: b²=c²-a²
    os.system('cls')

    while True:
     calc_cat('','','')
     hipotenusa = input('Digite o valor da hipotenusa: ')

     if hipotenusa.strip() == '': #caso esteja vazio
           os.system('cls')
           aviso('Insira um valor numérico.')
           continue

     if not hipotenusa.replace('.','',1).isdigit():
          #usamos o replace para substituir um ponto(caso tenha no numero) por um espaço vazio, e pedimos
          #para analisar se é um dígito, caso tenha mais de um ponto não é aceito
          #palavras e símbolos são barrados aqui tbb
           os.system('cls')   
           aviso('Insira um valor numérico.')
           continue
    
     h = float(hipotenusa) #passamos o valor da hpotenusa para outra vaiavel do tipo float para calcular
     os.system('cls')
     break

    while True:
     calc_cat(hipotenusa,'','')
     cateto = input('Digite o valor do cateto: ')

     if cateto.strip() == '':
          os.system('cls')  
          aviso('Insira um valor numérico.')
          continue
     
     if not cateto.replace('.','',1).isdigit():
          #usamos o replace para substituir um ponto(caso tenha no numero) por um espaço vazio, e pedimos
          #para analisar se é um dígito, caso tenha mais de um ponto não é aceito
          #palavras e símbolos são barrados aqui tbb
         os.system('cls') 
         aviso('Insira um valor numérico.')
         continue
     
     if float(cateto) >= h: 
         #os catetos nunca podem se maiores ou iguais a hipotenusa
         #passamos a cateto para uma variável do tipo float para comparar seu tamanho com a hipotenusa
         os.system('cls')
         aviso('O cateto não pode ser igual ou maior do que a hipotenusa.')
         continue
     
     c1 = float(cateto) #passamos o valor do cateto para outra vaiavel do tipo float para calcular
     os.system('cls')
     break

    c2 = sqrt(h**2 - c1**2) #calculando o seegundo cateto
    c2 = round(c2,2) #limitando em 2 casas decimais
    calc_cat(hipotenusa,cateto,c2)
    input("Pressione ENTER para encerrar")

if dec == '3': #nada de importante, apenas um sistema mais enfeitado para fechar o terminal
    os.system('cls')
    aviso('Você escolheu sair')
    print('fechando em 3')
    sleep(1)
    os.system('cls')
    aviso('Você escolheu sair')
    print('fechando em 2')
    sleep(1)
    os.system('cls')
    aviso('Você escolheu sair')
    print('fechando em 1')
    sleep(1)
    exit()