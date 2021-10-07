v = float(input('Digite a distãncia da sua viagem: '))
if (v <= 200):
    print('O preço da sua viagem de {}Km será de R$'.format(v), v * 0.50)
else:
    print('O preço da sua de {}Km viagem será de R$'.format(v), v * 0.45)