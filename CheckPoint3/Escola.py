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

Op3M1 = []
Op3M2 = []
Op3M3 = []
Op3V1 = []

Op4M1 = []
Op4M2 = []
Op4M3 = []
Op4V1 = []

Op5M1 = []
Op5M2 = []
Op5M3 = []
Op5V1 = []


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
            count = 0
            while count < 3:
                print("****MATUTINO****")
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
                    count = count - 1
                    menu()
                count += 1
                print(f' Você ja realizou {count} inscrições!')

        
        #oficinas disponiveis para o terceiro ano
        elif rm in rm3class:
            print("***Oficinas Disponiveis***")
            count = 0
            while count < 3:
                print("****MATUTINO****")
                #verificando disponibilidade de oficinas
                if len(Op3M1) < 10: 
                    print("--Segunda-Feira-- Criar e contar histórias (Opção--> 1)")
                    print(f'Já foram realizadas {len(Op3M1)} inscrições!')
                    #quantas inscriçoes ja foram realizadas
                if len(Op3M2) < 10:
                    print("--Terça-Feira-- Teatro: Luz, Câmera e Ação (Opção--> 2)")
                    print(f'Já foram realizadas {len(Op3M2)} inscrições!')
                if len(Op3M3) < 10:
                    print("--Quarta-Feira-- A lingua dos sinais (Opção--> 3)")
                    print(f'Já foram realizadas {len(Op3M3)} inscrições!')
                print("****VESPERTINO****")
                if len(Op3V1) < 10:
                    print("--Terça-Feira-- O corpo fala (Opção--> 4)")
                    print(f'Já foram realizadas {len(Op3V1)} inscrições!')
                print("Retorno ao menu --> 0")
                #solicitando que o usuario escolha uma opção
                opcao = int(input("Escolha uma opção --> "))
                #validando para que seja uma opção existente 
                while opcao < 0 or opcao > 4:
                    print("Opção invalida!")
                    opcao = int(input("Digite uma opção valida: "))
                if opcao == 1:
                    #verificando se o usuario ja esta cadastrado em tal oficina, se nao, cadastrar.
                    if rm not in Op3M1:
                        Op3M1.append(rm)
                        menu()
                    else: 
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 2:
                    if rm not in Op3M2:
                        Op3M2.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 3:
                    if rm not in Op3M3:
                        Op3M3.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 4:
                    if rm not in Op3V1:
                        Op3V1.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 0:
                    count = count - 1
                    menu()
                count += 1
                print(f' Você ja realizou {count} inscrições!')
                
        #oficinas disponiveis para o quarto ano
        elif rm in rm4class:
            print("***Oficinas Disponiveis***")
            count = 0
            while count < 3:
                print("****MATUTINO****")
                #verificando disponibilidade de oficinas
                if len(Op4M1) < 10: 
                    print("--Terça-Feira-- Teatro: Luz, Câmera e Ação (Opção--> 1)")
                    print(f'Já foram realizadas {len(Op4M1)} inscrições!')
                    #quantas inscriçoes ja foram realizadas
                if len(Op4M2) < 10:
                    print("--Quarta-Feira-- A lingua dos sinais (Opção--> 2)")
                    print(f'Já foram realizadas {len(Op4M2)} inscrições!')
                if len(Op4M3) < 10:
                    print("--Quinta-Feira-- Expressão Artística (Opção--> 3)")
                    print(f'Já foram realizadas {len(Op4M3)} inscrições!')
                print("****VESPERTINO****")
                if len(Op4V1) < 10:
                    print("--Segunda-Feira-- Leitura dramática (Opção--> 4)")
                    print(f'Já foram realizadas {len(Op4V1)} inscrições!')
                print("Retorno ao menu --> 0")
                #solicitando que o usuario escolha uma opção
                opcao = int(input("Escolha uma opção --> "))
                #validando para que seja uma opção existente 
                while opcao < 0 or opcao > 4:
                    print("Opção invalida!")
                    opcao = int(input("Digite uma opção valida: "))
                if opcao == 1:
                    #verificando se o usuario ja esta cadastrado em tal oficina, se nao, cadastrar.
                    if rm not in Op4M1:
                        Op4M1.append(rm)
                        menu()
                    else: 
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 2:
                    if rm not in Op4M2:
                        Op4M2.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 3:
                    if rm not in Op4M3:
                        Op4M3.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 4:
                    if rm not in Op4V1:
                        Op4V1.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 0:
                    count = count - 1
                    menu()
                count += 1
                print(f' Você ja realizou {count} inscrições!')
            
        #oficinas disponiveis para o quinto ano 
        elif rm in rm5class:
            print("***Oficinas Disponiveis***")
            count = 0
            while count < 3:
                print("****MATUTINO****")
                #verificando disponibilidade de oficinas
                if len(Op5M1) < 10: 
                    print("--Quarta-Feira-- A lingua dos sinais (Opção--> 1)")
                    print(f'Já foram realizadas {len(Op5M1)} inscrições!')
                    #quantas inscriçoes ja foram realizadas
                if len(Op5M2) < 10:
                    print("--Quinta-Feira-- Expressão Artística (Opção--> 2)")
                    print(f'Já foram realizadas {len(Op5M2)} inscrições!')
                if len(Op5M3) < 10:
                    print("--Sexta-Feira-- Soletrando (Opção--> 3)")
                    print(f'Já foram realizadas {len(Op5M3)} inscrições!')
                print("****VESPERTINO****")
                if len(Op5V1) < 10:
                    print("--Quinta-Feira-- Leitura dinâmica (Opção--> 4)")
                    print(f'Já foram realizadas {len(Op5V1)} inscrições!')
                print("Retorno ao menu --> 0")
                #solicitando que o usuario escolha uma opção
                opcao = int(input("Escolha uma opção --> "))
                #validando para que seja uma opção existente 
                while opcao < 0 or opcao > 4:
                    print("Opção invalida!")
                    opcao = int(input("Digite uma opção valida: "))
                if opcao == 1:
                    #verificando se o usuario ja esta cadastrado em tal oficina, se nao, cadastrar.
                    if rm not in Op5M1:
                        Op5M1.append(rm)
                        menu()
                    else: 
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 2:
                    if rm not in Op5M2:
                        Op5M2.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 3:
                    if rm not in Op5M3:
                        Op5M3.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 4:
                    if rm not in Op5V1:
                        Op5V1.append(rm)
                        menu()
                    else:
                        print("Opção já cadastrada, digite outra opção")
                        count = count - 1
                        opcao = int(input("---> "))
                elif opcao == 0:
                    count = count - 1
                    menu()
                count += 1
                print(f' Você ja realizou {count} inscrições!')
    else:
        print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")

def listRegistration():
    print("")
    print("-"*50)
    print("LISTA DE INSCRIÇÕES")
    print("-"*50)
        
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
        listRegistration()
    elif option == 4:
        break
        