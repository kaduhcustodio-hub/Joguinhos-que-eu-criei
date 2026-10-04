import random

dragão_hp = 10
jogador ={
    "nome": "",
    "nomeado": False,
    "hp": 100,
    "vivo": True
}
while jogador["vivo"]:
    if jogador["nomeado"] == False:
        print("Seja bem vindo, jogador, ao loma, você é um cavaleiro, e precisa matar um dragrão, que mora em um torre e está artomentando o reino, qual vai ser o seu nome?")
        while True:
            jogador['nome'] = input("Digite: ")
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
                                print(f"ERA OBVIO, MAS ERA OBVIO, PQ NÃO FOI NA RUINA PRIMEIRO MEU AMIGO? TÁ ACHANDO QUE É O BATMAN? TÁ ACHANDO QUE É TOJI POR ACASO? VC NÃO É NENHUM DELES VC É O {jogador['nome']}")
                                print("você morreu.")
                                break
                        else:
                            print("que Deus tenha piedade de quem cruzar o seu caminho.")
                            print("parabens você venceu, a que custo?")
                            jogador["vivo"] = False
                            break
                    elif caminho == "2" :
                        print("caminho, indisponivel, por favor volte mais tarde")
                        print("você dá meia volta e volta para o inicio.")
                    elif caminho == "3" :
                        print("Você se joga no penhasco e adivinha?")
                        print("Você morre, por quê você carambas você se jogou em um penhasco?")
                        jogador["hp"] = 0
                        break
                    else:
                        print("Escolha um numero.")
