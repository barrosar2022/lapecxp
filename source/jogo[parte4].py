# Quarta parte do jogo
# Fazendo o fundo girar (carrocel)

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
   
    #variável para manter o jogo rodando em loop infinito
    executar = True

    #mantém o jogo rodando em loop até que seja fechada a janela
    while executar:
        #carrega imagem do fundo
        screen.blit(img_fundo,(0,0))
        #aguarda que x seja pressionado para sair do jogo
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                executar = False
                
        #carrossel
        x_rel = largura % img_fundo.get_rect().width
        screen.blit(img_fundo, (x_rel - img_fundo.get_rect().width,0))
        if x_rel < 1280:
            screen.blit(img_fundo, (x_rel, 0))
        
        largura = largura - 2

        pygame.display.update()

except:
    print('Erro em algum módulo do PyGame. Reinicie a aplicação.')
    pygame.quit()
