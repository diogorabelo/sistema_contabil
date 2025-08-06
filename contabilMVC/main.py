from model.conta_contabil import ContaAtivo, ContaPassivo
from view.view import ContaView
from controller.controller import ContaController


def main():
    view = ContaView()

    conta_caixa = ContaAtivo(1, "Conta Caixa")
    conta_emprestimo = ContaPassivo(2, "Conta Empréstimo")

    controller_caixa = ContaController(conta_caixa, view)
    controller_emprestimo = ContaController(conta_emprestimo, view)

    controller_caixa.creditar(1000)
    controller_caixa.debitar(200)
    controller_emprestimo.debitar(500)

    print("\n Saldos Finais:")
    controller_caixa.mostrar_saldo()
    controller_emprestimo.mostrar_saldo()


if __name__ == "__main__":
    main()