rm2class = []
rm3class = []
rm4class = []
rm5class = []

studentName2 = []
studentName3 = []
studentName4 = []
studentName5 = []

Op2M1 = []
Op2M2 = []
Op2V1 = []
Op2V2 = []

def menu():
    print("-"*50)
    print("COLEGIO NOVA ESPERANÇA-EVENTO LITERARIO")
    print("-"*50)
    print(" ")
    print("***Menu de Opções***")
    print("1- Cadastrar Alunos")
    print("2- Fazer Inscrições")
    print("3- Listar Inscrições")
    print("4- Sair")
    print("********************")

    return int(input("Escolha a opção desejada, apenas o numero: "))

def studentsRegistration():
    while True:
        rm = int(input("Digite o rm do aluno: "))
        #validar quando deve sair do looping
        if rm ==0:
            break            
        elif rm!=0:
            #valida se o rm nao esta duplicado
            if rm not in rm2class and rm not in rm3class and rm not in rm4class and rm not in rm5class:
                #validando se a serie existe 
                studentClass = int(input("Digite a serie em que o aluno se encontra, apenas numero: "))
                while studentClass < 2 or studentClass > 5:
                    print("Série não encontrada!")
                    print("Só estão válidas da 2 a 5 serie!")
                    studentClass = int(input("Digite  a série do aluno: "))
                #iniciando o cadastro 
                if studentClass == 2:
                    rm2class.append(rm)
                    studentName2.append(input("Digite o nome do aluno: "))     
                elif studentClass == 3:    
                    rm3class.append(rm)
                    studentName3.append(input("Digite o nome do aluno: "))     
                elif studentClass == 4:   
                    rm4class.append(rm)
                    studentName4.append(input("Digite o nome do aluno: "))
                else:
                    rm5class.append(rm)
                    studentName5.append(input("Digite o nome do aluno: "))
                print("--Aluno Cadastrado--")
                print("--Proximo Aluno--")
            else: 
                print("Rm ja existente!")

def studentsSubscribe():
    print("")
    print("-"*50)
    print("REALIZANDO INSCRIÇÕES")
    print("-"*50)
    rm = int(input("Digite seu rm: "))
    #validando se o rm existe/foi cadastrado
    if rm in rm2class or rm in rm3class or rm in rm4class or rm in rm5class:
        #oficinas disponiveis para o segundo ano
        if rm in rm2class:
            print("***Oficinas Disponiveis***")
            print("****MATUTINO****")
            count = 0
            while count < 3:
            #verificando disponibilidade de oficinas
                if len(Op2M1) < 10: 
                    print("--Segunda-Feira-- Criar e contar histórias (Opção--> 1)")
                    print(f'Já foram realizadas {len(Op2M1)} inscrições!')
                    #quantas inscriçoes ja foram realizadas
                if len(Op2M2) < 10:
                    print("--Quarta-Feira-- A lingua dos sinais (Opção--> 2)")
                    print(f'Já foram realizadas {len(Op2M2)} inscrições!')
                print("****VESPERTINO****")
                if len(Op2V1) < 10:
                    print("--Quarta-Feira-- O mundo da imaginação (Opção--> 3)")
                    print(f'Já foram realizadas {len(Op2V1)} inscrições!')
                if len(Op2V2) < 10:
                    print("--Sexta-Feira-- Criando e recriando com emojis (Opção--> 4)")
                    print(f'Já foram realizadas {len(Op2V2)} inscrições!')
                print("Retorno ao menu --> 0")
                #solicitando que o usuario escolha uma opção
                opcao = int(input("Escolha uma opção --> "))
                #validando para que seja uma opção existente 
                while opcao < 0 or opcao > 4:
                    print("Opção invalida!")
                    opcao = int(input("Digite uma opção valida: "))
                if opcao == 1:
                    #verificando se o usuario ja esta cadastrado em tal oficina, se nao, cadastrar.
                    if rm not in Op2M1:
                        Op2M1.append(rm)
                        menu()
                    else: 
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 2:
                    if rm not in Op2M2:
                        Op2M2.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 3:
                    if rm not in Op2V1:
                        Op2V1.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 4:
                    if rm not in Op2V2:
                        Op2V2.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 0:
                    menu()
                count += 1
                print(f' Você ja realizou {count} inscrições!')

        
        #oficinas disponiveis para o terceiro ano
        elif rm in rm3class:
            print("***Oficinas Disponiveis***")
            print("****MATUTINO****")
            print("--Segunda-Feira-- Criar e contar histórias")
            print("--Terça-Feira-- Teatro: Luz, Câmera e Ação")
            print("--Quarta-Feira-- A lingua dos sinais")
            print("****VESPERTINO****")
            print("--Terça-Feira-- O corpo fala")
        #oficinas disponiveis para o quarto ano
        elif rm in rm4class:
            print("***Oficinas Disponiveis***")
            print("****MATUTINO****")
            print("--Terça-Feira-- Teatro: Luz, Câmera e Ação")
            print("--Quarta-Feira-- A lingua dos sinais")
            print("--Quinta-Feira-- Expressão Artística")
            print("****VESPERTINO****")
            print("--Segunda-Feira-- Leitura dramática")
        #oficinas disponiveis para o quinto ano 
        elif rm in rm5class:
            print("***Oficinas Disponiveis***")
            print("****MATUTINO****")
            print("--Quarta-Feira-- A lingua dos sinais")
            print("--Quinta-Feira-- Expressão Artística")
            print("--Sexta-Feira-- Soletrando")
            print("****VESPERTINO****")
            print("--Quinta-Feira-- Leitura dinâmica")
    else:
        print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")


        
while True:
    option = menu()
    while option < 1 or option > 4:
        print("Opção invalida!")
        option = int(input("Digite uma opção valida: "))
    if option == 1:
        studentsRegistration()
    elif option == 2:
        studentsSubscribe()
    elif option == 3:
        print("Em construção, aguarde nova atualização!")
    elif option == 4:
        break
        