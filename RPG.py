import random


ouviu = 0
dragão_hp = 1
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
        print("Seja bem vindo, jogador, ao loma, você é um cavaleiro, e precisa matar um dragrão, que mora em um torre e está artomentando o reino, qual vai ser o seu nome?")
        while True:
            jogador['nome'] = input("Digite: ").strip()
            if jogador['nome'] == "":
                print("nome invalido, você precisas digitar um nome.")
            else:
                jogador["nomeado"] = True
                break
    else:
        while jogador["vivo"]:
            if jogador["hp"] <= 0:
                jogador["vivo"] = False
            else:
                print(f"{jogador['nome']}, seja bem vindo, a loma, a sua frente tem a batalha com o dragão, a sua direita você vê uma placa dizendo: 'caminho a ruina', a sua esquerda um penhasco.")
                while True:
                    print("1- Seguir reto e entrar na batalha com o Dragão")
                    print("2- Seguir para direita e ir para essa tal ruina.")
                    print("3- Pular no penhasco.")
                    caminho = input("Escolha um caminho:  ").strip()
                    if caminho == "1" :
                        print("Você entra e vê o dragrão e quando o dragrão te olha e da uma risada sincera, e diz:")
                        print("- tu veio aqui sem amardura sem nada, e acha que vai me matar? KSKSKSKSKSKSKSK")
                        print("ele tampa a saida com a cauda.")
                        print("então a batalha começa.")
                        while jogador["hp"] >0 and dragão_hp >0:
                            print("1- para atacar e 2 para curar")
                            turno = "0"
                            while turno == "0":
                                turno = "0"
                                turno = input("Digite: ").strip()
                                if turno == "1":
                                    dragão_hp -=1
                                    print(f"Seu hp:{jogador['hp']}")
                                    print(f"Hp dragrão:{dragão_hp}")
                                elif turno == "2":
                                    if jogador["hp"] >= 100:
                                        print(f"a vida está em {jogador['hp']}%, não é necessario cura")
                                    else:
                                        jogador["hp"] +=5
                                        print(f"Seu Hp{jogador['hp']}")
                                        print(f"Hp dragrão:{dragão_hp}")
                                else:
                                    print("Cara, tu tá sem porcaria nenhuma, e ainda quer matar um dragrão, escreve um numero errado? vou te dar mais uma chance para escrever certo.")
                                    turno="0"
                                if dragão_hp > 0:
                                    print("vez do dragrão")
                                    jogador["hp"] -= random.randint (3, 7)
                                    print(f"Seu hp{jogador['hp']}")
                                    print(f"Hp do dragrão:{dragão_hp}")
                                else:
                                    print("-Você me matou, como isso pode aconter?")
                        if jogador["hp"] <= 0:
                                print(f"ERA ÓBVIO, MAS ERA ÓBVIO. POR QUE NÃO FOI PARA O VILAREJO PRIMEIRO, MEU AMIGO? TÁ ACHANDO QUE É O BATMAN? TÁ ACHANDO QUE É TOJI POR ACASO? VOCÊ NÃO É NENHUM DELES; VOCÊ É O {jogador['nome']}")
                                print("Você morreu.")
                                break
                        else:
                                print("Que Deus tenha piedade de quem cruzar o seu caminho.")
                                print("Parabens você venceu, a que custo?")
                                jogador["vivo"] = False
                                break
                    elif caminho == "2" :
                        if jogador["ajudou_o_velho"] == False:
                            print("Ao caminho do vilarejo, você encontra um velho tentando sair de um circulo marcado no chão, ele te chama.")
                            print("1 - Para e ouvir o senhor")
                            print("2 - Continuar para o vilarejo ")
                            while True:
                                conversa = input("Digite: ").strip()
                                if conversa == "1":
                                    quico = True
                                    while quico:
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
                                                break
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
                                                print("vilarejo indisponivel")
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
                                                    print("vilarejo indisponivel")
                                                    quico = False
                                                    break
                                                else:
                                                    print("Digite um numero valido por favor.")
                                        elif ouviu == 1 and jogador["ajudou_o_velho"]:
                                            print("Ele te espanca até morrer e antes de você morrer ele fala:")
                                            print("- É assim o gosto da morte coverde.")
                                            print("'dev': merecido.")
                                            print("Você morreu. isso é bom?")
                                            jogador["vivo"] = False
                                elif conversa == "2":
                                    print("Vilarejo indisponivel.")
                                    break
                                else:
                                    print("Digite um numero valido por favor.")
                        else:
                            print("Vilarejo indisponivel.")
                    elif caminho == "3" :
                        print("Você se joga no penhasco e adivinha?")
                        print("Você morre, por quê você carambas você se jogou em um penhasco?")
                        jogador["hp"] = 0
                        break
                    else:
                        print("Digite um numero valido por favor.")
