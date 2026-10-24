roy = {
    "nome": "nenhum",
    "idade": 79,
    "vivo": True,
    "nomeado": False
}
while roy["vivo"]:
    if roy["idade"] >= 80:
        print("Você morreu zé da manga.")
        roy["vivo"] = False
    else:
        if roy["nomeado"] == False:
            print("Parabéns, você nasceu. Seu nome é Roy. Quer manter ou mudar?")
            while True:
                mntr_nome = input("manter nome? apenas sim ou não").lower().strip()
                if mntr_nome == "sim":
                    print("Nome mantido com sucesso!")
                    roy['nome'] = "roy"
                    roy['nomeado'] = True
                    break
                elif mntr_nome == "não":
                    print("Qual nome devo chamá-lo?")
                    roy["nome"] = input("Digite:")
                    roy["nomeado"] = True
                    break
                else:
                    print("Não consegui entender, poderia repetir?")
        else:
            print(f"Você tem {roy['idade']} anos deseja passar para o proximo ano?")
            print("Apenas sim ou não")
            passar = input("Digite")
            if passar == "não":
                print("poblema é teu vai sim tio")
                roy["idade"]+=1
            elif passar == "sim":
                print("passando")
                roy["idade"]+=1
            else:
                print("vai ser burro morto só de raiva.")
                roy["vivo"]= False