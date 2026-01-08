








while  True :

    try :
        num1 = float(input('Digite o primeiro numero \n'))
        num2 = float(input('Digite o segundo numero \n'))
        print('Digite o operador (+-/*)')
        operador = input()
        resposta = ""

        if operador not in ('+','-','/','*'):
            print('Operador invalido')

        elif operador == '+':
            resultado = (num1 + num2)
            print(resultado)

        elif operador == '-':
            resultado = (num1 - num2)
            print(resultado)

        elif operador == '/':

            if  num2 == 0:
                 print('Nao é possivel fazer divisao por *zero* ')
            else:
                resultado = (num1 / num2)
                print(resultado)

        elif operador == '*':
            resultado = (num1 * num2)
            print(resultado)

        while resposta not in ('s', 'n'):

            resposta = input('Deseja fazer uma nova conta,[S]im ou [N]ao ? ').lower()
            if resposta not in ('s','n'):
                print('Resposta incorreta, digite apenas (Sim) ou (Nao) ')
            else:
                continue

        if resposta.startswith('s'):
            print('OK,Vamos nessa ')
        elif resposta.startswith('n'):
            print('Voce finalizou o sistema !!')
            break


    except ValueError :
        print('Digite apenas numeros válidos !!')






