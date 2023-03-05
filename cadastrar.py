from random import randint
def cadastrar_usuario():

 id = (randint(1, 1000), randint(1, 1000))
 count = 0
 with open(f"{id}.txt", "w") as arquivo:
    while True:
        a = str(input("Crie um nome de usuario:"))
        b = str(input("Crie uma senha numerica:"))
        arquivo.write(a)
        arquivo.write(b)
        count = count + 1
        if count == 1:
            break
 with open(f"{id}.txt", "r") as aberto:
    aberto.seek(0)
    Lista_Com_Dados = list(aberto)
    return Lista_Com_Dados



cadastrar_usuario()