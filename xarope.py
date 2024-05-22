class Xaropes:
    armario = []
    def __init__(self, nome, mililitros):
        self.nome = nome
        self.mililitros = mililitros

    @classmethod
    def adicionar_ao_armario(cls):
        nome = input('Sabor do xarope: ')
        mililitros = int(input('Volume em mL: '))
        quantidade_garrafas = int(input(f'Quantas garrafas de xarope de {nome} está adicionando ao estoque? '))
        mililitros_total = mililitros * quantidade_garrafas
        nova_bebida = cls(nome=nome, mililitros=mililitros_total)
        cls.armario.append({
            'Xarope': nova_bebida.nome,
            'Volume': nova_bebida.mililitros 
        })
        return nova_bebida
