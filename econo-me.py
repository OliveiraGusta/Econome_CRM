## Gustavo Rogrigues e Mateus Marana

# Dicionário com os clientes // Chave = Cpf
# Lista outras informações

clientes = { }
informacoesClientes = []

## Função 1 

cpf = ""
nome = ""
conta = ""
valor = ""
senha = ""



def novoCliente():

    global cpf

    global nome
    global conta
    global valor
    global senha

    cpf = input('Digite o CPF do cliente: ')
    nome = input('Digite o nome completo do cliente: ')
    conta = input('Digite o tipo de conta: ')
    valor = input('Digite o valor inicial da conta: ')
    senha = input('Digite a senha do usuário: ')

    informacoesClientes.append(nome)
    informacoesClientes.append(conta)
    informacoesClientes.append(valor)
    informacoesClientes.append(senha)

    clientes[cpf] = informacoesClientes
   
    print('Usuario cadastrado com SUCESSO!!')
    return

# Função apagar cliente
def apagarCliente():
    print()
    cpf = input('Digite o CPF a ser deletado: ')
    for x in clientes:
        if x == cpf:
            remover = input("Deseja realmente apagar o ccleliente pertencente ao CPF %s \n \nDigite 1 para confirmar \n \nDigite 2 para confirmar cancelar\n" % (cpf) )
            if(remover == "1"):
               #Apagar
                print("Tudo bem, cliente com CPF %s removido" % (cpf)) 
                del clientes[cpf]
                break
            else:
                #Nao Apagar
                print("Tudo bem, cliente não removido")  
                break   
        else:
            #cpf nao existe
            print("CPF nao condiz a algum cliente cadastrado")
            break
        

# Função Exibir os Clientes Cadastrados
def listarClientes():
    if clientes == {}:
        print("Não há clientes cadastrados")
    else:
        print("Listagem de Clientes Cadastrados")
        print('--------------------')
        for x,y in clientes.items():
                print('CPF = %s : %s' % (x,y))
                break
    
    

# Funçã Debitar Qualquer Valor
def debitarValor():
    print()
    print("Entrou na funcao Debitar Valor")
    
# Funçã Depositar Qualquer Valor
def depositaValor():
    print()
    print("Entrou na funcao Deposita Valor")
    
#Função Exibir Extrato da Conta
def extratoDaConta():
    print()
    print("Entrou na funcao Extrato da Conta ")
   
#Função Trasferir o Valor
def transferirValor():
    print()
    print("Entrou na funcao Transferir Valor")
   
#Função para Acessar os Investimentos
def investimentos():
    print()
    print("Entrou na funcao Investimentos")
   

def sair():
    print()
    print("Obrigado por utilizar nosso programa")
    


#Painel
while True:
    print('--------------------')
    print('$$ ECONO-ME BANK $$')
    print('--------------------')
    print()
    print('Para Cadastrar Novo Cliente - Digite 1')
    print('Para Apagar Cliente pelo Cpf - Digite 2')
    print('Para Listar os Clientes Existentes - Digite 3')
    print('Para Debitar um Valor na Conta - Digite 4')
    print('Para Depositar um Valor na Conta - Digite 5')
    print('Para Tirar Extrato - Digite 6')
    print('Para Transferir um Valor -Digite 7')
    print('Para Investir um Valor - Digite 8')
    print('Para Fechar o programa - Digite 9')
    print()
    decisao = input('O que Deseja?: ')
    if decisao == '1': novoCliente()
    if decisao == '2': apagarCliente()
    if decisao == '3': listarClientes()
    if decisao == '4': debitarValor()
    if decisao == '5': depositaValor()
    if decisao == '6': extratoDaConta()
    if decisao == '7': transferirValor()
    if decisao == '8': investimentos()
    if decisao == '9': break