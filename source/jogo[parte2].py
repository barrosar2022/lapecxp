# Segunda parte do jogo
# Funcionalidades básicas para janela do jogo

import pygame
try:
    #inicia o pygame
    pygame.init()

    #largura e altura da janela
    largura = 1280
    altura = 720

    #variavel para armazenar a pontuação do jogo
    pontos = 0

    #variavel para armazenar a pontuação do jogo
    vidas = 4

    #velocidade do míssil
    velocidade_missil = 0

    #variável para o tiro
    fogo = False
    
    #configura a janela e o texto do jogo
    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption('Jogo Opala Space - IFPI campus Pedro II')

    #variável para manter o jogo rodando em loop infinito
    executar = True

    #mantém o jogo rodando em loop até que seja fechada a janela
    while executar == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executar = False



    pygame.display.update()

except:
    print('Erro em algum módulo do PyGame. Reinicie a aplicação.')
    pygame.quit()
