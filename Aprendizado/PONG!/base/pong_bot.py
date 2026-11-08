import pygame
import random as rdm
pygame.init()
tecla = pygame.key.get_pressed()
rodando = True
altura_tela = 600
largura_tela = 800
#pontos
vencedor = "Erro 1109, tá achando que é o Gabriel para roubar assim?"
pts_player1 = 0
pts_player2 = 0
ultimo_chute = ""
penultimo_chute = ""
#cores
branco = (255,255,255)
vermelho = (255, 0,0)
azul = (0,0,255)
verde = (0,255,0)
roxo = (87,2,104)
#raquetes
rqt_E = False
rqt_T = False
rqt_D = False
rqt_C = False
#pontos
E_pts = False
D_pts = False
T_pts = False
C_pts = False
#config PONG!
Modo_doido = False
bip = pygame.mixer.Sound("bip.wav")
fonte_placar = pygame.font.SysFont(None, 50)
fonte_fim = pygame.font.SysFont(None, 60)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong: Kaduh Version")
clock = pygame.time.Clock()

class bolinha:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.raio = 15
        self.velx = -5
        self.vely = -5
        self.cor = branco
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)
    def mover(self):
        self.x += self.velx
        self.y += self.vely
        self.rect.x = self.x - self.raio
        self.rect.y = self.y - self.raio
    def desenhar(self):
        pygame.draw.circle(tela,branco,(self.x,self.y),self.raio)
    def verificar_borda(self):
        global C_pts,T_pts,D_pts,E_pts
        if self.rect.x <= 0 and self.velx < 0:
            if rqt_E:
                E_pts = True
            else:
                self.velx *= -1
                self.x = self.raio
        if self.rect.y <= 0 and self.vely < 0:
            if rqt_T:
                T_pts = True
            else:
                self.vely *= -1
                self.y = self.raio 
        if self.rect.x + self.raio >= largura_tela and self.velx > 0:
            if rqt_D:
                D_pts = True
            else:
                self.velx *= -1
                self.x = largura_tela - self.raio
        if self.rect.y + self.raio >= altura_tela and self.vely > 0:
            if rqt_C:
                C_pts = True
            else:
                self.vely *= -1
                self.y = altura_tela - self.raio
class raquete:
    def __init__(self,lugar,cor):
        global rqt_C,rqt_D,rqt_T,rqt_E
        self.lugar = lugar
        if isinstance(cor, (tuple,list)):
            self.cor = cor
        else:
            print("Error 202: Tipo errado para a operação (TypeError)")
            print("Cor definida como branca")
            self.cor = (255,255,255)
        if lugar == "direita" or lugar == "esquerda":
            self.altura_rqt = 150
            self.largura_rqt = 15
            if lugar == "direita":
                self.tecla_up = pygame.K_UP
                self.tecla_baixo = pygame.K_DOWN
                self.x = 775
                self.y = 225
                rqt_D = True
            elif lugar == "esquerda":
                self.tecla_up = pygame.K_w
                self.tecla_baixo = pygame.K_s
                self.x = 15
                self.y = 225
                rqt_E = True
            self.rect = pygame.Rect(self.x,self.y, 15, 150)
        elif lugar == "teto" or lugar == "chão":
            self.altura_rqt = 15
            self.largura_rqt = 150
            if lugar == "teto":
                self.tecla_up = pygame.K_o
                self.tecla_baixo = pygame.K_l
                self.x = 400
                self.y = 15
                rqt_T = True
            elif lugar == "chão":
                self.tecla_up = pygame.K_KP8
                self.tecla_baixo = pygame.K_KP2
                self.x = 400
                self.y = 570
                rqt_C = True
            self.rect = pygame.Rect(self.x,self.y,15,40)
        else:
            global rodando
            print("Erro 203: Valor inválido (ValueError)")
            rodando = False
    def verificar_borda(self):
        if self.lugar == "direita" or self.lugar == "esquerda":
            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y + self.altura_rqt > altura_tela:
                self.rect.y = altura_tela - self.altura_rqt
        if self.lugar == "teto" or self.lugar == "chão":
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x + self.largura_rqt > largura_tela:
                self.rect.x = largura_tela - self.largura_rqt
    def mover(self):
        if self.lugar == "direita" or self.lugar == "esquerda":
            if tecla[self.tecla_up]:
                self.rect.y -= 8
            elif tecla[self.tecla_baixo]:
                self.rect.y += 8
        if self.lugar == "teto" or self.lugar == "chão":
            if tecla[self.tecla_up]:
                self.rect.x -= 8
            elif tecla[self.tecla_baixo]:
                self.rect.x += 8
        self.verificar_borda()
    def desenhar(self):
        pygame.draw.rect(tela, self.cor,self.rect)

def louca_lavada_evita_paulada():
    louca = rdm.randint(0,1)
    if louca == 1:
        return -5
    elif louca == 0:
        return 5

def reiniciar_valores():
    global ultimo_chute,penultimo_chute
    bolinha_de_golfe.rect.x = 400
    bolinha_de_golfe.x = 400
    bolinha_de_golfe.rect.y = 300
    bolinha_de_golfe.y = 300
    bolinha_de_golfe.velx = louca_lavada_evita_paulada()
    bolinha_de_golfe.vely = louca_lavada_evita_paulada()
    ultimo_chute = ""
    penultimo_chute = ""
    #reniciar as raquetes
    if rqt_T:
        rqt4.rect.x = 400
    if rqt_C:
        rqt3.rect.x = 400
    if rqt_E:
        rqt2.rect.y = 225
    if rqt_D:
        rqt1.rect.y = 225
def marcar_pontos():
    global E_pts, D_pts,T_pts,C_pts,pts_player1,pts_player2,ultimo_chute
    if E_pts:
        if ultimo_chute != "esquerda":
            pts_player2 += 1
            if rqt1.nivel < 255:
                rqt1.nivel += 1
            reiniciar_valores()
        else:
            bolinha_de_golfe.velx *= -1
        E_pts = False
    if D_pts:
        if ultimo_chute != "direita":
            pts_player1 += 1
            if rqt2.nivel < 255:
                rqt2.nivel += 1
            reiniciar_valores()
        else:
            bolinha_de_golfe.velx *= -1
        D_pts = False
    if T_pts:
        if ultimo_chute != "teto":
            pts_player2 += 1
            reiniciar_valores()
        else:
            bolinha_de_golfe.vely *= -1
        T_pts = False
    if C_pts:
        if ultimo_chute != "chão":
            pts_player1 += 1
            reiniciar_valores()
        else:
            bolinha_de_golfe.vely *= -1
        C_pts = False
            
def colisao(): #agora eu vou ficar mentalmente insano.
    global ultimo_chute,penultimo_chute
    if bolinha_de_golfe.rect.colliderect(rqt1.rect):
        if bolinha_de_golfe.velx > 0:
            bolinha_de_golfe.velx *= -1
            if Modo_doido == False:
                if abs(bolinha_de_golfe.velx) < 10:
                    bolinha_de_golfe.velx -= 1
            else:
                if abs(bolinha_de_golfe.velx) < 45:
                    bolinha_de_golfe.velx -= 1
            bolinha_de_golfe.x = rqt1.rect.x - bolinha_de_golfe.raio
            bolinha_de_golfe.rect.x = rqt1.rect.x - bolinha_de_golfe.raio
            penultimo_chute = ultimo_chute
            ultimo_chute = "direita"
            bip.play()
    if bolinha_de_golfe.rect.colliderect(rqt2.rect):
        if bolinha_de_golfe.velx < 0:
            bolinha_de_golfe.velx *= -1
            if bolinha_de_golfe:
                if Modo_doido == False:
                    if abs(bolinha_de_golfe.velx) < 10:
                        bolinha_de_golfe.velx += 1
                else:
                    if abs(bolinha_de_golfe.velx) < 45:
                        bolinha_de_golfe.velx += 1   
            bolinha_de_golfe.x = rqt2.rect.x + rqt2.largura_rqt + bolinha_de_golfe.raio
            bolinha_de_golfe.rect.x  = rqt2.rect.x + rqt2.largura_rqt + bolinha_de_golfe.raio
            penultimo_chute = ultimo_chute
            ultimo_chute = "esquerda"
            bip.play()

class Nara(raquete):
    def __init__(self, lugar, cor, nivel = 255):
        super().__init__(lugar, cor)
        self.nivel = nivel
    def mover(self,bolinha):
        global Modo_doido
        self.difereca = abs(bolinha.y - self.rect.centery)
        if self.nivel >= 1 and self.nivel <= 9:
            if self.difereca >= 200 and bolinha.rect.x >= 400 and bolinha.velx > 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 3 
                elif bolinha.y < self.rect.centery:
                    self.rect.y -= 3
        if self.nivel >= 10 and self.nivel <= 19:
            if self.difereca >= 100 and bolinha.rect.x >= 400 and bolinha.velx > 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 5 
                elif bolinha.y < self.rect.centery:
                    self.rect.y -= 5 
        if self.nivel >= 20 and self.nivel <= 90:
            if self.difereca >= 80 and bolinha.rect.x >= 400 and bolinha.velx > 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 5
                elif bolinha.y < self.rect.centery:
                    self.rect.y -= 5
        if self.nivel >= 91 and self.nivel <= 200:
            if self.difereca >= 70 and bolinha.rect.x >= 400 and bolinha.velx > 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 6
                if bolinha.y < self.rect.centery:
                    self.rect.y -= 6
        if self.nivel >= 200 and self.nivel <= 254:
            if self.difereca >= 50 and bolinha.rect.x >= 400 and bolinha.velx > 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 10
                if bolinha.y < self.rect.centery:
                    self.rect.y -= 10
        if self.nivel >= 255:
            if self.difereca > 1 and bolinha.rect.x >= 400 and bolinha.velx > 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += abs(bolinha_de_golfe.velx) + 10
                if bolinha.y < self.rect.centery:
                    self.rect.y -= abs(bolinha_de_golfe.velx) + 10
                Modo_doido = True
class Nara2(raquete):
    def __init__(self, lugar, cor, nivel = 255):
        super().__init__(lugar, cor)
        self.nivel = nivel
    def mover(self,bolinha):
        global Modo_doido
        self.difereca = abs(bolinha.y - self.rect.centery)
        if self.nivel >= 1 and self.nivel <= 9:
            if self.difereca >= 200 and bolinha.rect.x <= 400 and bolinha.velx < 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 3 
                elif bolinha.y < self.rect.centery:
                    self.rect.y -= 3
        if self.nivel >= 10 and self.nivel <= 19:
            if self.difereca >= 100 and bolinha.rect.x <= 400 and bolinha.velx < 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 5 
                elif bolinha.y < self.rect.centery:
                    self.rect.y -= 5 
        if self.nivel >= 20 and self.nivel <= 90:
            if self.difereca >= 80 and bolinha.rect.x <= 400 and bolinha.velx < 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 5
                elif bolinha.y < self.rect.centery:
                    self.rect.y -= 5
        if self.nivel >= 91 and self.nivel <= 200:
            if self.difereca >= 70 and bolinha.rect.x <= 400 and bolinha.velx < 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 6
                if bolinha.y < self.rect.centery:
                    self.rect.y -= 6
        if self.nivel >= 200 and self.nivel <= 254:
            if self.difereca >= 50 and bolinha.rect.x <= 400 and bolinha.velx < 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += 10
                if bolinha.y < self.rect.centery:
                    self.rect.y -= 10
        if self.nivel >= 255:
            if self.difereca > 1 and bolinha.rect.x <= 400 and bolinha.velx < 0:
                if bolinha.y > self.rect.centery:
                    self.rect.y += abs(bolinha_de_golfe.velx) + 10
                if bolinha.y < self.rect.centery:
                    self.rect.y -= abs(bolinha_de_golfe.velx) + 10
                Modo_doido = True
        
bolinha_de_golfe = bolinha()
rqt1 = Nara("direita",verde)
rqt2 = Nara2("esquerda",vermelho)
while rodando:
    clock.tick(30)
    texto_placar = fonte_placar.render(f"Nara:{pts_player1} Vs Nara:{pts_player2}", True, branco)
    texto_fim_jogo = fonte_fim.render(f"Fim De jogo o {vencedor} Ganhou!", True, verde)
    tecla = pygame.key.get_pressed()
    tela.fill((0,0,0))
    tela.blit(texto_placar, (190, 20))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    if pts_player1 <= 255 and pts_player2 <= 255:
        bolinha_de_golfe.mover()
        bolinha_de_golfe.verificar_borda()
        bolinha_de_golfe.desenhar()
        rqt2.mover(bolinha_de_golfe)
        rqt1.mover(bolinha_de_golfe)
        rqt1.verificar_borda()
        rqt2.verificar_borda()
        rqt1.desenhar()
        rqt2.desenhar()
        colisao()
        marcar_pontos()
        pygame.display.flip()
    else:
        bolinha_de_golfe.velx = 0
        bolinha_de_golfe.vely = 0
        if pts_player1 >= 255:
            vencedor = "Nara Direita"
        elif pts_player2 >= 255:
            vencedor = "Nara Esquerda"
        tela.blit(texto_fim_jogo, (90, 300))
        pygame.display.flip()
        if tecla[pygame.K_RETURN] or tecla[pygame.K_KP_ENTER]:
            pts_player1 = 0
            pts_player2 = 0
            bolinha_de_golfe.velx = -5
            bolinha_de_golfe.vely = -5
            rqt2.rect.y = 225
            rqt1.rect.y = 225


pygame.quit()