'''#O RPG DO MAL'''

#importando as classes e objetos criados (variaveis dos personagens)
from rpgclasses import*

def intro():
    global lugar, inicio, quest, quest2
    inicio = 1
    quest = 0
    quest2 = 1
    print(narrador + 'Você acorda no meio de uma floresta, apenas com um desejo insaciável de se aventurar.')
    jogador.nome = input('Qual o seu nome grande aventureiro? ')
    print('Ahh, então você é',jogador.cor+jogador.nome,narrador+'...')
    time.sleep(0.5)
    print('Que nome bobo. Enfim, sua jornada começa agora...')
    time.sleep(0.5)
    print('Kkkk,',jogador.cor+jogador.nome,narrador+'. Aiai, esses jovens de hoje em dia, senhor.')
    time.sleep(1)
    lugar = 'florestadasalmasperdidas()'
    eval(lugar.lower())

#função para escolher para onde o player irá dentre os lugares na lista
def viagem():
    global lugar
    lugares = ['Floresta das Almas Perdidas', 'Vila Curuçá', 'Lago das Águas Passadas']
    print(narrador+"Há uma placa com os seguintes lugares:")
    time.sleep(0.3)
    for i in range(len(lugares)):
        print("    "+f"{i+1}.",lugares[i])
        time.sleep(0.2)
    time.sleep(0.1)
    j=0
    print('Para onde desejas ir, nobre viajante?')
    destino = input('[Digite o nome completo do lugar ou seu índice - S para sair]: ')
    while j != len(lugares):
        if destino.lower() in map(str.lower, lugares) or destino in (f"{i}" for i in range(1,len(lugares)+1)):
            if destino.lower() == lugares[j].lower() or destino == str(j+1):
                print(f'Você decide caminhar até {lugares[j]}.')
                lugar = lugares[j]
                lugar = lugar.replace(' ', '')+'()'
                break
            elif destino.lower() != lugares[j].lower() and destino != str(j+1):
                j+=1
        elif destino.lower() == 's':
            break
        else:
            print('Aprenda a ler e decida ir pra algum lugar existente, por favor.')
            time.sleep(0.28)
            print('Para onde desejas ir, nobre viajante?')
            destino = input('[Digite o nome completo do lugar ou seu índice - S para sair]: ')
    print('aleluia')
    print(lugar.lower())
    eval(lugar.lower())
    time.sleep(1)

def florestadasalmasperdidas():
    global inicio, quest, quest2, primeiro_combate
    print('A floresta tem um ar misterioso. O que deseja fazer, incrível aventureiro? ')
    acao = input('1. Caminhar\n2. Cantar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    i = 0
    while i != 1:
        if acao.lower() == 'caminhar' or acao == '1':
                if inicio == 1:
                    print('Ao caminhar pelo local, você avista uma moça e uma criança colhendo ervas.')
                    time.sleep(1)
                    print('Se aproximando delas, seus olhos treinados avistam um duende claramente com inteção de atacá-las.')
                    time.sleep(1.5)
                    print('O que deseja fazer?')
                    acao2 = input('1. Atacar o duende\n2. Deixar acontecer\n[Digite o índice da ação]: ')
                    check = 0
                    while check != 1:
                        if acao2.lower() == '1':
                            print('Você segura a sua espada de madeira que carregava na cintura esse tempo todo e se joga na frente do duende.')
                            time.sleep(3.5)
                            inimigo.nome = duendes[0]
                            primeiro_combate = 1
                            combate()
                            primeiro_combate = 0
                            time.sleep(0.35)
                            print(narrador+'Você vence seu adversário e consegue garantir a segurança da moça e da criança.')
                            time.sleep(2.5)
                            check += 1
                        elif acao2.lower() == '2':
                            print('Você apenas observa a criatura atacar a moça enquanto ela protege a criança com seu próprio corpo.')
                            time.sleep(4)
                            print('Depois de um tempo, os gritos de agonia param e a criatura foge levando a cesta de ervas da moça.')
                            time.sleep(4)
                            print('Você fica parado ouvindo o choro da criança.')
                            print('Ela grita: "Mamãe!"\n"Mamãe, acorde por favor!"')
                            time.sleep(4)
                            print('Ao presenciar essa cena, seu corpo começa a vagar pela floresta sem rumo, nunca conseguindo sair dela.')
                            time.sleep(4)
                            print('Minutos se transformam em horas, horas se transformam em dias, dias se transformam em meses.')
                            time.sleep(4)
                            print('Seu corpo cai no chão, não conseguindo mais se mover de exaustão.')
                            time.sleep(4)
                            print('Você finalmente recobra a consciência, como se até então estivesse em um transe.')
                            time.sleep(4)
                            print('Em seus últimos suspiros, você sente como se a sua alma estivesse escapando pela sua boca, para continuar vagando.')
                            time.sleep(4)
                            print('Seus olhos se fecham... A floresta pune aqueles sem propósito.')
                            time.sleep(4)
                            print('Final 1/6')
                            check += 1
                            i+=1
                            raise SystemExit(0)
                    print('Moça: Obrigada, jovem aventureiro(a), por sua ajuda. Graças a você, minha filha e eu estamos sã e salvas.')
                    time.sleep(4)
                    print('Matilda: Chamo-me Matilda, e essa é a minha filha Flora.')
                    time.sleep(3)
                    print('Matilda: Por favor, se lhe for de seu agrado, visite-nos em nossa vila para que assim eu possa te agradecer propriamente.')
                    time.sleep(6)
                    print('Assim Matilda e Flora recolhem seus pertences e caminham para casa.')
                    time.sleep(3)
                    inicio = 0
                    quest = 1
                else:
                    if randint(1,3) == 1:
                        escolher_inimigo_comum()
                        combate()
                        time.sleep(0.35)
                        print(narrador+'Você vence seu adversário e prossegue na sua jornada.')
                    time.sleep(0.2)
                    print('Você caminha e caminha, mas nada encontra. Parece que os devs esqueceram de colocar alguma coisa aqui.')
        elif acao.lower() == 'cantar' or acao == '2':
                print('O seu magnificamente horrendo canto atrai uma alcateia de lobos que acham que você é um petisco.\nVocê corre e corre até despistá-los.')
                time.sleep(3)
        elif acao.lower() == 'viajar' or acao == '3':
                viagem()
                break
        else:
            print('Escolhe alguma coisa logo, porra.')
        print('O que deseja fazer?')
        acao = input('1. Caminhar\n2. Cantar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    
def vilacuruçá():
    global quest, quest2
    print('Você vê as pessoas andando pela vila pacificamente. O que deseja fazer, incrível aventureiro? ')
    acao = input('1. Conversar\n2. Atacar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    i = 0
    while i != 1:
        if acao.lower() == 'conversar' or acao == '1':
                j=0
                if quest == 1:
                    print('Ao olhar ao redor, você encontra Matilda e Flora. Você se aproxima para conversar.')
                    time.sleep(3.5)
                    print('Matilda: Oh. Você veio, que bom. Diga-me,',jogador.cor+jogador.nome+narrador+'. Há alguma coisa que eu possa fazer por você como agradecimento?')
                    acao2 = int(input('1. Perguntar sobre tesouros\n2. Pedir apenas uma refeição quente\n[Digite o índice da ação.]: '))
                    while j !=1:
                        if acao2 == 1:
                            print('Matilda: Bom... Infelizmente não possuo joias ou relíquias. Porém há rumores que há um tesouro dentro da caverna perto do Lago das Águas Passadas.')
                            time.sleep(5.5)
                            print('Matilda: Outros aventureiros tentaram achá-lo, mas nenhum teve sucesso.')
                            time.sleep(4)
                            print('Matilda: Se decidir ir se aventurar lá, por favor, aguarde um momento. Tenho algo para você,',jogador.cor+jogador.nome)
                            time.sleep(4)
                            print(narrador+'Enquanto espera Matilda retornar, você brinca de adoleta com Flora.')
                            time.sleep(3)
                            print('Eventualmente ela retorna e te entrega uma lamparina, a qual você prende na sua cintura.')
                            time.sleep(3)
                            print('As duas se despedem de você para voltar a seus afazeres.')
                            quest = 0
                            quest2 = 1
                            j+=1
                        elif acao2 == 2:
                            print('Matilda: Ah, mas é claro. Você deve ter se exaurido quando lutava contra aquele duende.')
                            time.sleep(5)
                            print('Matilda: Estávamos terminando de fazer compras para o jantar, mesmo. Por favor,',jogador.cor+jogador.nome,'venha até minha casa.')
                            time.sleep(5)
                            print('Você segue as duas até sua casa. Matilda com um sorriso pede para ficar a vontade e aguardar enquanto prepara a janta.')
                            time.sleep(4)
                            print('Flora pede para brincar com você e vocês entram numa disputa incessante de jokenpô.')
                            time.sleep(4)
                            print('Assim que Matilda termina de cozinhar, os três começam a comer.')
                            time.sleep(3.5)
                            print('É estranho, mas parece que essa é a primeira vez que você ingere algum tipo de comida. E que bela primeira refeição.')
                            time.sleep(4)
                            print('Ao terminar, lá fora já está de noite. Matilda pergunta se não gostaria de passar a noite ali.\nVocê, com medo de se aventurar a noite, aceita de prontidão.')
                            time.sleep(5)
                            print('Entretanto, apenas uma noite se torna duas. E duas se tornam três. Você começa a sair com Matilda e Flora em seus passeios, e as protege de eventuais duendes.')
                            time.sleep(6)
                            print('Conforme os dias passam, sua vontade de aventurar cessa e você se vê chamando a casa de Matilda e Flora de lar.')
                            time.sleep(5)
                            print('Para retribuir toda a gentileza que te ofereceram, você consegue um emprego de guarda na vila, com suas habilidades de aventureiro(a).')
                            time.sleep(5)
                            print('Tudo parece um sonho. É tão perfeito quanto um sonho. É tão... estranho quanto um sonho...')
                            time.sleep(6.5)
                            print('Mas quem se importa? Você está feliz na sua nova vida. Se fosse um sonho, você não gostaria de acordar...')
                            time.sleep(5)
                            print('Final 3/6')
                            j+=1
                            raise SystemExit(0)
                        elif acao2 != 1 and acao2 != 2:
                            print('Matilda não tem o dia todo. Decida-se.')
                            acao2 = int(input('1. Perguntar sobre tesouros\n2. Pedir apenas uma refeição quente\n[Digite o índice da ação.]: '))
                else:
                    time.sleep(0.2)
                    print('Ao observar uma moça a caminhar pela vila, provavelmente voltando para casa, você se aproxima dela para conversar.')
                    time.sleep(5.5)
                    print('O que deseja fazer? ')
                    acao2 = int(input('1. Perguntar como as coisas vão nessa vila.\n2. Paquerar a jovem moça.\n[Digite o índice da ação.]: '))
                    while j !=1:
                        if acao2 == 1:
                            print('Você pergunta sobre a vila para a jovem moça, sem esperar muita coisa.')
                            time.sleep(5)
                            print('Jovem moça: Hm... As coisas vão bem, aparentemente. Nada a se preocupar mesmo.')
                            time.sleep(4)
                            print('Ao ouvir da jovem moça que a vila Curuçá está bem, você percebe que não há nada a se fazer ali e decide ir para outro lugar.')
                            time.sleep(5.5)
                            j+=1
                            viagem()
                            break
                        elif acao2 == 2:
                            print('Você tenta cortejar a moça se usando de suas "incríveis" habilidades de paquera.')
                            time.sleep(5)
                            print('As coisas não saem como o esperado e você acaba insultando a moça.')
                            time.sleep(4)
                            print('Ela arrasada te dá um tapa e sai de perto de você, para não ter que olhar para sua cara novamente.')
                            time.sleep(5)
                            print('Pouco tempo depois, guardas se aproximam de você.')
                            time.sleep(5)
                            print('Acontece que a jovem moça era filha do chefe do vilarejo, e ele não gostou que você a ofendeu.')
                            time.sleep(5)
                            print('Você é preso. Tentando explicar que foi apenas um mal entendido, você só piora a sua situação.')
                            time.sleep(5)
                            print('Tudo dá errado e você consegue a pena de morte. Até parece que foi tudo planejado... Como se forças externas estivessem decidindo o seu destino...')
                            time.sleep(6.5)
                            print('Final 5/6')
                            raise SystemExit(0)
                        elif acao2 != 1 and acao2 != 2:
                            print('O gato comeu a sua língua? Escolhe alguma opção que existe logo, abestado.')
                            acao2 = int(input('1. Perguntar como as coisas vão nessa vila.\n2. Paquerar a jovem moça.\n[Digite o índice da ação.]: '))
        elif acao.lower() == 'atacar' or acao == '2':
                print('Você começa a atacar as pessoas da vila, sem nenhum motivo. Elas entram em pânico.\nAo ouvirem a comoção, os guardas da vila logo chegam no local.')
                time.sleep(4)
                print('Ao avistarem as pessoas feridas, eles não perdem por esperar e te atacam. Você morre sem causar nenhuma vítima, felizmente.')
                time.sleep(4)
                print('Final 2/6')
                time.sleep(3)
                raise SystemExit(0)
        elif acao.lower() == 'viajar' or acao == '3':
                viagem()
                break
        else:
            print('Escolhe alguma coisa logo, por favor.')
        print('O que deseja fazer?')
        acao = input('1. Conversar\n2. Atacar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')

def lagodaságuaspassadas():
    global quest, quest2
    if randint(1,3) == 1:
          escolher_inimigo_comum()
          combate()
          time.sleep(0.35)
          print(narrador+'Você vence o seu inimigo... E olha ao redor.')
    time.sleep(0.35)
    print('Observando a linda paisagem do lago, você percebe uma caverna. O que deseja fazer, magnânimo aventureiro(a)?')
    acao = input('1. Lago\n2. Caverna\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    i = 0
    while i != 1:
        if acao.lower() == 'lago' or acao == '1':
            #fazer o jogador olhar para o lago e aos poucos ir sendo consumido por ele, até se afogar. Final 4/6
            return True
        elif acao.lower() == 'caverna' or acao == '2':
            caverna()
        elif acao.lower() == 'viajar' or acao == '3':
                viagem()
                break
        else:
            print('Escolhe alguma coisa logo, por favor.')
        print('O que deseja fazer?')
        acao = input('1. Lago\n2. Caverna\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')

#acontecimentos da caverna do Lago das Águas Passadas
def caverna():
    global quest2, combate_final
    if quest2 == 1:
        print('Você acende a lamparina que Matilda te deu e adentra a caverna.')
        time.sleep(3)
        print('Poucos passos além da entrada, você nota alguns morcegos agressivamente se aproximando de você.')
        time.sleep(3)
        print('No momento que você se prepara para sacar sua espada, os morcegos te contornam e não te atacam.\nParece que luz os repele.')
        time.sleep(7)
        print('Você continua a explorar a caverna.')
        time.sleep(3)
        print('Há um caminho estreito e extremamente escuro à frente. Por sorte, você consegue exergá-lo o suficiente para não tropeçar com a sua lamparina.')
        time.sleep(6)
        labirinto = [[jogador.nome[0],0,1,1,1],[1,0,1,1,1],[1,0,1,0,'x'],[1,0,0,0,1],[1,1,1,1,1]]
        percorre_labirinto(labirinto)
        print('Ao sair do labiritno, você encontra uma parede com uma escritas claramente não-humanas.')
        time.sleep(5)
        print('Mas você, por algum motivo definitivamente não importante, consegue lê-las fluentemente.')
        time.sleep(5)
        print('Você pronuncia as palavras escritas na parede e uma passagem se abre.')
        time.sleep(5)
        print('Antes de entrar na passagem, é possível sentir uma presença assustadora do outro lado.')
        time.sleep(4)
        print('O que deseja fazer?')
        acao2 = int(input('1. Olha ao redor\n2. Segue em frente mesmo assim\n[Digite o índice da ação.]: '))
        check=0
        while check != 1:
            if acao2 == 1:
                print('Antes de adentrar a passagem, você olha ao redor e percebe uma espada de prata. Você troca a sua espada de madeira por ela. Seu dano aumenta.')
                jogador.dano[0] += 15
                jogador.dano[1] += 15
                time.sleep(6)
                check += 1
            elif acao2 == 2:
                print('Você acha que está preparado(a) para o que der e vier e adentra a passagem.')
                check += 1
            elif acao2 != 1 and acao2 != 2:
                print('Decida-se, por favor.')
                acao2 = int(input('1. Olha ao redor\n2. Segue em frente mesmo assim\n[Digite o índice da ação.]: '))
        print('Uma criatura medonha e sem forma definida aparece diante de você.')
        inimigo.nome = lista_inimigos_especiais[1]
        inimigo.dano = inimigos_especiais_dano[1]
        inimigo.vidaT = inimigos_especiais_vidaT[1]
        combate_final = 1
        combate()
        combate_final = 0
        print(narrador+'Ao derrotar a criatura, um baú se materializa. Dentro dele você acha uma carta.')
        time.sleep(3)
        print('Nela está escrito:')
        time.sleep(2)
        print('"Parabéns,',jogador.cor+jogador.nome,narrador+'por chegar até aqui. Deve ter sido um saco."')
        time.sleep(5)
        print('"Pode ser decepcionante passar por tudo isso e encontrar apenas uma carta."')
        time.sleep(5)
        print('"Mas eu quero que se lembre. Não se trata do fim, e sim, da jornada."')
        time.sleep(5)
        print('"E a sua jornada ainda não terminou. Esse é apenas o começo, então vá. Continue a se aventurar."')
        time.sleep(5)
        print('"Compartilhe a sua jornada com os outros e assim, quem sabe, você encontre um tesouro que considere digno."')
        time.sleep(5)
        print('"Então..."')
        time.sleep(2)
        print('"O que deseja fazer, novo aventureiro(a)?"')
        time.sleep(3)
        print('Final 6/6')
        raise SystemExit(0)
    else:
        print('A caverna é bem escura, mas você consegue enxergar o suficiente para não tropeçar em nada.')
        time.sleep(5)
        print('Ao adentrar mais fundo na caverna você percebe seres voando em sua direção.')
        time.sleep(5)
        print('São morcegos gigantes e acho que eles não gostaram de você ter invadido o território deles.')
        inimigo.nome = lista_inimigos_especiais[0]
        inimigo.dano = inimigos_especiais_dano[0]
        inimigo.vidaT = inimigos_especiais_vidaT[0]
        combate()
        time.sleep(0.35)
        print(narrador+'Você derrota os morcegos e segue em frente.')
        time.sleep(4)
        print('Quanto mais fundo, menos você consegue enxergar.')
        time.sleep(4)
        print('Parece que você encontra uma passagem esguia, mas com a falta de luz você dá de cara de parede em parede e não sai do lugar.')
        time.sleep(6)
        print('Talvez se você tivesse uma lamparina, você conseguiria desbravar o caminho...')
        time.sleep(4)
        print('Você retraça seus paços e sai da caverna.')

#usada para imprimir a matriz usada como labirinto  
def mostra_matriz(matriz):
  for linha in matriz:
    print(*linha)

#sistema para o jogador andar pelo labirinto
def percorre_labirinto(matriz):
    mostra_matriz(matriz)
    P = jogador.nome[0]
    while matriz[2][4] != P:
        print('Você quer andar:')
        coluna = input('Para esquerda ou para direita (0 para nenhum): ')
        i = 0
        while i != 1:
            if coluna.lower() == 'esquerda':
                coluna = '-1'
                i=1
            elif coluna.lower() == 'direita':
                coluna = '1'
                i=1
            elif coluna == '0':
                i=1
            elif (coluna.lower() != 'esquerda' and coluna.lower() != 'direita' and coluna != '0'):
                print('Entrada inválida. Digite novamente para onde quer ir.')
                coluna = input('Para esquerda ou para direita (0 para nenhum): ')
        
        linha = input('Para cima ou para baixo (0 para nenhum): ')
        i = 0
        while i != 1:
            if linha.lower() == 'cima':
                linha = '-1'
                i=1
            elif linha.lower() == 'baixo':
                linha = '1'
                i=1
            elif linha == '0':
                i=1
            elif (linha.lower() != 'cima' and linha.lower() != 'baixo' and linha != '0'):
                print('Entrada inválida. Digite novamente para onde quer ir.')
                linha = input('Para cima ou para baixo (0 para nenhum): ')  

        for n_lin in range(len(matriz)):
            if P in matriz[n_lin]:
                Px = matriz[n_lin].index(P)
                Py = matriz.index(matriz[n_lin])
        if matriz[Py+int(linha)][Px+int(coluna)] != 1:
            matriz[Py][Px] = 0
            matriz[Py+int(linha)][Px+int(coluna)] = P
        else:
           print('Você se depara com uma parede.')
        mostra_matriz(matriz)


#função de causar dano, pode ser usada com dois objetos/personagens ou uma int e um objeto que recebe o dano
def causar_dano(agressor, vitima):
    if type(agressor) == int:
        dano_causado = agressor
    else:
        dano_causado = int(choices(agressor.dano, agressor.prob)[0])
        print(agressor.fala_agressao)

    vitima.vida -= dano_causado
    print(vitima.cor + f'{vitima.nome} - vida: {vitima.vida}', inimigo.cor + f'(-{dano_causado})')
    if vitima.vida<=0:
        if type(agressor) != int:
            print(agressor.cor + agressor.fala_finalizacao)
        elif type(agressor) == int and vitima != jogador:
             print(jogador.cor + jogador.fala_finalizacao)

#função simples de combate entre o jogador e um inimigo.
def combate():
    global inicio, quest2, primeiro_combate, combate_final
    inimigo.vida = inimigo.vidaT
    jogador.vida = jogador.vidaT
    print(f'Você se depara com um {inimigo.cor + inimigo.nome + narrador} selvagem')
    while jogador.vida>0 and inimigo.vida>0:
        print(narrador + 'O que você deseja fazer?')
        acao = input('1. Atacar\n2. Fugir\n3. Conversar\n[Digite o nome da ação ou seu índice]: ')
        if acao.lower() == 'atacar' or int(acao) == 1:
            causar_dano(jogador, inimigo)
            if inimigo.vida>0:
                print(inimigo.cor + 'O inimigo decidiu atacar!')
                causar_dano(inimigo, jogador)
            else:
                break
        elif acao.lower() == 'fugir' or int(acao) == 2:
            if inicio == 1 and primeiro_combate == 1:
                 print('Sua mente te diz para fugir, mas seu coração super valente te faz manter a sua decisão de proteger as duas pessoas indefesas.')
            elif quest2 == 1 and combate_final == 1:
                 print('A presença desse monstro te dá uma única certeza. Não tem como fugir. Você precisa lutar.')
            else:  
                print('Você vira suas costas ao seu adversário e sai correndo com o rabo entre as pernas.')
                time.sleep(1)
                break
        elif acao.lower() == 'conversar' or int(acao) == 3:
            print(narrador + 'Você não achou mesmo que conversar com um monstro iria adiantar alguma coisa né, kkkk?!')
            causar_dano(12, jogador)
            print(narrador + 'Recebeu dano só pra parar de ficar bobeando aí.')
        else:
            print('Escolha logo!!! Você tá no meio de uma batalha!!!')

#função que define qual será o inimigo que o jogador irá enfrentar em combate, excluindo os inimigos especiais.
def escolher_inimigo_comum():
    x = randint(0,1)
    inimigo_escolhido = lista_inimigos_comuns[x]
    i = randint(0, 2)
    inimigo.nome = inimigo_escolhido[0][i]
    inimigo.vidaT = inimigo_escolhido[1][i]
    inimigo.dano = inimigo_escolhido[2][i]

def main():
    intro()

main()
