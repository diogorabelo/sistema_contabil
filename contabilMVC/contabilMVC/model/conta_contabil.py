class ContaContabil:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__saldo = 0.0

    def creditar(self, valor):
        self.__saldo += valor

    def debitar(self,valor):
        raise ValueError("esse metodo deve ser implementado pela subclasse")
    def get_nome(self):
        return self.__nome
    
    def get_saldo(self):
        return self.__saldo
    
class ContaAtivo(ContaContabil):
    def debitar(self, valor):
        self._ContaContabil__saldo -= valor #Acesso ao atributo privado da superclasse
    
class ContaPassivo(ContaContabil):
    def debitar(self, valor):
        self._ContaContabil__saldo += valor  # Acesso ao atributo privado da superclasse