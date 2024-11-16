jogador1 = []
jogador2 = []

print("NOME DOS JOGADORES:")
jogador_1 = str(input("digite o seu nick (jogador 1):"))
jogador_2 = str(input("digite o seu nick (jogador 2):"))
print("")
print("PERGUNTAS DOS JOGADORES:")
pergunta_jogador1 = input(f"jogador {jogador_1} digite a sua pergunta:")
pergunta_jogador2 = input(f"jogador {jogador_2} digite a sua pergunta:")
print("")
print("RESPOSTAS DAS PERGUNTAS FEITAS:")
resposta_pergunta_1 = input(f"jogador {jogador_1} digite a resposta da pergunta que voce fez ao jogador {jogador_2}:")
resposta_pergunta_2 = input(f"jogador {jogador_2} digite a resposta da pergunta que voce fez ao jogador {jogador_1}:")
print("")
print("DICAS:")
dica_jogador1 = input(f"jogador {jogador_1} digite a sua dica:")
dica_jogador2 = input(f"jogador {jogador_2} digite a sua dica:")
print("")
print("PALPITES:")
palpite_jogador1 = input(f"jogador {jogador_1} digite o seu palpite da pergunta do jogador {jogador_2}:")
palpite_jogador2 = input(f"jogador {jogador_2} digite o seu palpite da pergunta do jogador {jogador_1}:")
print("")

tentativas_1=0
tentativas_2=0

while palpite_jogador1 != resposta_pergunta_2:
    tentativas_1+=1
    jogador1.append(palpite_jogador1)
    dica_jogador2 = input(f"jogador {jogador_2} digite outra dica:")
    palpite_jogador1 = input(f"{jogador_1} digite seu palpite novamente:")
    print("")
jogador1.append(palpite_jogador1)
tentativas_1+=1

while palpite_jogador2 != resposta_pergunta_1:
    tentativas_2+=1
    jogador2.append(palpite_jogador2)
    dica_jogador1ica_jogador1 = input(f"jogador {jogador_1} digite outra dica:")
    palpite_jogador2 = input(f"{jogador_2} digite seu palpite novamente:")
    print("")
jogador2.append(palpite_jogador2)
tentativas_2+=1



if  tentativas_1 == tentativas_2:
    jogador1.append(palpite_jogador1)
    jogador2.append(palpite_jogador2)
    print("essas foram as tentativas dos jogadores:")
    print(f"tentativas do jogador {jogador_1}",jogador1)
    print(f"tentativas do jogador {jogador_2}",jogador2)
    print("esse foi o numero de tentativas dos jogadores:")
    tentativas_1+=1
    tentativas_2+=1
    print(f"o jogador {jogador_1} tentou {tentativas_1} vez para acertar")
    print(f"o jogador {jogador_2} tentou {tentativas_2} vez para acertar")
    print("o resultado foi empate")

elif tentativas_1 < tentativas_2:
    print("essas foram as tentativas dos jogadores:")
    print(f"tentativas do jogador {jogador_1}",jogador1)
    print(f"tentativas do jogador {jogador_2}",jogador2)
    print("esse foi o numero de tentativas dos jogadores:")
    print(f"o jogador {jogador_1} tentou {tentativas_1} vez para acertar")
    print(f"o jogador {jogador_2} tentou {tentativas_2} vez para acertar")
    print(f"o jogador {jogador_1} foi o vencedor!!!")
    
elif tentativas_2 < tentativas_1:
    print("essas foram as tentativas dos jogadores:")
    print(f"tentativas do jogador {jogador_1}",jogador1)
    print(f"tentativas do jogador {jogador_2}",jogador2)
    print("esse foi o numero de tentativas dos jogadores:")
    print(f"o jogador {jogador_1} tentou {tentativas_1} vez para acertar")
    print(f"o jogador {jogador_2} tentou {tentativas_2} vez para acertar")
    print(f"o jogador {jogador_2} foi o vencedor!!!")