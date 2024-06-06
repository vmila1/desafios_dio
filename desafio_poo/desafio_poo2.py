class PlanoTelefone():
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo

    @property
    def verificar_saldo(self):
        return self._saldo

def mensagem_personalizada(saldo):
    if saldo < 10:
        return 'Seu saldo está baixo. Recarregue e use os serviços do seu plano.'
    elif saldo >= 50:
        return 'Parabéns! Continue aproveitando seu plano sem preocupações.'
    else:
        return 'Seu saldo está razoável. Aproveite o uso moderado do seu plano.'

class UsuarioTelefone():
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        saldo = self.plano.verificar_saldo
        return saldo, mensagem_personalizada(saldo)


nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())


# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  


# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
