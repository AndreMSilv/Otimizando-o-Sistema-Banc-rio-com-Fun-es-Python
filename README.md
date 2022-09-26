# Otimizando-o-Sistema-Banc-rio-com-Fun-es-Python
Otimizando o Sistema Bancário com Funções Python /  Python Developer /  Dio.me
![images](https://user-images.githubusercontent.com/87867234/192295408-009f6c69-e6f6-45e0-b04e-452737605075.jpg)



"""Projeto banco DIO - Python Bootcamp

- único usuário, três operações, saque, depósito e extrato

- depósito: tem que perguntar o valor, que deve ser positivo.

- saque: no máximo 3 saques por dia, limite de 500 reais cada saque, se não tiver saldo em conta, deve mandar msg que não pode sacar pois não tem

- extrato: devem ser exibidos todos os saques e depósitos realizados, formatado valor R$ XXXX.XX.



"""

import time
import os

SAUDACOES = """
  -=-=-=-=-=-=-=-=-=-=-=-=

    Bem vindo ao Banco 

  -=-=-=-=-=-=-=-=-=-=-=-=
"""

MENU = """
  -=-=-=-=-=-=-=-=-=-=-=-=

  Digite a opção desejada:

  [d] - Depósito
  [s] - Saque
  [e] - Extrato
  [f] - Fechar o programa

  -=-=-=-=-=-=-=-=-=-=-=-=
"""



LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES = 3
LIMITE_VALOR_TOTAL = LIMITE_VALOR_SAQUE * LIMITE_SAQUES
extrato = list()
saques = 0
valor_total_sacado = 0
saldo = 499

print(SAUDACOES)


while True:
  print(MENU)
  opc = input("\n Digite a opção desejada: ")
  if opc in 'dDsSfFeE':
    
    # Verificando se usuário digitou numeros
    if opc in 'sS':
      valor = input('\nDigite o valor desejado para sacar: ')
      try:
        valor = float(valor)
      except:
        print('\nSomente são aceitos valores monetários para saque. Retornando ao menu principal')
        time.sleep(3)
        
        continue

      # Verificando condições do saque
      if valor > LIMITE_VALOR_SAQUE:
        print("\nO valor máximo para saques é de R$ 500.00 \nRetornando ao menu principal ")
        time.sleep(3)
        continue
        
      elif saques >= LIMITE_SAQUES:
        print("\n Você atingiu o limite máximo de saques de hoje... \nRetornando ao menu principal ")
        time.sleep(3)
        continue
        
      elif valor_total_sacado >= LIMITE_VALOR_TOTAL:
        print("\n Você atingiu o limite máximo do valor sacado de hoje... \nRetornando ao menu principal ")
        time.sleep(3)
        continue
        
      elif valor > saldo:
        print("\n Você não possui saldo suficiente para sacar este valor... \nRetornando ao menu principal ")
        time.sleep(3)
        continue

      # Efetuando saque
      else:
        
        saques += 1
        valor_total_sacado += valor
        saldo -= valor
        extrato.append(['Saque',valor])
        print(f"\nVoce sacou R$ {valor:.2f} da sua conta, o saldo agora é de R$ {saldo:.2f}.")


    # ESCOLHEU DEPOSITO
    
    elif opc in 'dD':
      # Verificando se usuário digitou numeros
      valor = input('\nDigite o valor desejado para depositar: ')
      try:
        valor = float(valor)
      except:
        print('\nSomente são aceitos valores monetários para depósito. Retornando ao menu principal')
        time.sleep(3)
        continue
  
      # Verificando condições do deposito
      if valor < 1:
        print("\nO valor mínimo para depósitos é de R$ 1.00 \nRetornando ao menu principal ")
        time.sleep(3)
        continue
      
      # Executando o depósito
      else:
        saldo += valor
        extrato.append(['Deposito',valor])
        print(f"\nVoce depositou R$ {valor:.2f} da sua conta, o saldo agora é de R$ {saldo:.2f}.")
        time.sleep(3)
        continue
          

    elif opc in 'eE':
      print("Imprimindo extrato: ")
      time.sleep(1)
      tamanho = len(extrato)
      for i in range(tamanho):
        print(f"Você realizou um {extrato[i][0]} no valor de R$ {extrato[i][1]:.2f} ")
        time.sleep(0.5)
        print(f"Seu saldo é de R$ {saldo:.2f}")
        time.sleep(5)

    else: 
      print('fechando')
      time.sleep(1)
      break
      
  else:
    print("\nOpção inválida, retornando ao menu principal \n")
    time.sleep(1)
