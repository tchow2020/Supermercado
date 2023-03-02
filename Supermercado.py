"""
Faça uma lista de comprar com "listas"
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
buy_list = []
options = input(
    'Bem vindo ao Big\n\nSelecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()


while True:
    if options == 'i':
        insert_item = input('Digite o que você vai comprar: ')
        print('item adicionado com sucesso!')
        buy_list.insert(0, insert_item)
        options = input(
            'Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    elif options == 'a':
        remove_item = input('Digite qual item você vai apagar: ')
        try:
          # Pelo nome do item
          buy_list.remove(remove_item)
          print(f'o item {remove_item} foi removido com sucesso!')
        except ValueError:
          print('Item não removido!')
        except NameError:
          print('Item não encontrado!')

        options = input(
            'Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    elif options == 'l':
        if buy_list == []:
            print('Sacola vazia!')
        for i, nome in enumerate(buy_list):
            print(i, nome)
        options = input(
            'Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    elif options == 's':
        print('Obrigado por comprar as coisas no Big!')
        break

    elif len(options) > 1:
        print('um item por vez!')
        options = input(
            'Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    else:
        print('Selecione apenas as opções abaixo!')
        options = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
