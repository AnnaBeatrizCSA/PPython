import threading
import time
import os

resposta = None
soma = 0

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Bem vindo ao quiz Mestre dos Saberes")
print("Escolha o tema desejado:\n 1-Matemática Básica\n 2-História do Brasil\n 3-Geografia\n 4-Língua Portuguesa\n 5-Filmes e Séries\n 6-Música")
escolha = int(input("Digite a escolha: "))
print("Escolha o nível:\n 1-Fácil\n 2-Médio\n 3-Difícil")
nivel = int(input("Digite a escolha: "))

def contador(tempo):
    for i in range(1, tempo + 1):
        if resposta is not None:
            return
        print(f"      {i} segundos...", end="\r")
        time.sleep(1)
    if resposta is None:
        print("\nTempo esgotado! Indo para a próxima pergunta...\n")

def ler_resposta():
    global resposta
    resposta = input("Opção: ")

def fazer_pergunta(pergunta, opcoes, correta, tempo_limite=10):
    global resposta, soma
    resposta = None

    limpar_tela()
    print("\n" + pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}- {opcao}")

    t_contador = threading.Thread(target=contador, args=(tempo_limite,), daemon=True)
    t_contador.start()

    t_input = threading.Thread(target=ler_resposta, daemon=True)
    t_input.start()

    t_input.join(timeout=tempo_limite)
    t_contador.join()

    if resposta is None:
        print("Você não respondeu a tempo!")
    else:
        try:
            questao = int(resposta)
            if questao == correta:
                soma += 1
            else:
                print("Resposta incorreta!")
        except ValueError:
            print("Entrada inválida! Resposta ignorada.")

if escolha == 1 and nivel == 1:
    print("Você selecionou Matemática Básica - Nível Fácil")
    fazer_pergunta("Quanto é 9 x 6?", ["56", "54", "60"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual é a metade de 64?", ["30", "40", "32"], correta=3, tempo_limite=10)
    fazer_pergunta("Quanto é 120 dividido por 10?", ["15", "10", "12"], correta=3, tempo_limite=10)

elif escolha == 1 and nivel == 2:
    print("Você selecionou Matemática Básica - Nível Médio")
    fazer_pergunta("Qual é a raiz quadrada de 144?", ["10", "12", "14"], correta=2, tempo_limite=10)
    fazer_pergunta("Resolva: 15 x 8", ["110", "120", "130"], correta=2, tempo_limite=10)
    fazer_pergunta("Quanto é 200 dividido por 4?", ["50", "60", "40"], correta=1, tempo_limite=10)

elif escolha == 1 and nivel == 3:
    print("Você selecionou Matemática Básica - Nível Difícil")
    fazer_pergunta("Qual é o valor de 2³ x 5?", ["30", "40", "50"], correta=2, tempo_limite=10)
    fazer_pergunta("Resolva: (50 ÷ 2) + (18 ÷ 3)", ["29", "34", "28"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual é a raiz cúbica de 27?", ["2", "3", "4"], correta=2, tempo_limite=10)

elif escolha == 2 and nivel == 1:
    print("Você selecionou História do Brasil - Nível Fácil")
    fazer_pergunta("Quem foi o primeiro presidente do Brasil?", ["Deodoro da Fonseca", "Getúlio Vargas", "Dom Pedro II"], correta=1, tempo_limite=10)
    fazer_pergunta("Em que ano o Brasil proclamou a independência?", ["1822", "1889", "1808"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem foi o 'Patriarca da Independência'?", ["José Bonifácio", "Tiradentes", "Pedro Álvares Cabral"], correta=1, tempo_limite=10)

elif escolha == 2 and nivel == 2:
    print("Você selecionou História do Brasil - Nível Médio")
    fazer_pergunta("Quem liderou a Inconfidência Mineira?", ["José Bonifácio", "Tiradentes", "Duque de Caxias"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual era o nome da capital do Brasil antes de Brasília?", ["Salvador", "Rio de Janeiro", "Belo Horizonte"], correta=2, tempo_limite=10)
    fazer_pergunta("Em que ano ocorreu a Proclamação da República?", ["1889", "1822", "1922"], correta=1, tempo_limite=10)

elif escolha == 2 and nivel == 3:
    print("Você selecionou História do Brasil - Nível Difícil")
    fazer_pergunta("Quem foi o presidente durante a Revolução de 1930?", ["Washington Luís", "Getúlio Vargas", "Juscelino Kubitschek"], correta=1, tempo_limite=10)
    fazer_pergunta("O que foi a Guerra de Canudos?", ["Revolta popular", "Conflito internacional", "Movimento abolicionista"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem assinou a Lei Áurea?", ["Princesa Isabel", "Dom Pedro II", "José Bonifácio"], correta=1, tempo_limite=10)

elif escolha == 3 and nivel == 1:
    print("Você selecionou Geografia - Nível Fácil")
    fazer_pergunta("Qual é a capital do Brasil?", ["São Paulo", "Brasília", "Rio de Janeiro"], correta=2, tempo_limite=10)
    fazer_pergunta("O Brasil está localizado em qual continente?", ["Europa", "América do Sul", "Ásia"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual é o maior estado brasileiro em área?", ["Amazonas", "São Paulo", "Mato Grosso"], correta=1, tempo_limite=10)

elif escolha == 3 and nivel == 2:
    print("Você selecionou Geografia - Nível Médio")
    fazer_pergunta("Qual é o rio mais extenso do Brasil?", ["São Francisco", "Amazonas", "Paraná"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual bioma ocupa a maior área do Brasil?", ["Amazônia", "Cerrado", "Pantanal"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual país faz fronteira com o Brasil?", ["Chile", "Equador", "Uruguai"], correta=3, tempo_limite=10)

elif escolha == 3 and nivel == 3:
    print("Você selecionou Geografia - Nível Difícil")
    fazer_pergunta("Qual é a altitude aproximada do Pico da Neblina?", ["2994 m", "2500 m", "3200 m"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual estado brasileiro é conhecido como 'celeiro do Brasil'?", ["Mato Grosso", "Paraná", "Goiás"], correta=1, tempo_limite=10)
    fazer_pergunta("O Aquífero Guarani é uma reserva de quê?", ["Petróleo", "Água doce", "Minérios"], correta=2, tempo_limite=10)

elif escolha == 4 and nivel == 1:
    print("Você selecionou Língua Portuguesa - Nível Fácil")
    fazer_pergunta("Qual é o plural de 'cão'?", ["Cães", "Cãos", "Cãez"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual palavra está escrita corretamente?", ["Excessão", "Exceção", "Exsseção"], correta=2, tempo_limite=10)
    fazer_pergunta("O verbo 'correr' está em qual conjugação?", ["Primeira", "Segunda", "Terceira"], correta=2, tempo_limite=10)

elif escolha == 4 and nivel == 2:
    print("Você selecionou Língua Portuguesa - Nível Médio")
    fazer_pergunta("Qual é o antônimo de 'feliz'?", ["Triste", "Contente", "Alegre"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual palavra é um adjetivo?", ["Rapidamente", "Bonito", "Correr"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual frase está correta?", ["Houveram problemas", "Houve problemas", "Houvera problemas"], correta=2, tempo_limite=10)

elif escolha == 4 and nivel == 3:
    print("Você selecionou Língua Portuguesa - Nível Difícil")
    fazer_pergunta("O que é uma oração subordinada adverbial?", ["Explica substantivo", "Expressa circunstância", "Indica ação principal"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual palavra está no grau aumentativo?", ["Cachorrão", "Cachorrinho", "Cachorro"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual é o sujeito na frase 'Chove muito'?", ["Oculto", "Indeterminado", "Inexistente"], correta=3, tempo_limite=10)

elif escolha == 5 and nivel == 1:
    print("Você selecionou Filmes e Séries - Nível Fácil")
    fazer_pergunta("Quem é o protagonista de 'Toy Story'?", ["Buzz Lightyear", "Woody", "Andy"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual herói é conhecido como 'Homem de Ferro'?", ["Tony Stark", "Bruce Wayne", "Steve Rogers"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual é o nome do ogro verde da DreamWorks?", ["Shrek", "Fiona", "Burro"], correta=1, tempo_limite=10)

elif escolha == 5 and nivel == 2:
    print("Você selecionou Filmes e Séries - Nível Médio")
    fazer_pergunta("Qual série tem o personagem Walter White?", ["Breaking Bad", "Stranger Things", "The Office"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem dirigiu 'Jurassic Park'?", ["Steven Spielberg", "James Cameron", "Christopher Nolan"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual é o vilão principal em 'Vingadores: Ultimato'?", ["Thanos", "Loki", "Ultron"], correta=1, tempo_limite=10)

elif escolha == 5 and nivel == 3:
    print("Você selecionou Filmes e Séries - Nível Difícil")
    fazer_pergunta("Em que ano foi lançado 'O Senhor dos Anéis: A Sociedade do Anel'?", ["2001", "2003", "1999"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem interpretou Coringa em 'O Cavaleiro das Trevas'?", ["Joaquin Phoenix", "Heath Ledger", "Jared Leto"], correta=2, tempo_limite=10)
    fazer_pergunta("Qual é o nome verdadeiro de Darth Vader?", ["Anakin Skywalker", "Luke Skywalker", "Obi-Wan Kenobi"], correta=1, tempo_limite=10)

elif escolha == 6 and nivel == 1:
    print("Você selecionou Música - Nível Fácil")
    fazer_pergunta("Quem canta 'Shape of You'?", ["Ed Sheeran", "Shawn Mendes", "Justin Bieber"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual banda ficou famosa com 'Bohemian Rhapsody'?", ["Queen", "The Beatles", "Nirvana"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem é conhecida como 'Rainha do Pop'?", ["Madonna", "Beyoncé", "Lady Gaga"], correta=1, tempo_limite=10)

elif escolha == 6 and nivel == 2:
    print("Você selecionou Música - Nível Médio")
    fazer_pergunta("Quem compôs 'Garota de Ipanema'?", ["Tom Jobim e Vinícius", "Caetano Veloso", "Chico Buarque"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual cantor é conhecido como 'Rei do Rock'?", ["Elvis Presley", "Michael Jackson", "Frank Sinatra"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem canta 'Blinding Lights'?", ["The Weeknd", "Bruno Mars", "Post Malone"], correta=1, tempo_limite=10)

elif escolha == 6 and nivel == 3:
    print("Você selecionou Música - Nível Difícil")
    fazer_pergunta("Qual compositor é conhecido por suas sinfonias, como a 9ª?", ["Beethoven", "Mozart", "Bach"], correta=1, tempo_limite=10)
    fazer_pergunta("Quem canta 'Smells Like Teen Spirit'?", ["Nirvana", "Pearl Jam", "Foo Fighters"], correta=1, tempo_limite=10)
    fazer_pergunta("Qual é o nome verdadeiro de Lady Gaga?", ["Stefani Germanotta", "Adele Adkins", "Robyn Fenty"], correta=1, tempo_limite=10)

else:
    print("Opção inválida de tema ou nível!")

print("\nSua pontuação final é:", soma)
