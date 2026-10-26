import pygame
#cores
branco = (255,255,255)
preto = (0,0,0)
#jogador
tem_chave = False
chave_rect = pygame.Rect(100, 300, 40, 15)
#config
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
msg = ""
msg_porta_tempo = 0
while rodando:
    clock.tick(60)
    tecla = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_rect.collidepoint(evento.pos):
                if estado_jogo == "menu":
                    estado_jogo = "jogando"
            if porta_rect.collidepoint(evento.pos) and estado_jogo == "jogando":
                if tem_chave == False:
                    msg = "porta trancada!"
                if tem_chave:
                    estado_jogo = "vitoria"
            if chave_rect.collidepoint(evento.pos) and estado_jogo == "jogando":
                if tem_chave == False:
                    tem_chave = True
                    msg = "Você pegou a chave!"
                    msg_porta_tempo = 0
    if estado_jogo == "menu":
        tela.fill((0,0,0))
        pygame.draw.rect(tela,(255,255,255),botao_rect)
        tela.blit(Jogar, Jogar_rect)
    if estado_jogo == "jogando":
        tela.fill((0,0,55))
        pygame.draw.rect(tela,(139,65,0),porta_rect)
        pygame.draw.circle(tela,(94,44,0),(720,220),20)
        if msg != "":
            msg_rect = fonte.render(msg, True, (255,255,255))
            tela.blit(msg_rect, (350,20))
            msg_porta_tempo += 1
            if msg_porta_tempo >= 120:
                msg = ""
                msg_porta_tempo = 0
        if tem_chave == False:
            pygame.draw.rect(tela, (255, 255, 0), chave_rect)
    if estado_jogo == "vitoria":
        tela.fill((0,20,0))
        tela.blit(fonte.render("Parabens você venceu.", True, branco), (350, 60))
        tela.blit(fonte.render("Aperte enter, para voltar ao menu", True, branco), (350,20))
        if tecla[pygame.K_RETURN]:
            msg = ""
            msg_porta_tempo = 0 
            tem_chave = False
            estado_jogo = "menu"            
    elif not (estado_jogo == "vitoria" or estado_jogo == "jogando" or estado_jogo == "menu"):
        print("Erro 803: Não encontrado.")
    pygame.display.flip()
        