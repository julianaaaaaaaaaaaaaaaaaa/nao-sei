from datetime import date

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__nascimento = nascimento

    def __str__(self):
        return (
            f"ID: {self.__id}\n"
            f"Nome: {self.__nome}\n"
            f"E-mail: {self.__email}\n"
            f"Telefone: {self.__telefone}\n"
            f"Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"
        )

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id

    def get_nascimento(self):
        return self.__nascimento

    def atualizar(self, nome=None, email=None, telefone=None, nascimento=None):
        if nome: self.__nome = nome
        if email: self.__email = email
        if telefone: self.__telefone = telefone
        if nascimento: self.__nascimento = nascimento


class ContatoUI:
    def __init__(self):
        self.contatos = []

    def menu(self):
        while True:
            print("\n--- Menu da Agenda ---")
            print("1 - Inserir novo contato")
            print("2 - Listar todos os contatos")
            print("3 - Atualizar um contato")
            print("4 - Excluir um contato")
            print("5 - Pesquisar por iniciais do nome")
            print("6 - Mostrar aniversariantes do mês")
            print("7 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "5":
                self.pesquisar()
            elif opcao == "6":
                self.aniversariantes()
            elif opcao == "7":
                print("Saindo da agenda...")
                break
            else:
                print("Opção inválida!")

    def inserir(self):
        print("\n-- Novo Contato --")
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        dia = int(input("Dia do nascimento: "))
        mes = int(input("Mês do nascimento: "))
        ano = int(input("Ano do nascimento: "))
        nascimento = date(ano, mes, dia)
        contato = Contato(id, nome, email, telefone, nascimento)
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def listar(self):
        print("\n-- Lista de Contatos --")
        for c in self.contatos:
            print(c)
            print("-" * 30)

    def atualizar(self):
        id = int(input("Digite o ID do contato que deseja atualizar: "))
        contato = self.buscar_por_id(id)
        if contato:
            print("Deixe em branco se não quiser atualizar o campo.")
            nome = input("Novo nome: ")
            email = input("Novo e-mail: ")
            telefone = input("Novo telefone: ")
            nascimento = None
            nasc_input = input("Nova data de nascimento (dd/mm/aaaa): ")
            if nasc_input:
                dia, mes, ano = map(int, nasc_input.split("/"))
                nascimento = date(ano, mes, dia)
            contato.atualizar(nome or None, email or None, telefone or None, nascimento)
            print("Contato atualizado.")
        else:
            print("Contato não encontrado.")

    def excluir(self):
        id = int(input("Digite o ID do contato a excluir: "))
        contato = self.buscar_por_id(id)
        if contato:
            self.contatos.remove(contato)
            print("Contato removido.")
        else:
            print("Contato não encontrado.")

    def pesquisar(self):
        iniciais = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in self.contatos if c.get_nome().lower().startswith(iniciais)]
        if encontrados:
            print("\n-- Contatos Encontrados --")
            for c in encontrados:
                print(c)
                print("-" * 30)
        else:
            print("Nenhum contato encontrado.")

    def aniversariantes(self):
        mes = int(input("Digite o mês (1 a 12): "))
        aniversarios = [c for c in self.contatos if c.get_nascimento().month == mes]
        if aniversarios:
            print(f"\n-- Aniversariantes de {mes:02d} --")
            for c in aniversarios:
                print(c)
                print("-" * 30)
        else:
            print("Nenhum aniversariante neste mês.")

    def buscar_por_id(self, id):
        for contato in self.contatos:
            if contato.get_id() == id:
                return contato
        return None

if __name__ == "__main__":
    ui = ContatoUI()
    ui.menu()
