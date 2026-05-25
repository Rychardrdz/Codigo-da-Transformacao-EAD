class LoginInvalidoError(Exception):
    pass

def sistema_login():
    credenciais_corretas = {"usuario": "admin", "senha": "123"}
    tentativas = 3

    print("--- Sistema de Login ---")
    
    while tentativas > 0:
        try:
            user = input("Usuário: ")
            pw = input("Senha: ")

            if user != credenciais_corretas["usuario"] or pw != credenciais_corretas["senha"]:
                tentativas -= 1
                raise LoginInvalidoError(f"Credenciais incorretas. Tentativas restantes: {tentativas}")
            
            print("\nLogin bem-sucedido! Bem-vindo ao sistema.")
            break

        except LoginInvalidoError as e:
            print(e)
            if tentativas == 0:
                print("Acesso bloqueado. Procure o administrador.")

sistema_login()