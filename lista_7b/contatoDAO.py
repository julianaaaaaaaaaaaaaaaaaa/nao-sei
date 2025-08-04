class ContatoDAO:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def listar(self):
        return self.contatos

    def buscar(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    def remover(self, nome):
        contato = self.buscar(nome)
        if contato:
            self.contatos.remove(contato)
            return True
        return False
