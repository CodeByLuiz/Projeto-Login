import hashlib
import json

def criptografar(senha):
    return hashlib.sha256(senha.encode()).hexdigest()   

def salvar(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

def carregar():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except:
        return {}

def cadastrar():
    usuario = input("Usuário: ")
    senha = criptografar(input("Senha: "))
    
    usuarios[usuario] = senha
    salvar(usuarios)

def login():
    usuario = input("Usuário: ")
    senha = criptografar(input("Senha: "))
    
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login OK")
    else:
        print("Erro")


usuarios = carregar()

while True:
    opcao = input("\n1 - Cadastrar\n2 - Login\n3 - Sair\nEscolha: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        break