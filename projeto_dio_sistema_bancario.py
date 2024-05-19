"""
*COMENTARIO*
Sistema bancario implementando 3 operações - sacar - depositar - extrato 

"""
from datetime import datetime
saldo = 0
qde_saque = 0
extrato = list()
LIMITS_SAQUE = {'valor':500,'quantidade':3}
contador = {'valor':0,'quantidade':0}
hoje = datetime.now()
extrato.append(f"""
Extrado da Conta - Dio Bank
===========================
{hoje:%d/%m/%Y} {hoje:%H:%M}                            
""")

while True:
    opcao = str(input(f'''
    ___________________________________
    |        SISTEMA BANCARIO          |
    |▒▒▒▒▒▒▒▒  <<DIO BANK>>  ▒▒▒▒▒▒▒▒▒▒|                
    
    Data: {hoje:'%d/%m/%Y'}
    Saldo: R$ {saldo:.2f}

    Selecione uma Opção:
        Menu
            (d) - Deposito
            (s) - Saque
            (e) - Extrato
            (q) -  Sair

    '''
    ))
    match opcao:
        case 'd':
            try:
                valor = float(input("Informe o valor do Deposito:\n"))
                if valor <= 0:
                    print("Valor Incorreto, refaça a operação")
                    del valor
                                    
                else:
                    saldo+=valor
                    print(f"Deposito realizado com sucesso!\n")
                    print(f"Saldo: R$ {saldo:.2f}")
                    extrato.append(f"{hoje:%d/%m/%Y} {hoje:%H:%M} - Deposito realizado no valor de R$ {valor:.2f} - Saldo do dia: R$ {saldo:.2f}")
                    del valor
            except:
                print("O valor informado é inválido, tente novamente!")


        case 's':
            if contador['quantidade'] == 3:
                print("Limite de saque diario Atingido")
            else:        
                try:
                    valor =  float(input("Informe o Valor do saque:\n"))               
                    
                    if valor < 0:
                        print("Valor incorreto, refaça a operação!")

                    elif valor > LIMITS_SAQUE['valor']:
                        print("Saque Maior que o limite permitido, refaça a operação!")
                        del valor               
                    elif valor >= saldo:
                        print("Saque solicitado é igual a zero ou seu saldo é insuficiente! ")
                        print(f"Saldo dispónivel: R$ {saldo:.2f}")
                        del valor
                    else:
                        saldo -= valor
                        print("Saque realziado com sucesso!")
                        print(f"Saldo dispónivel: R$ {saldo:.2f}")
                        extrato.append(f"{hoje:%d/%m/%Y} {hoje:%H:%M} - Saque realizado no valor de R$ {valor:.2f} - Saldo do dia: R$ {saldo:.2f}")
                        contador['quantidade'] += 1
                        print(contador['quantidade'])
                        del valor
                except:
                        print("O valor informado é inválido, tente novamente")


        case 'e':
            if len(extrato) == 1:
                print(extrato[0])
                print("Extrato sem movimentações!")
                print(f"Saldo Atualizado: R$ {saldo:.2f}")
                print("===========================\n") 
            else:
                for item in extrato:
                
                    print(item)
                
                print("\n")    
                print(f"Saldo Atualizado: R$ {saldo:.2f}")
                print("====================\n")  

        case 'q':
            print("Obrigado por confiar em nossos Serviços, volte sempre!\n\n")
            break
        case _:
            print("Selecione um opção valida!")    


   
        

        



