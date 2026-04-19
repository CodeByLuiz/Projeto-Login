usuarios = {}

def cadastrar():
    usuario = input("Digite um usuário: ")
    senha = input("Digite uma senha: ")
    
    usuarios[usuario] = senha
    print("Usuário cadastrado!")

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

while True:
    opcao = input("\n1 - Cadastrar\n2 - Login\n3 - Sair\nEscolha: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        break