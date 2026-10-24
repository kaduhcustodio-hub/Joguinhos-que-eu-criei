import pygame

rodando = True
estado_jogo = "menu"
pygame.init()
tela = pygame.display.set_mode((1000, 400))
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 50)
botao_rect = pygame.Rect(400, 165, 200, 70)
Jogar = fonte.render("Jogar", True, (0,0,0))
Jogar_rect = Jogar.get_rect()
Jogar_rect.center = botao_rect.center
porta_rect = pygame.Rect(700,20,160,380)

while rodando:
    clock.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_rect.collidepoint(evento.pos):
                estado_jogo = "jogando"
    if estado_jogo == "menu":
        tela.fill((0,0,0))
        pygame.draw.rect(tela,(255,255,255),botao_rect)
        tela.blit(Jogar, Jogar_rect)
    if estado_jogo == "jogando":
        tela.fill((0,0,55))
        pygame.draw.rect(tela,(139,65,0),porta_rect)
        pygame.draw.circle(tela,(94,44,0),(720,220),20)
    pygame.display.flip()
        