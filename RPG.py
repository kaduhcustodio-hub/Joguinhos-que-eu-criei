import random
import webbrowser

def vilarejo():
    ficar = True
    while ficar:
        print("Você chegou ao vilarejo")
        print("tá que nem a mente de quem faz 67 (vazia) quer ficar?")
        loli = input("Digite: ").strip().lower()
        if loli == "não":
            ficar = False
    
def batalhar_dragrão():
    while jogador["hp"] >0 and dragão["hp"] >0:
        print("1- para atacar e 2 para curar")
        turno = "0"
        while turno == "0":
            turno = "0"
            turno = input("Digite: ").strip()
            if turno == "1":
                dragão["hp"] -=1
                print(f"Seu hp:{jogador['hp']}")
                print(f"Hp dragrão:{dragão['hp']}")
            elif turno == "2":
                if jogador["hp"] >= 100:
                    print(f"a vida está em {jogador['hp']}%, não é necessario cura")
                else:
                    jogador["hp"] +=5
                    print(f"Seu Hp{jogador['hp']}")
                    print(f"Hp dragrão:{dragão['hp']}")
            else:
                if chance == 0:
                    if not jogador["tem_arma_e_amarmadura"]:
                        print("Cara, tu tá sem porcaria de arma e amardura nenhuma, e ainda quer matar um dragrão, escreve um numero errado? vou te dar mais uma unica chance para escrever certo.")
                        chance = 1
                else:
                 print("Digite um numero valido por favor.")    
                turno="0"
        if dragão["hp"] > 0:
            print("vez do dragrão")
            jogador["hp"] -= random.randint (3, 7)
            print(f"Seu hp{jogador['hp']}")
            print(f"Hp do dragrão:{dragão['hp']}")
        elif dragão["hp"] <0 or dragão["hp"] == 0:
                print("-Você me matou, como isso pode acontecer?")
    if jogador["hp"] <= 0:
        if jogador["ajudou_o_velho"]:
            print("Momentos antes de você morrer o bodybuilder aparece, mata o dragrão e te leva para a enfermaria do vilarejo, aonde você ficou bom.")
            print("Parabens você venceu!")
        elif jogador["matou_o_velho"]:
               print ("Graças a Deus você morreu, que queime no inferno.")
        elif jogador["tem_arma_e_amarmadura"] or jogador["tem_o_remedio_XL"]:
                print("Você morreu.")
        if jogador["matou_o_velho"]:
                print("uma pena que não foi antes.")
        elif jogador["ajudou_o_velho"]:
            print("Vai com Deus guerreiro.")        
        else:
            print(f"ERA ÓBVIO, MAS ERA ÓBVIO. POR QUE NÃO FOI PARA O VILAREJO PRIMEIRO PARA COMPRAR, MEU AMIGO? TÁ ACHANDO QUE É O BATMAN? TÁ ACHANDO QUE É TOJI POR ACASO? VOCÊ NÃO É NENHUM DELES; VOCÊ É O {jogador['nome']}")
        print("Você morreu.")
    elif dragão["hp"] <=0:
        if not jogador["tem_arma_e_amarmadura"]:
            print("Que Deus tenha piedade de quem cruzar o seu caminho.")
            print("Parabens você venceu, a que custo?")
        elif jogador["ajudou_o_velho"]:
            print("Parabens você e o bodybuilder vencenram!")
        else:
            print("Parabens você venceu!")
            jogador["vivo"] = False
    if jogador["hp"] <-500 or dragão["hp"]<-500:
        webbrowser.open("https://www.youtube.com/watch?v=kIte0CuJZ5E")
    jogador["vivo"] = False
    
chance = 0
ouviu = 0
dragão ={
    "hp": 1000,
}
jogador ={
    "nome": "",
    "remedio": 0,
    "hp": 100,
    "ouro": 0,
    "vivo": True,
    "nomeado": False,
    "ajudou_o_velho": False,
    "matou_o_velho": False,
    "tem_arma_e_amarmadura": False,
    "tem_o_remedio_XL": False    
}
while jogador["vivo"]:
    if jogador["nomeado"] == False:
        print("Seja bem vindo, jogador, você é um cavaleiro, e precisa matar um dragrão, que mora em um torre e está artomentando o reino, qual vai ser o seu nome?")
        while True:
            jogador['nome'] = input("Digite: ").strip().lower()
            if jogador['nome'] == "":
                print("nome invalido, você precisas digitar um nome.")
            elif jogador["nome"] == "67":
                print("volta pro roblox enzo.")
                jogador["vivo"] = False
                break
            elif jogador["nome"] == "sans":
                print("não.")
            elif jogador["nome"] == "toji":
                print("VOCÊ NÃO É O TOJI, VAI NA LOJA COMPRAR UMA ARMA INVES DE TENTAR ME SACANEAR!!")
            elif jogador["nome"] == "batman":
                print("O dev é o batman e não pode existir dois batman")
                print("Por isso você vai ter uma batalha com o dev.")
                print("'dev'- i'am batman")
                jogador["vivo"] = False
                print("Você morreu! e o dev é o batman")
                break
            elif jogador["nome"] == "papyrus":
                print("EU VOU PERMITIR!!!!")
            elif jogador["nome"] == "frisk":
                print(f"{jogador['nome']}, seja bem vindo, a sua frente tem a batalha com o dragão, a sua direita você vê uma placa dizendo: 'caminho ao vilarejo', a sua esquerda um buraco muito fundo.")
                print("1- Pular no buraco.")
                while True:
                    egg = input("Digite: ").strip().lower()
                    if egg == "1":
                        webbrowser.open("https://store.steampowered.com/app/391540/Undertale/")
                        print("ai ó o jogo que vc quer:")
                        print("Digite um nome para você no jogo sem bricadeira.")
                        break
                    elif egg == ("quero mudar o nome" or "mudar nome"):
                        print("Digite um nome para você no jogo sem bricadeira.")
                        break
                    else:
                        print("digite 1 para continuar")
            else:
                jogador["nomeado"] = True
                break
    else:
        while jogador["vivo"]:
            if jogador["hp"] <= 0:
                jogador["vivo"] = False
            else:
                print(f"{jogador['nome']}, seja bem vindo, a loma, a sua frente tem a batalha com o dragão, a sua direita você vê uma placa dizendo: 'caminho a ruina', a sua esquerda um buraco.")
                while jogador["vivo"]:
                    print("1- Seguir reto e entrar na batalha com o Dragão")
                    print("2- Seguir para direita e ir para o vilarejo.")
                    print("3- Pular no buraco.")
                    caminho = input("Escolha um caminho:  ").strip()
                    if caminho == "1" :
                        if jogador["ajudou_o_velho"] == False and jogador["tem_arma_e_amarmadura"] == False:
                            print("Você entra e vê o dragrão e quando o dragrão te olha e da uma risada sincera, e diz:")
                            print("- tu veio aqui sem amardura sem nada, e acha que vai me matar? KSKSKSKSKSKSKSK")
                            print("ele tampa a saida com a cauda.")
                            print("então a batalha começa.")
                            batalhar_dragrão()
                        elif jogador["ajudou_o_velho"]:
                            print("Você entra e vê o dragrão e quando o dragrão te olha e da uma risada sincera, e na hora que ele iria falar, chega o bodybuild que vc ajudou e dá uma voadora na cara dele, e sai correndo dizendo 'agora é com você meu amigo.'")
                            dragão["hp"] -= 500
                            print(f"-500  de 1000")
                            print(f"hp do dragrão: {dragão['hp']}")
                            print("-tú vai ver quando eu derrotar esse caboco, vai ser eu e você na moral. -disse o dragrão.")
                            print("então a batalha começa")
                            batalhar_dragrão()
                        else:
                            print("Você entra e vê o dragrão e quando o dragrão te olha, cerra os dentes e vai para cima de você")
                            print("ele tampa a saida com a cauda.")
                            batalhar_dragrão()

                    elif caminho == "2" :
                        if jogador["ajudou_o_velho"] == False:
                            print("Ao caminho do vilarejo, você encontra um velho tentando sair de um circulo marcado no chão, ele te chama.")
                            print("1 - Para e ouvir o senhor")
                            print("2 - Continuar para o vilarejo ")
                            while True:
                                conversa = input("Digite: ").strip()
                                if conversa == "1":
                                    quico = True
                                    while quico and jogador["vivo"]:
                                        if ouviu == 0 and jogador["ajudou_o_velho"] == False:
                                            print("- Jovem você poderia me ajudar?")
                                            print("- Tá vendo esse controle no chão? ele me deixou preso em um loop temporal, pore está falho, eu já tô nesse  loop a 2 semanas, e por conta da dilatação temporal eu envelheci 68 anos")
                                            print("-A cada 60 segundos eu volto")
                                            print("1- Ajudar")
                                            print("2- Matar")
                                            print("3- Fingir que não ouviu e ir para o vilarejo.")
                                            escolha = input("Digite").strip()
                                            if escolha == "1":
                                                print("Após entregar o controle para ele, ele volta a ter 24 anos sendo um body builder e te dá 100 de ouro")
                                                jogador["ajudou_o_velho"] = True
                                                jogador["ouro"] += 100
                                                ouviu = 1
                                                quico = False
                                            elif escolha == "2": #esse cara é um babaca.
                                                ouviu = 1
                                                print("Você ganhou 10 de ouro e perdeu o respeito do Dev.")
                                                jogador["ouro"] += 10
                                                while True:
                                                    print("ele volta após 60 segundo aonde estava quando você o viu pela primeira vez.")
                                                    jogador["matou_o_velho"] = True
                                                    print("matar ele novamente?")
                                                    print("1- Sim       2 - Não")
                                                    matar = input("Digite: ").strip()
                                                    if matar == "1":
                                                        print("Você ganhou 10 de ouro.")
                                                        jogador["ouro"] += 10
                                                    elif matar == "2":
                                                        print("você decide não mata-lo")
                                                        break
                                                    else:
                                                        print("um numero babaca.")
                                            elif escolha == "3":
                                                vilarejo()
                                                quico = False
                                                break
                                            else:
                                                print("Digite um numero valido por favor.")
                                        elif ouviu == 1 and jogador["ajudou_o_velho"] == False:
                                            print("Você olha o velho chorando.")
                                            print("1-Ajudar")
                                            print("2-Mata-lo novamente")
                                            print("3-Ir para o vilarejo.")
                                            escolha_2 =input("Digite: ").strip()
                                            while True:
                                                if escolha_2 == "1":
                                                    print("Após entregar o controle para ele, ele volta a ter 24 anos sendo um body buildero")
                                                    jogador["ajudou_o_velho"] = True
                                                    ajudou = True
                                                    break
                                                elif escolha_2 == "2": #esse cara merece morrer.
                                                    ouviu = 1
                                                    print("Você ganhou 10 de ouro e perdeu o respeito do Dev.")
                                                    jogador["ouro"] += 10
                                                    while True:
                                                        print("ele volta após 60 segundo aonde estava quando você o viu pela primeira vez.")
                                                        jogador["matou_o_velho"] = True
                                                        print("matar ele novamente?")
                                                        print("1- Sim       2 - Não")
                                                        matar = input("Digite: ").strip()
                                                        if matar == "1":
                                                            print("Você ganhou 10 de ouro.")
                                                            jogador["ouro"] += 10
                                                        elif matar == "2":
                                                            print("você decide não mata-lo")
                                                            break
                                                    else:
                                                            print("um numero babaca.")
                                                elif escolha_2 == "3":
                                                    vilarejo()
                                                    quico = False
                                                    break
                                                else:
                                                    print("Digite um numero valido por favor.")
                                        elif jogador["matou_o_velho"] and jogador["ajudou_o_velho"]:
                                            print("Ele te espanca até morrer e antes de você morrer ele fala:")
                                            print("- É assim o gosto da morte coverde.")
                                            print("'dev': merecido.")
                                            print("Você morreu. isso é bom?")
                                            jogador["vivo"] = False
                                    break
                                elif conversa == "2":
                                    vilarejo()
                                    break
                                else:
                                    print("Digite um numero valido por favor.")
                            break        
                        else:
                            vilarejo()
                    elif caminho == "3" :
                        print("Você se joga no buraco e adivinha?")
                        print("Você morre, por quê você carambas você se jogou em um buraco? tá achando que é Undertale?")
                        jogador["hp"] = 0
                        break
                    else:
                        print("Digite um numero valido por favor.")
