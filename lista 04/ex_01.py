import random

class Bingo:
    def __init__(self):
        self.num_bolas = 0
        self.bolas_sorteadas = []

    def iniciar(self, num_bolas):
        self.num_bolas = num_bolas
        self.bolas_sorteadas = []
        print(f"Jogo iniciado com {num_bolas} bolas.")

    def sortear(self):
        if len(self.bolas_sorteadas) == self.num_bolas:
            return None
        while True:
            bola = random.randint(1, self.num_bolas)
            if bola not in self.bolas_sorteadas:
                self.bolas_sorteadas.append(bola)
                return bola

    def sorteados(self):
        return self.bolas_sorteadas

class BingoUI:
    def __init__(self):
        self.bingo = None

    def menu(self):
        print("\n--- MENU DO BINGO ---")
        print("1 - Iniciar novo jogo")
        print("2 - Sortear número")
        print("3 - Mostrar números sorteados")
        print("4 - Sair")

    def iniciar_jogo(self):
        num = int(input("Quantas bolas terá o jogo? "))
        self.bingo = Bingo()
        self.bingo.iniciar(num)

    def sortear_numero(self):
        if self.bingo is None:
            print("Você precisa iniciar um jogo primeiro.")
            return
        numero = self.bingo.sortear()
        if numero is None:
            print("Todas as bolas já foram sorteadas.")
        else:
            print(f"Número sorteado: {numero}")

    def mostrar_sorteados(self):
        if self.bingo is None:
            print("Nenhum jogo em andamento.")
        else:
            print("Números sorteados até agora:")
            print(self.bingo.sorteados())

    def main(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.iniciar_jogo()
            elif opcao == '2':
                self.sortear_numero()
            elif opcao == '3':
                self.mostrar_sorteados()
            elif opcao == '4':
                print("Encerrando o jogo. Até mais!")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    ui = BingoUI()
    ui.main()
