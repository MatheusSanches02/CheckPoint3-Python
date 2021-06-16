rm2class = []
rm3class = []
rm4class = []
rm5class = []

studentName2 = []
studentName3 = []
studentName4 = []
studentName5 = []

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
    if rm in rm2class or rm in rm3class or rm in rm4class or rm in rm5class:
        if rm in rm2class:
            print("***Oficinas Disponiveis***")
            
while True:
    option = menu()
    while option < 1 or option > 4:
        print("Opção invalida!")
        option = int(input("Digite uma opção valida: "))
    alreadyDone = False
    if option == 1:
        if alreadyDone == False:
            studentsRegistration()
            alreadyDone = True
        else:
            print("Essa opção ja foi solicitada, tente outra opção!")
    elif option == 2:
        studentsSubscribe()
    elif option == 4:
        break
        