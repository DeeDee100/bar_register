import os
from cocktail import Drink
from bebida import Bebidas
from refrigerantes import Refrigerantes
from fruta import Frutas
from xarope import Xaropes

ingredientes = []
receitas = []

def finalizar_app():
    os.system('cls')
    print('Beba com moderação')


def exibir_titulo():
    print('Bar em Casa\n')

def exibir_opcoes():
    print('1 - Registrar Receita')
    print('2 - Incluir Ingrediente')
    print('3 - Listar Drinks Possíveis')
    print('4 - Listar Ingredientes')
    print('5 - Finalizar app\n')



def voltar_ao_menu():
    input('\nPressione qualque tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu()


def incluir_ingrediente():
    pass
    
def registrar_receita():
    drink_adicionado = Drink.criar_drink()
    receitas.append(Drink.carta_drinks[-1]) 
    voltar_ao_menu()

def listar_drinks():
    print(receitas)
    voltar_ao_menu()

def listar_ingredientes():
    print(ingredientes)
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1: 
            registrar_receita()
        elif opcao_escolhida == 2: 
            incluir_ingrediente()
        elif opcao_escolhida == 3: 
            listar_drinks()
        elif opcao_escolhida == 4:
            listar_ingredientes()
        elif opcao_escolhida == 5: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()