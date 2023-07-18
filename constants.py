import pygame

TELA_LARGURA = 500
TELA_ALTURA = 700

IMAGEM_CANO = pygame.transform.scale2x(
    pygame.image.load('./imgs/pipe.png'))
IMAGEM_CHAO = pygame.transform.scale2x(
    pygame.image.load('./imgs/base.png'))
IMAGEM_BACKGROUND = pygame.transform.scale2x(
    pygame.image.load('./imgs/bg.png'))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(
        './imgs/bird1.png')),
    pygame.transform.scale2x(pygame.image.load(
        './imgs/bird2.png')),
    pygame.transform.scale2x(pygame.image.load(
        './imgs/bird3.png')),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
