import pygame
import random

pygame.init()

LARGURA, ALTURA = 600, 400 #tamanho da janela 
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake")

relogio = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 48)

TAMANHO_BLOCO = 20
cobra_x, cobra_y = 300, 200
comida_x, comida_y = 100, 100
velocidade_x, velocidade_y = 0, 0

corpo = []
comprimento = 0

cores_cobra =[(128, 0, 128), (0, 0, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0)]

a_correr = True
while a_correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            a_correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                velocidade_x, velocidade_y = TAMANHO_BLOCO, 0
            if evento.key == pygame.K_LEFT:  
                velocidade_x, velocidade_y = -TAMANHO_BLOCO, 0  
            if evento.key == pygame.K_UP:  
                velocidade_x, velocidade_y = 0, -TAMANHO_BLOCO  
            if evento.key == pygame.K_DOWN:  
                velocidade_x, velocidade_y = 0, TAMANHO_BLOCO  
            
    cobra_x += velocidade_x
    cobra_y += velocidade_y

    if cobra_x < 0 or cobra_x >= LARGURA or cobra_y < 0 or cobra_y >= ALTURA:
        a_correr = False

    for parte_x, parte_y in corpo[1:]:
        if cobra_x == parte_x and cobra_y == parte_y:
            a_correr = False

    corpo.insert(0, (cobra_x, cobra_y))
    corpo = corpo[:comprimento + 1]

    if cobra_x == comida_x and cobra_y == comida_y:
        comida_x = random.randrange(0, LARGURA, TAMANHO_BLOCO)
        comida_y = random.randrange(0, ALTURA, TAMANHO_BLOCO)
        comprimento += 1

    pygame.display.set_caption(f"Snake - Pontuação: {comprimento}")    
    
    tempo = pygame.time.get_ticks()
    pulso = 2 * abs((tempo // 100) % 10 - 5)
    tamanho_comida = TAMANHO_BLOCO - 10 + pulso

    cor_cobra = cores_cobra[comprimento % len(cores_cobra)]

    janela.fill((0, 0, 0))
    pygame.draw.rect(janela, (255, 0, 0), (comida_x, comida_y, tamanho_comida, tamanho_comida))
    pygame.draw.rect(janela, cor_cobra, (cobra_x, cobra_y, TAMANHO_BLOCO, TAMANHO_BLOCO))

    for parte_x, parte_y in corpo [1:]:
        pygame.draw.rect(janela, cor_cobra, (parte_x, parte_y, TAMANHO_BLOCO, TAMANHO_BLOCO))
    
    pygame.display.flip()
    relogio.tick(15)

print(f"Fim de Jogo! Pontuação final: {comprimento}")

for _ in range(3):
    janela.fill((0, 0, 0))
    pygame.display.flip()
    pygame.time.wait(200)

    pygame.draw.rect(janela, (255, 0, 0), (comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO))
    for parte_x, parte_y in corpo:
        pygame.draw.rect(janela, cor_cobra, (parte_x, parte_y, TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.display.flip()
    pygame.time.wait(200)

texto = fonte.render("GAME OVER", True, (255, 255, 255))
janela.blit(texto, (LARGURA // 2- 110, ALTURA // 2 - 24))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()