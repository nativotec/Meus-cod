#Ler arquivo txt



with open('projetox.txt', "r") as arquivo:
    projetox = arquivo.read()
print(projetox)