from Contato import Contato
from ContatoDAO import ContatoDAO
from ContatoView import ContatoView

class ContatoUI:
    def __init__(self):
        self.dao = ContatoDAO()
        self.view = ContatoView()

    def executar(self):
        while True:
            self.view.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome, telefone, email = self.view.ler_dados_contato()
                contato = Contato(nome, telefone, email)
                self.dao.adicionar(contato)
                self.view.mostrar_mensagem("Contato adicionado com sucesso!")

            elif opcao == '2':
                contatos = self.dao.listar()
                self.view.mostrar_contatos(contatos)

            elif opcao == '3':
                nome = input("Digite o nome para buscar: ")
                contato = self.dao.buscar(nome)
                self.view.mostrar_contato(contato)

            elif opcao == '4':
                nome = input("Digite o nome para remover: ")
                if self.dao.remover(nome):
                    self.view.mostrar_mensagem("Contato removido com sucesso.")
                else:
                    self.view.mostrar_mensagem("Contato não encontrado.")

            elif opcao == '0':
                self.view.mostrar_mensagem("Saindo...")
                break

            else:
                self.view.mostrar_mensagem("Opção inválida.")
