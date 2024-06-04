while True:
    numero_cliente = input('\nESCREVA O NÚMERO QUE DESEJA ADICIONAR AO SEUS CONTATOS com o (DDD): \n- ')
    nome_cliente = input('\nESCREVA O NOME QUE DESEJA ADICIONAR AO SEUS CONTATOS: \n- ').upper()

    numero_cliente = '(' + numero_cliente[0:2] + ')' + numero_cliente[2:7] + ' - ' + numero_cliente[7:]

    with open('clientes.txt', 'a') as arquivo:
        arquivo.write(nome_cliente + ' - ' + numero_cliente + '\n')

    print("OBRIGADO, CLIENTE ADICIONADO A LISTA COM \033[0;30;42m SUCESSO \033[m")

    adicionar_outro = input("Deseja adicionar outro número? (sim/não): ")
    if adicionar_outro.lower() != 'sim' and adicionar_outro.lower() != 's':
        break
