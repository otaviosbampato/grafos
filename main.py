# em python, usamos snake_case.
# durante o código, aspas duplas "" serão usadas para output e input, 
# e aspas simples '' para definições e manipulações de tipos quaisquer.

import os # pra uso de comandos no terminal em funções diversas->(?)

def mostra_titulo():
  print(""" 
        
                                    
                ▄▄█████  ▐█████▄     ▐███         ██    ▄██
                ▐██████▀▀  ▐██▀███▌    █████       ▐███  █████
                ███▀       ▐██ ███▌    █████▌      ███████████
                ████▄▄     ▐██▐█████  ▐██▀███     ▐████████████
                ███████▄  ▐███▀▀███▌ ███▄████    ███ ████  ███▌
                    ▀▀████  ██▌  ███▌ ████████▌  ███▌  █▀   ████
                ███     ███  ███▄████ ▐██▌   ███▌ ███        ▐███
                ███████████  ███████  ▐██     ██▌▐██▌         ███▌
                ▀▀▀▀▀▀▀▀▀   ▀▀▀▀     ▀▀▀     ▀▀▀▐██


           ▄
          ▀
█▀█ ▀█▀ ▄▀█ █ █ █ █▀█   █▀ █▄▄ ▄▀█ █▀▄▀█ █▀█ ▄▀█ ▀█▀ █▀█   ▄▀█ █▄ █ █▀▄ █▀█ ▄▀█ █▀▄ █▀▀
█▄█  █  █▀█ ▀▄▀ █ █▄█   ▄█ █▄█ █▀█ █ ▀ █ █▀▀ █▀█  █  █▄█   █▀█ █ ▀█ █▄▀ █▀▄ █▀█ █▄▀ ██▄
                                     
                                ▄█ █▀█ ▄▀█
                                ░█ █▄█ █▀█
""")
  
def mostra_menu():
   print("""  

              
            MENU DE OPÇÕES
         
    0. Sair do programa

    V̲e̲r̲i̲f̲i̲c̲a̲r̲:
    1. Conexo
    2. Bipartido
    3. Euleriano
    4. Possui ciclo
            
    L̲i̲s̲t̲a̲r̲
    5. Componentes conexas
    6. Componentes fortemente conexas
    7. Uma trilha Euleriana
    8. Vértces de articulação
    9. Identificador das arestas ponte
            
    G̲e̲r̲a̲r̲
    10. Árvore de profundidade
    11. Árvore de largura
    12. Árvore geradora mínima
    13. Ordem topológica
    14. Valor do caminho mínimo entre dois vértices
    15. Valor do fluxo máximo
    16. Fecho transitivo
    """)

def recebe_grafo():
   grafo = input("\n\nDigite o grafo a manipular: ")
   mostra_menu()

def finaliza_programa():
   os.system("cls") # envia uma instrução ao terminal para que ele fique limpo.
   print("Programa finalizado.")

def verifica_conexo():
   pass

def verifica_bipartido():
   pass

def verifica_euleriano():
   pass

def verifica_ciclo():
   pass

def lista_conexos():
   # em ordem lexicográfica (?)
   pass

def lista_fortemente_conexos():
   pass

def lista_uma_trilha_euleriana():
#    priorizando a ordem lexicográfica dos vértices
   pass

def lista_vertices_de_articulacao():
   pass

def lista_id_arestas_fonte():
   pass

def gera_arvore_profundidade():
   pass

def gera_arvore_largura():
   pass

def gera_arvore_geradora_minima():
   pass

def gera_ordem_topologica():
#    não deve estar disponível em grafos não direcionados. tratar caso (não refazerei outra interface)
   pass

def gera_valor_caminho_minimo():
   pass

def gera_valor_fluxo_maximo():
   pass

def gera_fecho_transitivo():
   #    não deve estar disponível em grafos não direcionados. tratar caso (não refazerei outra interface)
   pass


def pega_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
    except ValueError:
        print("\n\nPor favor insira um número inteiro.")   # tratando inputs inválidos (char, string, float, etc.)
        volta_menu = input("Digite uma tecla pra voltar ao menu principal. ")
        if volta_menu:
           main()

    match opcao_escolhida:
       case 0: finaliza_programa()
       case 1: verifica_conexo()
       case 2: verifica_bipartido()
       case 3: verifica_euleriano()
       case 4: verifica_ciclo()
       case 5: lista_conexos()
       case 6: lista_fortemente_conexos()
       case 7: lista_uma_trilha_euleriana()
       case 8: lista_vertices_de_articulacao()
       case 9: lista_id_arestas_fonte()
       case 10: gera_arvore_profundidade()
       case 11: gera_arvore_largura()
       case 12: gera_arvore_geradora_minima()
       case 13: gera_ordem_topologica()
       case 14: gera_valor_caminho_minimo()
       case 15: gera_valor_fluxo_maximo()
       case 16: gera_fecho_transitivo()
       case _: finaliza_programa()

def interface():
    mostra_titulo()
    recebe_grafo()
    pega_opcao()

def main():
    interface()

if __name__ == "__main__":
   main()