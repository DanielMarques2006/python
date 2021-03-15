opcao = 0
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

while opcao != 3:
    print(CYAN, '''   [ 1 ] Listar tarefas guardadas
    [ 2 ] Adicionar nova tarefa
    [ 3 ] Sair''')
    print("###" *10)
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        tarefas = open('arquivo.txt', 'r')
        listaDeTarefas = tarefas.readlines() 
        i = 0
        print(RED, "LISTA DE TAREFAS \n", RESET)
        while i < len(listaDeTarefas):
            print("Tarefa " , i + 1, ": ",listaDeTarefas[i].replace("\n", ""))
            i = i + 1

        tarefas.close()
    elif opcao == 2:
        print('\n')
        NovaTarefa = input("Digite a tarefa a se adicionar: ")
        tarefas = open('arquivo.txt', 'a')
        tarefas.write(NovaTarefa + "\n")
        print(GREEN, "Operação concluída com sucesso no arquivo " 
        + tarefas.name + " usando o modo de acesso " + tarefas.mode)
        tarefas.close()

        texto = open('arquivo.txt' ,'r')
        tarefas.close()
    
print(BLUE, 'App fechado')