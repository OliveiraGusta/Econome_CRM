# Gustavo Rodrigues e Mateus Marana
appBanco = {
'usuarios': [],
'contas': []
}

#Função Cadastrar novo Clientes Cadastrados
def novoCliente(nome,senha,cpf,tipoConta):
    print()
    usuario = {
    'nome': nome,
    'senha': senha,
    'cpf' : cpf
    }
    conta = {
    'usuario': usuario,
    'saldo': 0,
    'tipoConta': tipoConta
    
    }
    appBanco['usuarios'].append(usuario)
    appBanco['contas'].append(conta)


#Função Apagar os Clientes Cadastrados
def apagarCliente(cpf):
    print()
    for i, usuario in enumerate(appBanco['usuarios']):
        if usuario['cpf'] == cpf:
            del appBanco['usuarios'][i]
            del appBanco['contas'][i]
            print("Usuário excluído com sucesso!")
        return
        print("Usuário não encontrado.")

#Função Exibir os Clientes Cadastrados
def listarClientes():
    print()
    for usuario in appBanco['usuarios']:
        print(f"Nome: {usuario['nome']}")
        print(f"Cpf: {usuario['cpf']}")

#Função Debitar Qualquer Valor
def debitarValor():
    print()
    print("Entrou na funcao Debitar Valor")

#Função Depositar Qualquer Valor
def depositaValor():
    print()
    print("Entrou na funcao Deposita Valor")

#Função Exibir Extrato da Conta
def extratoDaConta():
    print()
    print("Entrou na funcao Extrato da Conta ")
   
#Função Trasferir o Valor
def transferirValor(origem,destino,valor):
    print()
    conta_origem = None
    conta_destino = None

    for conta in appBanco['contas']:
        if conta['usuario']['nome'] == origem:
            conta_origem = conta
        if conta['usuario']['nome'] == destino:
            conta_destino = conta

        if conta_origem is None:
            print("Conta de origem não encontrada.")
        return
        if conta_destino is None:
            print("Conta de destino não encontrada.")
        return

        if conta_origem['saldo'] >= valor:
            conta_origem['saldo'] -= valor
            conta_destino['saldo'] += valor
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente para realizar a transferência.")
   
#Função para Acessar os Investimentos
def investimentos():
    print()
    print("Entrou na funcao Investimentos")
   
#Painel
while True:
    print('--------------------')
    print('$$ ECONO-ME BANK $$')
    print('--------------------')
    print()
    print(' Digite 1 - Cadastrar Novo Cliente  ')
    print(' Digite 2 - Apagar Cliente pelo Cpf')
    print(' Digite 3 - Listar os Clientes Existentes')
    print(' Digite 4 - Debitar um Valor na Conta')
    print(' Digite 5 - Depositar um Valor na Conta')
    print(' Digite 6 - Tirar Extrato')
    print(' Digite 7 - Transferir um Valor')
    print(' Digite 8 - Investir um Valor')
    print(' Digite 9 - Fechar o programa')
    print()
    decisao = input('O que Deseja?: ')
    
    if decisao == '1':  
        nome = input(" Digite o nome do usuário: ")
        cpf = input(" Digite o cpf do usuário:")
        tipoConta = input(" Digite o tipo da conta:")
        senha = input(" Digite a senha do usuário: ")
        novoCliente(nome, senha, cpf, tipoConta)
    
    if decisao == "2":
        cpf = input(" o cpf do usuário a ser excluído: ")
        apagarCliente(cpf)
    
    if decisao == '3': 
        listarClientes()
    
    if decisao == '4':
         debitarValor()
    
    if decisao == '5':
         depositaValor()
    
    if decisao == '6': 
        extratoDaConta()
    
    if decisao == '7':  
        origem = input(" o nome da conta de origem: ")
        destino = input(" o nome da conta de destino: ")
        valor = float(input(" o valor da transferência: "))
        transferirValor(origem, destino, valor)
    
    if decisao == '8': 
        investimentos()
    
    if decisao == '9': 
        break