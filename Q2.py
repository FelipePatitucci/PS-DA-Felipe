#Q2

def main():
    valores = '12345678'
    alf = "abcdefgh"
    pos = input("Digite a posição inicial e final do cavalo: ")
    if 0 < abs(int(alf.index(pos[0])) - int(alf.index(pos[3]))) < 3 and 0 < abs(int(pos[1]) - int(pos[4])) < 3:
        #Se chegamos aqui, é porque o cavalo fez o movimento correto, agora checaremos se as casas existem
        if (pos[0] and pos[3] in alf) and (pos[1] and pos[4] in valores):
            #Nesse caso, as casas informadas existem no tabuleiro
            print('O movimento é válido!')
        else:
            print('O movimento é inválido!')
    else:
        print('O movimento é inválido!')
        
if __name__ == "__main__":
    main()