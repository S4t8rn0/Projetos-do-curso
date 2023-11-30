print('Bem vindo, o que deseja?')
some= 's'
while some == 's':
    some = 'n'
    print ('O cardápio de hoje a seguir:')
    print('1- Macarrão ao molho branco. \n2- Lasanha de queijo com presunto. \n3- Bife à milanesa.\n')
    nn= input()
    if nn == '1':
        nn = 12
        print ('Será R$12,00.')

    elif nn == '2':
        nn= 14
        print('Será R$14,00')

    elif nn== '3':
        nn= 13
        print('Será R$13,00')
    
    else:
        print('Não reconheci, pode repetir?')

    print('Deseja alguma bebida? S|N')
    beb= input()
    if beb == 'S':
        print('Refrigerante(coca-cola, fanta, pepsi), suco (maracujá ou uva) ou água')
        bebi= input('Qual das bebidas?\n')
        if bebi == 'coca-cola' or 'fanta' or 'pepsi' or 'Coca-cola' or 'Coca' or 'Fanta' or 'Pepsi':
            print('Será R$5,00')
            beb = 5

        elif bebi == 'Suco de maracujá' or 'Suco de uva' or 'suco de maracujá' or 'suco de uva':
            print('Será R$7,00')
            beb= 7

        elif bebi == 'Água' or 'água':
            print('Será R$4,00')
            beb= 4

        else:
            print('Não reconheci, pode repetir?')

    if beb == 'N':
        beb= 0

    print('Seu pedido ficou:')
    print(nn + beb)
    some= input('Algo a mais? s|n:')

print('Ok, espero que goste. Tenha um bom dia.')
    