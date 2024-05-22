class Bebidas:
    estoque = []
    def __init__(self, nome, mililitros):
        self.nome = nome
        self.mililitros = mililitros

    @classmethod
    def adicionar_ao_estoque(cls):
        nome = input('Nome da bebida: ')
        mililitros = int(input('Volume da Garrafa em mL: '))
        quantidade_garrafas = int(input(f'Quantas garrafas de {nome} está adicionando ao estoque? '))
        mililitros_total = mililitros * quantidade_garrafas
        nova_bebida = cls(nome=nome, mililitros=mililitros_total)
        cls.estoque.append({
            'Bebida': nova_bebida.nome,
            'Volume': nova_bebida.mililitros
        })
        return nova_bebida
        
#bebida_adicionada = Bebidas.adicionar_ao_estoque()
#print(Bebidas.estoque)

if __name__ == '__main__':
    pass
