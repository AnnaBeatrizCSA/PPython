
entradas = []
gastos = []


def mostrar_menu():
    print("\n---CONTROLE DE GASTOS---")
    print("1 - Adicionar entrada (receita)")
    print("2 - Adicionar gasto (despesa)")
    print("3 - Ver saldo")
    print("4 - Listar histórico")
    print("5 - Apagar histórico")
    print("6 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor da entrada (R$): "))
        entradas.append(valor)
        print("Entrada adicionada com sucesso!")

    elif opcao == "2":
        valor = float(input("Digite o valor do gasto (R$): "))
        gastos.append(valor)
        print("Gasto registrado com sucesso!")

    elif opcao == "3":
        saldo = sum(entradas) - sum(gastos)
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "4":
        print("\nHistórico de entradas:")
        for e in entradas:
            print(f"  + R$ {e:.2f}")
        print("\nHistórico de gastos:")
        for g in gastos:
            print(f"  - R$ {g:.2f}")

    elif opcao == "5":
        confirmacao = input("⚠ Tem certeza que deseja apagar todo o histórico? (S/N): ").upper()
        if confirmacao == "S":
            entradas.clear()
            gastos.clear()
            print("Histórico apagado com sucesso!")

    elif opcao == "6":
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")
