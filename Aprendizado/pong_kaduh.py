import pygame
rodando = True
#pontos
vencedor = "Erro 1109, tá achando que é o Gabriel para roubar assim?"
pts_player1 = 0
pts_player2 = 0
#cores
branco = (255,255,255)
vermelho = (255, 0,0)
azul = (0,0,255)
verde = (0,255,0)
#raquete geral
tmnho_rqt_largura = 15
tmnho_rqt_altura = 150
#raquete 1
cor_rqt1 = branco
x_rqt1 = 0 + tmnho_rqt_largura
y_rqt1 = 225 
#raquete 2
cor_rqt2 = branco
x_rqt2 = 790 - tmnho_rqt_largura
y_rqt2 = 225
#bolinha de Pong
x_bol = 400
y_bol = 300
raio_bol = 15
velx_bol = -5
vely_bol = -5
cor_bol = branco

def verificar_borda(borda_x, borda_y):
    global velx_bol, vely_bol, y_rqt1, y_rqt2, x_rqt1, x_rqt2, x_bol, y_bol, pts_player1, pts_player2, cor_bol
    if x_bol - raio_bol < 0:
        pts_player2 += 1
        velx_bol = 5
        x_bol = 400
        y_bol = 300
        cor_bol = branco
    elif x_bol + raio_bol > borda_x:
        pts_player1 += 1
        velx_bol = -5
        x_bol = 400
        y_bol = 300
        cor_bol = branco
    if y_bol - raio_bol < 0:
        vely_bol = 5
    elif y_bol + raio_bol > borda_y:
        vely_bol = -5
    if y_rqt1 < 0: 
        y_rqt1 = 0
    elif y_rqt1 + tmnho_rqt_altura > borda_y:
        y_rqt1 = borda_y - tmnho_rqt_altura
    if y_rqt2 < 0: 
        y_rqt2 = 0
    elif y_rqt2 + tmnho_rqt_altura > borda_y:
        y_rqt2 = borda_y - tmnho_rqt_altura
def verificar_colisao():
    global velx_bol, x_bol, cor_bol
    if (x_bol - raio_bol <= x_rqt1 + tmnho_rqt_largura) and (y_bol + raio_bol >= y_rqt1) and (y_bol - raio_bol <= y_rqt1 + tmnho_rqt_altura):
        if velx_bol < 0:
            velx_bol = 5
            x_bol = x_rqt1 + tmnho_rqt_largura + raio_bol
        if cor_rqt1 != branco:
            cor_bol = azul
    if (x_bol + raio_bol >= x_rqt2) and (y_bol + raio_bol >= y_rqt2) and (y_bol - raio_bol <= y_rqt2 + tmnho_rqt_altura):
        if velx_bol > 0:
            velx_bol = -5
            x_bol = x_rqt2 - raio_bol
        if cor_rqt2 != branco:
            cor_bol = vermelho
pygame.init()
fonte_placar = pygame.font.SysFont(None, 50)
fonte_fim = pygame.font.SysFont(None, 60)
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong: Kaduh Version")
clock = pygame.time.Clock()
while rodando:
    clock.tick(30)
    texto_placar = fonte_placar.render(f"Player 1:{pts_player1} Vs Player 2:{pts_player2}", True, branco)
    texto_fim_jogo = fonte_fim.render(f"Fim De jogo o {vencedor} Ganhou!", True, verde)
    tecla = pygame.key.get_pressed()
    tela.fill((0,0,0))
    tela.blit(texto_placar, (190, 20))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    if pts_player1 <= 4 and pts_player2 <= 4:
        pygame.draw.rect(tela, cor_rqt2,(x_rqt2, y_rqt2, tmnho_rqt_largura, tmnho_rqt_altura))
        pygame.draw.rect(tela, cor_rqt1,(x_rqt1, y_rqt1, tmnho_rqt_largura, tmnho_rqt_altura))
        y_bol += vely_bol
        x_bol += velx_bol
        pygame.draw.circle(tela, cor_bol,(x_bol, y_bol), raio_bol)
        if tecla[pygame.K_w]:
            y_rqt1 -= 8
        elif tecla[pygame.K_s]:
            y_rqt1 += 8
        if tecla[pygame.K_UP]:
            y_rqt2 -= 8
        elif tecla[pygame.K_DOWN]:
            y_rqt2 += 8
        if tecla[pygame.K_k]:
            cor_rqt1 = azul
            cor_rqt2 = vermelho
        elif tecla [pygame.K_b]:
            cor_rqt1 = branco
            cor_rqt2 = branco
            cor_bol = branco
        verificar_colisao()
        verificar_borda(800, 600)
        pygame.display.flip()
    else:
        velx_bol = 0
        vely_bol = 0
        if pts_player1 >= 5:
            vencedor = "Player 1"
        elif pts_player2 >= 5:
            vencedor = "Player 2"
        tela.blit(texto_fim_jogo, (90, 300))
        pygame.display.flip()
        if tecla[pygame.K_RETURN] or tecla[pygame.K_KP_ENTER]:
            pts_player1 = 0
            pts_player2 = 0
            velx_bol = -5
            vely_bol = -5
            y_rqt2 = 225
            y_rqt1 = 225


pygame.quit()