class Drink:
    carta_drinks = []
    
    def __init__ (self, nome, copo, metodo_preparo, ingredientes):
        self.nome = nome
        self.copo = copo
        self.metodo_preparo = metodo_preparo
        self.ingredientes = ingredientes
    
    @classmethod
    def criar_drink(cls):
        nome = input('Nome do Drink: ')
        copo = input('Taça ou Copo: ')
        metodo_preparo = input('Método de preparo: ')
        numero_ingrediente = int(input('Quantos ingredientes: '))
        
        ingredientes = []
        for i in range(numero_ingrediente):
            ingrediente_nome = input(f'Nome do ingrediente {i + 1}: ')
            ingredientes.append(ingrediente_nome)
        
        novo_drink = cls(nome=nome, copo=copo, metodo_preparo=metodo_preparo, ingredientes=ingredientes)
        
        cls.carta_drinks.append({
            'Drink' : novo_drink.nome,
            'Método de preparo' : novo_drink.metodo_preparo,
            'Copo' : novo_drink.copo,
            'Ingredientes' : novo_drink.ingredientes
        })    
        
        return novo_drink

drink_adicionado = Drink.criar_drink()
print(Drink.carta_drinks)
