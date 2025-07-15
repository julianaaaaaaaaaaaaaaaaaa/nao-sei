class Treino:
    def __init__(self, id, data, distancia, tempo):
        self._id = id
        self._data = data
        self._distancia = distancia
        self._tempo = tempo

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_distancia(self):
        return self._distancia

    def set_distancia(self, distancia):
        self._distancia = distancia

    def get_tempo(self):
        return self._tempo

    def set_tempo(self, tempo):
        self._tempo = tempo

    def __str__(self):
        return f"ID: {self._id} | Data: {self._data} | Distância: {self._distancia} km | Tempo: {self._tempo} min"

    def velocidade_media(self):
        if self._tempo > 0:
            return self._distancia / (self._tempo / 60)
        return 0


class TreinoUI:
    def __init__(self):
        self.lista = []

    def menu(self):
        while True:
            print("\n=== MENU DE TREINOS ===")
            print("1 - Inserir novo treino")
            print("2 - Listar todos os treinos")
            print("3 - Listar treino por ID")
            print("4 - Atualizar treino")
            print("5 - Excluir treino")
            print("6 - Mostrar treino mais rápido")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.listar_id()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.excluir()
            elif opcao == "6":
                self.mais_rapido()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    def inserir(self):
        id = int(input("ID do treino: "))
        data = input("Data do treino (dd/mm/aaaa): ")
        distancia = float(input("Distância (km): "))
        tempo = float(input("Tempo (min): "))
        treino = Treino(id, data, distancia, tempo)
        self.lista.append(treino)
        print("✅ Treino inserido com sucesso!")

    def listar(self):
        if len(self.lista) == 0:
            print("Nenhum treino cadastrado.")
        else:
            print("\n--- LISTA DE TREINOS ---")
            for t in self.lista:
                print(t)

    def listar_id(self):
        id = int(input("Informe o ID do treino: "))
        for t in self.lista:
            if t.get_id() == id:
                print("Treino encontrado:")
                print(t)
                return
        print("Treino não encontrado.")

    def atualizar(self):
        id = int(input("Informe o ID do treino que deseja atualizar: "))
        for t in self.lista:
            if t.get_id() == id:
                nova_data = input("Nova data: ")
                nova_distancia = float(input("Nova distância (km): "))
                novo_tempo = float(input("Novo tempo (min): "))
                t.set_data(nova_data)
                t.set_distancia(nova_distancia)
                t.set_tempo(novo_tempo)
                print("✅ Treino atualizado.")
                return
        print("Treino com esse ID não foi encontrado.")

    def excluir(self):
        id = int(input("Informe o ID do treino para excluir: "))
        for t in self.lista:
            if t.get_id() == id:
                self.lista.remove(t)
                print("❌ Treino removido.")
                return
        print("Treino não encontrado.")

    def mais_rapido(self):
        if len(self.lista) == 0:
            print("Nenhum treino para analisar.")
            return

        mais_rapido = self.lista[0]
        for t in self.lista[1:]:
            if t.velocidade_media() > mais_rapido.velocidade_media():
                mais_rapido = t

        print("🏅 Treino com maior velocidade média:")
        print(mais_rapido)
        print(f"Velocidade média: {mais_rapido.velocidade_media():.2f} km/h")


if __name__ == "__main__":
    app = TreinoUI()
    app.menu()
