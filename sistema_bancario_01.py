# importação da biblioteca para data/hora
from datetime import datetime

#menu de opções
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

#declaração de váriáveis 
data_hora_atual = datetime.now() #declaração da data e hora atual
mascara = "%d-%m-%Y" # declaração da formato de saída da data
saldo = 0 # Saldo inicia com R$ 0,00
limite = 500 # Limita transações em R$ 500,00
extrato = "" #extrato começa vazio
numero_saques = 0 #Limite iniciao de saques
LIMITE_SAQUES = 3 #Limite final de saques no dia

#Inicia Menu - apresentação na tela
while True:

    opcao = input(menu)

# Opção de depósito no menu
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"{data_hora_atual.strftime(mascara)} - Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

# Opção de saque no menu
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"{data_hora_atual.strftime(mascara)} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

  # Opção de extrato no menu
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n{data_hora_atual.strftime(mascara)} - Saldo: R$ {saldo:.2f}")
        print("==========================================")

  # Saida do looping do laço do menu
    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
