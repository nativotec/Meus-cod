# Dierença

# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B 
# pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

# Entrada
# O arquivo de entrada contém 4 valores inteiros.

# Saída
# Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

# Exemplos de Entrada	Exemplos de Saída

# 5
# 6
# 7
# 8          DIFERENCA = -26

# 0
# 0
# 7
# 8          DIFERENCA = -56

# 5
# 6
#-7
# 8          IFERENCA = 86

linha1 = input().split(" ")
linha2 = input().split(" ")
cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2
total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))
print("VALOR A PAGAR: R$ %0.2f" %total)