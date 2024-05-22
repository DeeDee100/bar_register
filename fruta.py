class Frutas:
    fruteira = []
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    @classmethod    
    def adicionar_a_fruteira(cls):
       nome = input('Qual fruta deseja adicionar? ')
       quantidade = int(input(f'Quantas unidades de {nome} está adicionando? '))
       nova_fruta = cls(nome=nome, quantidade=quantidade)
       cls.fruteira.append({
           'Fruta' : nova_fruta.nome,
           'Unidades' : nova_fruta.quantidade
       }) 

nova_fruta = Frutas.adicionar_a_fruteira()

print(Frutas.fruteira)