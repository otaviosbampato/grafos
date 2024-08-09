# nota do autor

# forte ênfase nos comentários de código foi dada por mim nesse projeto, tanto a fins
# de visar a manutenibilidade e as boas práticas, quanto por fins de capricho e gosto pessoal.

# por mais que uma "modularização" em diferentes arquivos seria um padrão de projeto preferível,
# uma ambiguidade -- ou arguivelmente uma incapacidade da minha parte de compreender com clareza
# o enunciado do projeto -- na descrição do trabalho deu a mim o entendimento que um arquivo fonte
# unitário seria usado para testes que determinariam a avaliação daquele, e portanto decidi
# por assim fazê-lo. 

# em python, usamos snake_case.
# durante o código, aspas duplas "" serão usadas para outputs e inputs, 
# e aspas simples '' para definições e manipulações de tipos quaisquer.



# INÍCIO DO TRABALHO

import os # pra uso de comandos no terminal em funções diversas->(?)

def mostra_titulo():  # função pra mostar o título (e uma "assinatura") da aplicação.
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
  
def mostra_menu():  # função que mostra ao usuário as funcionalidades disponíveis no programa.
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

def recebe_grafo(): # criador do grafo. cria um dicionário "grafo" e passa a ele todos os dados do objeto.
   n_vertices, n_arestas = map(int, input("Digite a qtd de vértices e arestas: ").split())  # separa a entrada em 2 info diferentes.
   direcionado = True if input("O grafo é ou não direcionado? ") == 'direcionado' else False
   # direcionado = inp... provavelmente fazia o mesmo. mas assim fica mais legível.
   grafo = {i: [] for i in range(n_vertices)}  # para cada vértice no grafo criamos uma nova chave
   
   for _ in range(n_arestas): # vamos pegar os dados para cada aresta
        id_aresta, u, v, peso = map(int, input("Digite o id_aresta, u, v, e peso: ").split())   # NECESSARIAMENTE respeitar a ordem numérica (0, 1...)
        grafo[u].append((v, peso, id_aresta)) # na chave do vértice u ("pirncipal") adicionamos os valores do vértice com o qual ele se liga, a aresta que possibilita isso e o peso dessa.
        if not direcionado: # caso o grafo não seja direcionado, criamos uma relação bidirecional.
            grafo[v].append((u, peso, id_aresta))   
            
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
        input("Digite uma tecla pra voltar ao menu principal. ")
        return

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