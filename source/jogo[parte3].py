# Terceira parte do jogo
# Inserindo as imagens de fundo do jogo

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

    img_fundo = pygame.image.load('figs/fundo.jpg').convert_alpha()
    img_fundo = pygame.transform.scale(img_fundo, (largura,altura))
    
    img_alien = pygame.image.load('figs/alien.png').convert_alpha()
    img_alien = pygame.transform.scale(img_alien, (50,50))
    
    img_aviao = pygame.image.load('figs/aviao.png').convert_alpha()
    img_aviao = pygame.transform.scale(img_aviao, (50,50))
    img_aviao = pygame.transform.rotate(img_aviao, -90)
    
    img_missil = pygame.image.load('figs/missil.png')
    img_missil = pygame.transform.scale(img_missil,(25,25))
    img_missil = pygame.transform.rotate(img_missil, -45)

    #variável para manter o jogo rodando em loop infinito
    executar = True

    #mantém o jogo rodando em loop até que seja fechada a janela
    while executar == True:
        screen.blit(img_fundo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executar = False
        
        pygame.display.update()

except:
    print('Erro em algum módulo do PyGame. Reinicie a aplicação.')
    pygame.quit()
