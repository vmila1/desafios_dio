# TODO: Crie uma classe UsuarioTelefone.  
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."
    
    def __repr__(self) -> str:
        return f"Usuário {self.nome} criado com sucesso"


# Entrada:
nome = input()  
numero = input()  
plano = input()  

usuario = UsuarioTelefone(nome=nome, numero=numero, plano=plano)

print(usuario)