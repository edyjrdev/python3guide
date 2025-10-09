# Calcular fatorial de numero


# criar menu (loop infinito)
# saida 
sair='q'
while True: 
    print('Calculador de Fatorial')
    resposta = input('Digite um número: ')

    #tratar resposta
    if resposta==sair:
        print('Sem fatorial para calcular.')    
        break
    else:
        numero = int(resposta)
    fatorial = 1

    #calcular fatorial
    while numero > 0:
        fatorial = fatorial * numero
        numero = numero -1
    print('Fatorial de ', resposta, ' é ', fatorial, '.')

print('Fim da Calculadora')