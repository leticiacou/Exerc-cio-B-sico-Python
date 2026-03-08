print("Gostaria de fazer sua conta no banco? ")
print("Opções:")
choice = input("1.Sim \n2.Não ")
print("")

if (choice == '2'):
    print("Ok, tenha um ótimo dia!")

elif(choice == '1'):

        nome = input("Qual seu nome completo? ")

        if len(nome) < 3:
            print("Nome inválido tente novamente ")
            exit()

        elif len(nome) >= 3:
            senha1 = input("Digite sua senha ") 
            senha2 = input("Confirme sua senha ")

            if len(senha1) <= 3:
                print("Senha fraca, tente novamente ")    
                exit()

            if (senha1 != senha2):
                print("As senhas não coicidem")
                exit()

            saldo = float(input("Digite seu saldo "))
            print("")

            if(saldo < 0):
                print("Saldo inválido") 
                exit()

            while True:
                print("")
                choice2 = input("O que deseja fazer agora \n1. Consultar Saldo \n2. Depositar \n3. Sacar \n4. Sair") 
                print("")

                if(choice2 == '1'):
                    print(saldo)

                elif(choice2 == '2'):
                    deposito = float(input("Quanto deseja depositar? ")) 
                    
                    if(deposito <= 0):
                        print("Depósito inválido, deposito mínimo não atingido")
                        exit()

                    saldo += deposito 

                elif(choice2 == '3'):      
                    saque = float(input("Quanto deseja sacar da sua conta? "))

                    if(saque > saldo):
                        print("Saque inválido, saldo insuficiente!")
                        exit()

                    saldo -= saque

                elif(choice2 == '4'):
                    exit()        
                  


                        