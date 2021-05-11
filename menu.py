def leia_numeros():
    x = float(input('Digite um numero:'))
    y = float(input('Digite outro numero:'))
    return x, y

continua = True
while continua:

    print ('menu')
    print ('1 - soma de dois numeros')
    print ('2 - verificar se foi multado ou não')
    print ('3 - soma de dez numeros')
    print ('4 - sair')

    opcao = input('Digite uma opcao:')

    if opcao == '1':
        x, y = leia_numeros()
        z = x + y
        print(' {} + {} = {} '.format(x, y, z))
    elif opcao == '2':
        velocidade = float(input('Digite a velocidade em que voce estava:'))
        if velocidade >= 81: 
            print ('Voce foi multado')
        elif velocidade <= 80:
            print ('Voce nao foi multado')
    elif opcao == '3':
        soma = 0
        cont = 0
        for c in range(1, 11):
            num = int(input('Digite um {} numero: '.format(c)))
            soma = soma + num
            cont = cont + 1
        print('Voce informou {} numeros e a soma deles foi {}'.format(cont, soma))
    elif opcao == '4':
        print('Voce encerrou o programa, Bye.')
        continua = False
    else:
        print('opcao invalida!!!')
#####