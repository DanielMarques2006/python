opcao = 0

while opcao != 3:
    print('''    [ 1 ] Listar tarefas guardadas
    [ 2 ] Adicionar nova tarefa
    [ 3 ] Sair''')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        tarefas = open('arquivo.txt', 'r')
        print('\nMétodo readlines() : \n')
        print(tarefas.readlines())

print('App fechado')