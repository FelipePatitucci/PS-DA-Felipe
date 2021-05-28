#Q1

def main():
    valor ,final = 0, []
    while True: #Vamos adicionar os número recebidos em um lista até que "f" apareça
        valor = input("Digite um número ou f: ")
        if valor == "f": #Quando "f" aparecer, retornamos a soma dos nums dividida pelo total de nums
            if final == []: #Não há como calcular média sem números
                print(None)
                break
            print(f"A média dos valores é {sum(final) / len(final)}")
            break #Suspendemos o loop
        final.append(int(valor))

if __name__ == "__main__":
    main()
