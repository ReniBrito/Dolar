dias = int(input('Quantos dias o carro foi alugado ? '))
km = float(input('Quantos KM o carro foi percorrido ? '))
aluguel = dias * 60 + km * 0.15
#rodado = km * 0.15

print('o total a pagar pelo aluguel é R$-{:.2f} '.format(aluguel))



