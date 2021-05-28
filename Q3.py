#Q3

def main():
    valor = float(input('Digite o valor com duas casas decimais: '))
    pos = [100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.50,0.25,0.10,0.05,0.01] #Possibilidades
    minimo = [0 for i in pos]
    n1 = '\n' #Truque para quebrar linha em f-string
    fim = f"{n1}NOTAS:{n1}"
    for atual,qtde in zip(pos,minimo): #Vamos iterar as possibilidades e a quantidade ao mesmo tempo
        if valor >= atual: #Se nosso valor inserido for maior que a nota/moeda atual, vamos ver o quanto conseguimos desse valor
            qtde = int(valor // atual) #Vamos ver a quantidade máxima de notas/moedas que podemos usar 
            valor -= atual*qtde #Agora subtraimos o que já geramos do valor
            if atual > 1.00: #Se for nota
                fim += f"{qtde} nota(s) de R${atual: .2f}{n1}"
            elif atual <= 1.00 and 'MOEDAS' not in fim: #Se ainda não tivermos separado as moedas
                fim += f"{n1}MOEDAS:{n1}{qtde} moeda(s) de R${atual: .2f}{n1}"
            else: #Se for uma moeda
                fim += f"{qtde} moeda(s) de R${atual: .2f}{n1}"
    print(fim)
if __name__ == '__main__':
    main()