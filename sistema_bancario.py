"""
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a 
linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não 
precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável 
e exibidos na operação de extrato.

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema 
deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável 
e exibidos na operação de extrato.

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem 
ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45
"""

def entrar_no_banco():

    saldo = 2000
    extrato = ""
    numero_atual_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(
        """
            
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

        => """
        )
  
        if opcao == "s":
            saque = float(input("Digite a quantidade a ser sacada: "))

            if numero_atual_saques >= LIMITE_SAQUES:
                print("Você ultrapassou seu limite diário de saques!")

            elif saque > 0 and saque <= 500:
                print("Sacando...")
                saldo = saldo - saque
                numero_atual_saques += 1
                extrato = extrato + f"Saque:    R$ {saque:.2f}\n".replace('.', ',')
                saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
                print(f"Saque realizado com sucesso! \nSaldo restante: R$ {saldo_formatado}")

            elif saque > saldo:
                print("Não foi possível sacar este valor pois não há saldo suficiente")
                saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
                print(f"Saldo atual: R$ {saldo_formatado}")

            elif saque > 500:
                print("Não é permitido sacar mais do que R$ 500,00 de uma única vez")

            
        elif opcao == "e":
            print("\n================ EXTRATO ================\n")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
            print(f"\nSaldo: R$ {saldo_formatado}")
            print("\n=========================================")

        elif opcao == "d":
            deposito = float(input("Digite a quantidade a ser depositada: "))

            if deposito > 0:
                print("Depositando...")
                saldo = saldo + deposito
                extrato = extrato + f"Depósito: R$ {deposito:.2f}\n".replace('.', ',')
                saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
                print(f"Depósito realidado com sucesso! \nSaldo atual: R$ {saldo_formatado}")
            
            else:
                print("Valor digitado é inválido!")

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

entrar_no_banco()