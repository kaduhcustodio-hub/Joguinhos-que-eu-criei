import random
import webbrowser

def ferreiro():
    if jogador["tem_arma_e_amarmadura"]:
        print("você já possui amardura não é necessario compra-lá novamente.")
    elif not jogador["tem_arma_e_amarmadura"]:    
        print("Você entra no ferreiro e encontra uma placa dizendo conjunto amardura e espada por 100 ouros")
        print("comprar?")
        print("1- Sim, 100 de ouro")
        print("2- Não")
        while True:
            comprar_amardura = input("Digite: ")
            if comprar_amardura == "1":
                if jogador["ouro"] >= 100:
                    print("Você compra a armadura e arma e se sente mais preparado para lutar contra o dragrão.")
                    print("Você sai do ferreiro.")
                    jogador["tem_arma_e_amarmadura"] = True
                else:
                    print("Você não possui dinheiro suficiente.")
                break
            elif comprar_amardura == "2":
                print("Não a mais nada para comprar, você sai do ferreiro.")
                break
            else:
                print("Digite um numero valido.")
                dragão["paciencia"] += 1
                if dragão["paciencia"] >= 10:
                    webbrowser.open("https://www.youtube.com/watch?v=Le8fc7vIaZU")
    else:
        webbrowser.open("https://www.youtube.com/watch?v=kIte0CuJZ5E")

def enfermaria():
        while True:
            if (jogador["ajudou_necessitado"] and jogador["ajudou_o_velho"]) and not jogador["tem_o_remedio_XL"]:
                if not jogador["tem_o_remedio_XL"]:
                    print("Ao entrar na enfermeria, você vê uma pessoa vestida de batman te chamando.")
                    print("Ir até ele?")
                    print("1- Sim")
                    print("2- Não")
                    while True:
                        receber_benção = input("Digite: ").strip().lower()
                        if receber_benção == "1":
                            print("Ao chegar perto ele conta que é o dev, e por te sido um otimo ser humano ele te dar uma benção.")
                            print("e então ele some.")
                            jogador["tem_o_remedio_XL"] = True
                            break
                        elif receber_benção == "2":
                            print("você vai até o balcão fingindo que não viu ele.")
                            break
                        elif receber_benção == "dev?":
                            print("Sim, é ele.")
                        else:
                            print("Digite um numero valido, por favor.")
            elif jogador["matou_o_velho"] and not jogador["ajudou_necessitado"]:
                print("todo as pessoas te olham com nojo de você.")
                print("Ao chegar, no balcão a unica pessoa lá é uma idosa.")
                print("Comprar remedio? Recupera 10 de hp")
                print("1- Comprar.")
                print("2- Sair da enfermaria.")
                while True:
                    velha_surda = input("Digite:")
                    if velha_surda == "1":
                        print("ela não te ouviu.")
                    elif velha_surda == "2":
                        print('ao sair, você ouve a idosa dizendo: "Tomara que morra.", e o dev concorda.')
                        break
                    else:
                        print("Para matar velho e recusar ajuda é bom, mas para escrever um numero não dá conta?")
                break
            else:
                print("Comprar remedio? recupera 10 de hp")
                print("1- Sim, 10 de ouro.")
                print("2-Não, sair da enfermaria")
                while True:
                    remedio = input("Digite: ")
                    if remedio == "1":
                        if jogador["ouro"] >= 10:
                            jogador["ouro"] -= 10
                            print("você comprou 1 remedio.")
                            print("comprar novamente?")
                            print("1-Sim    2-Não, sair da enfermaria")  
                        else:
                            print("Você não possui dinheiro suficiente.")
                    elif remedio == "2":
                        print("Você sai da enfermaria.")
                        break
                break
def vilarejo():
    if not jogador["viu_necessitado"]:
        print("Ao entrar na Vila você vê um homem pedindo socorro apôs quebrar o joelho")
        print("ajudar?")
        print("1- sim")
        print("2- não")
        jogador["viu_necessitado"] = True
        while True:
            ajudar = input("Digite: ")
            if ajudar == "1":
                print("Você ajudou o necessitado e o levou a enfermaria")
                jogador["ajudou_necessitado"] = True
                jogador["ouro"] += 50
                enfermaria()
                break
            elif ajudar == "2":
                break
            else:
                print("Digite um numero valido por favor.")
    ficar = True
    while ficar:
        print("Você chegou a vila, aonde deseja ir?")
        print("1- Ferreiro")
        print("2- Enfermaria")
        print("3- sair da vila")
        aonde_vila = input("Digite: ")
        if aonde_vila =="1":
            ferreiro()
        elif aonde_vila =="2":
            enfermaria()
        elif aonde_vila =="3":
            break
        else:
            print("Digite um numero valido, por favor.")

    
def batalhar_dragrão():
    while jogador["hp"] >0 and dragão["hp"] >0:
        print("1- para atacar e 2 para curar")
        turno = "0"
        while turno == "0":
            turno = "0"
            turno = input("Digite: ").strip()
            if turno == "1":
                if jogador["tem_arma_e_amarmadura"]:
                    dragão["hp"] -=50
                    print(f"Seu hp:{jogador['hp']}")
                    print(f"Hp dragrão:{dragão['hp']}")
                else:    
                    dragão["hp"] -=1
                    print(f"Seu hp:{jogador['hp']}")
                    print(f"Hp dragrão:{dragão['hp']}")
            elif turno == "2":
                if jogador["hp"] >= 100:
                    print(f"a vida está em {jogador['hp']}%, não é necessario cura")
                else:
                    if jogador["tem_o_remedio_XL"] and jogador["hp"] <= 10:
                        print("usar Benção do Dev?")
                        print("1- Usar")
                        print("2- Não usar")
                        while True:
                            usar_remedio_xl = input("Digite: ")
                            if usar_remedio_xl == "1":
                                jogador["tem_o_remedio_XL"] = False
                                jogador["hp"] += 90
                                print(f"Você usou um Benção do Dev sua vida está com {jogador['hp']}hp ")
                                break
                            elif usar_remedio_xl == "2":
                                break
                            else:
                                print("Digite um numero valido por favor.")
                    elif jogador["remedio"] >0 and jogador["hp"] <=90:
                        print(f"Você possui {jogador['remedio']} remedios usar um?")
                        print("1- Usar")
                        print("2- Não usar")
                        while True:
                            usar_remedio = input("Digite: ")
                            if jogador["matou_o_velho"]:
                                jogador["hp"] -= 1
                            elif usar_remedio == "1":
                                jogador["remedio"] -= 1
                                jogador["hp"] += 10
                                print(f"Você usou um remedio sua vida está com {jogador['hp']}hp ")
                                break
                            elif usar_remedio == "2":
                                break
                            else:
                                print("Digite um numero valido por favor.")
                    else:
                        jogador["hp"] +=5
                        print(f"Seu Hp{jogador['hp']}")
                        print(f"Hp dragrão:{dragão['hp']}")
                        if not jogador["tem_arma_e_amarmadura"]:
                            print("-O caba acha que vai me ganhar curando 5 de vida.")
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
            if jogador["tem_arma_e_amarmadura"]:
                jogador["hp"] -= random.randint (1, 3)
                print(f"Seu hp{jogador['hp']}")
                print(f"Hp do dragrão:{dragão['hp']}")
            else:
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
    "paciencia": 0
}
jogador ={
    "nome": "",
    "remedio": 0,
    "hp": 100,
    "ouro": 10,
    "vivo": True,
    "ajudou_necessitado": False,
    "viu_necessitado": False,
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
                                            escolha = input("Digite: ").strip()
                                            if escolha == "1":
                                                print("Após entregar o controle para ele, ele volta a ter 24 anos sendo um body builder e te dá 100 de ouro")
                                                jogador["ajudou_o_velho"] = True
                                                jogador["ouro"] += 100
                                                ouviu = 1
                                                quico = False
                                                vilarejo()
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
