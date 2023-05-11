# Gustavo Rodrigues e Mateus Marana

menu = [
    '--------------------',
    '$$ ECONO-ME BANK $$',
    '--------------------',
    '',
    'Usuarios',
    ' Digite 1 - Cadastrar Novo Cliente',
    ' Digite 2 - Apagar Cliente pelo Cpf',
    ' Digite 3 - Listar os Clientes Existentes',
    '',
    'Conta',
    ' Digite 4 - Debitar um Valor na Conta',
    ' Digite 5 - Depositar um Valor na Conta',
    ' Digite 6 - Tirar Extrato',
    ' Digite 7 - Transferir um Valor',
    ' Digite 8 - Investir um Valor',
    '',
    'Sair',
    ' Digite 9 - Fechar o programa',
    ''
]

appBanco = {
    'usuarios': [],
    'contas': []
}


def exibir_menu():
    for linha in menu:
        print(linha)


def novoCliente():
    nome = input(" Digite o nome do usuário: ")
    cpf = input(" Digite o CPF do usuário: ")
    tipoConta = input(" Digite o tipo da conta: ")
    senha = input(" Digite a senha do usuário: ")
    valor = float(input(" Digite o valor inicial da conta: "))

    cadastrarCliente(nome, senha, cpf, valor, tipoConta, )


# Função Cadastrar novo Clientes Cadastrados
def cadastrarCliente(nome, senha, cpf, valor, tipoConta):
    for usuario in appBanco['usuarios']:
        if usuario['cpf'] == cpf:
            print()
            print("CPF já cadastrado. O usuário não será cadastrado novamente.")
            return

    usuario = {
        'nome': nome,
        'senha': senha,
        'cpf': cpf
    }
    conta = {
        'usuario': usuario,
        'saldo': valor,
        'tipoConta': tipoConta
    }
    appBanco['usuarios'].append(usuario)
    appBanco['contas'].append(conta)
    print()
    print("Usuário cadastrado com sucesso!")
    print()


# Função Apagar os Clientes Cadastrados
def apagarCliente():
    cpf = input(" Digite o CPF do usuário a ser excluído: ")
    print()
    for i, usuario in enumerate(appBanco['usuarios']):
        if usuario['cpf'] == cpf:
            del appBanco['usuarios'][i]
            del appBanco['contas'][i]
            print("Usuário excluído com sucesso!")
            return
    print()
    print("Usuário não encontrado.")
    print()

# Função Exibir os Clientes Cadastrados


def listarClientes():
    print("------------------------------------------")
    print("|   Nome   |      CPF       |     Valor  |")
    print("------------------------------------------")
    for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
        nome = usuario['nome']
        cpf = usuario['cpf']
        saldo = conta['saldo']
        print(f"| {nome:<8} | {cpf:<14} |   R${saldo:<14}")
    print("------------------------------------------")


# Função Debitar Qualquer Valor


def debitarValor():
    print()
    print("Entrou na funcao Debitar Valor")

# Função Depositar Qualquer Valor


def depositaValor():
    print()
    print("Entrou na funcao Deposita Valor")

# Função Exibir Extrato da Conta


def extratoDaConta():
    print()
    print("Entrou na funcao Extrato da Conta ")

# Função Trasferir o Valor
def transferir():
    origem = input(" Digite o CPF da conta de origem: ")
    destino = input(" Digite o CPF da conta de destino: ")
    valor = float(input(" Digite o valor a ser transferido: "))
    transferirValor(origem, destino, valor)

def transferirValor(origem, destino, valor):
    print()
    conta_origem = None
    conta_destino = None

    for conta in appBanco['contas']:
        if conta['usuario']['cpf'] == origem:
            conta_origem = conta
        if conta['usuario']['cpf'] == destino:
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

# Função para Acessar os Investimentos
def investimentos():
    print()
    print("Entrou na funcao Investimentos")


# Painel
while True:

    exibir_menu()
    decisao = input('O que Deseja?: ')
    if decisao == '1': novoCliente()

    if decisao == "2": apagarCliente()

    if decisao == '3': listarClientes()

    if decisao == '4':
        debitarValor()

    if decisao == '5':
        depositaValor()

    if decisao == '6':
        extratoDaConta()

    if decisao == '7':
        transferir()

    if decisao == '8':
        investimentos()

    if decisao == '9': break
  
    
