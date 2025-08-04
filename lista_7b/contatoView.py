class ContatoView:
    def mostrar_menu(self):
        print("\n=== MENU ===")
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Buscar Contato")
        print("4 - Remover Contato")
        print("0 - Sair")

    def ler_dados_contato(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        return nome, telefone, email

    def mostrar_contato(self, contato):
        if contato:
            print(f"\nContato encontrado: {contato}")
        else:
            print("\nContato não encontrado.")

    def mostrar_contatos(self, contatos):
        print("\n--- Lista de Contatos ---")
        for contato in contatos:
            print(contato)

    def mostrar_mensagem(self, msg):
        print(msg)
