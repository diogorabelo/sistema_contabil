import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget

class ContaView(QWidget):
    def __init__(self):
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()

        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contas Contábeis")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.label_titulo = QLabel("Movimentações da Conta")
        layout.addWidget(self.label_titulo)

        self.lista_movimentos = QListWidget()
        layout.addWidget(self.lista_movimentos)

        self.setLayout(layout)
        self.show()

    def operacao_realizada(self, mensagem):
        """Chamado pelo controller quando há crédito/débito."""
        self.lista_movimentos.addItem(mensagem)
        print(mensagem)  # mantém saída no console

    def mostrar_saldo(self, saldo):
        """Exibe o saldo final na interface."""
        mensagem = f"Saldo atual: R$ {saldo:.2f}"
        self.lista_movimentos.addItem(mensagem)
        print(mensagem)  # mantém saída no console

    def executar(self):
        """Executa o loop do PyQt."""
        if hasattr(self, 'app'):
            sys.exit(self.app.exec_())

            
