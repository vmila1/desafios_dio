class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        saldo_atual = self.plano.verificar_saldo()

        if saldo_atual >= custo:
            self.plano.deduzir_saldo(custo)
            return (f"Chamada para {destinatario} realizada com sucesso. Saldo: R$ {self.plano.verificar_saldo():.2f}")
        else:
            return ("Saldo insuficiente para fazer a chamada.")


class Plano:
    CUSTO_POR_MINUTO = 0.10
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        return duracao * self.CUSTO_POR_MINUTO

    def deduzir_saldo(self, valor):
        self.saldo -= valor

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))