frase = input("Digite uma frase: ")

indice = frase.rfind(" ")

ultima_palavra = frase[indice + 1:]

print(ultima_palavra)
