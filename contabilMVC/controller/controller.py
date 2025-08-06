class ContaController:
    def __init__(self, conta, view):
        self.conta = conta
        self.view = view

    def creditar(self, valor):
        self.conta.creditar(valor)
        self.view.operacao_realizada(f"Crédito de R$ {valor:.2f} realizado com sucesso.")

    def debitar(self, valor):
        self.conta.debitar(valor)
        self.view.operacao_realizada(f"Débito de R$ {valor:.2f} realizado com sucesso.")
    
    def mostrar_saldo(self):
        self.view.mostrar_saldo(self.conta.get_saldo())