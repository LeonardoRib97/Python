nome = input('Digite o seu nome ')
contador = 0
indice = 0

while contador < len(nome) :

    nomeatt = nome[contador ]
    print(f'*{nomeatt.upper()}', end="")
    contador += 1
