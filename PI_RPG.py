'''#O RPG DO MAL'''

#importando as classes e objetos criados (variaveis dos personagens)
from rpgclasses import*

def intro():
    global lugar, inicio, quest, quest2, primeiro_combate, combate_final
    inicio = 1 #define que o usuário está no inicio do jogo
    quest = 0 #define que o usuário não está na primeira parte da missão principal
    quest2 = 0 #define que o usuário não está na segunda parte da missão principal
    primeiro_combate = 0 #variável definindo que você não está no que deveria ser o primeiro combate do jogo
    combate_final = 0 #variável definindo que você não está no combate final do jogo
    print(narrador + 'Você acorda no meio de uma floresta, apenas com um desejo insaciável de se aventurar.')
    jogador.nome = input('Qual o seu nome grande aventureiro? ') #pede o nome do jogador ao usuário
    print('Ahh, então você é',jogador.cor+jogador.nome,narrador+'...')
    time.sleep(2)
    print('Que nome bobo. Enfim, sua jornada começa agora...')
    time.sleep(2)
    print('Kkkk,',jogador.cor+jogador.nome,narrador+'. Aiai, esses jovens de hoje em dia, senhor.')
    time.sleep(2)
    lugar = 'florestadasalmasperdidas()' #define o local de partida do jogador
    eval(lugar.lower()) #chama a função do local de partida do jogador

#função para escolher para onde o player irá dentre os lugares na lista
def viagem():
    global lugar
    lugares = ['Floresta das Almas Perdidas', 'Vila Curuçá', 'Lago das Águas Passadas'] #lista de lugares existentes para o jogador visitar
    print(narrador+"Há uma placa com os seguintes lugares:")
    time.sleep(0.3)
    for i in range(len(lugares)): #primeiro loop que percorre a lista de lugares possíveis e os printa em ordem
        print("    "+f"{i+1}.",lugares[i])
        time.sleep(0.2)
    time.sleep(0.1)
    j=0 #variável usada para definir quando o segundo loop se encerrará
    print('Para onde desejas ir, nobre viajante?')
    destino = input('[Digite o nome completo do lugar ou seu índice - S para sair]: ')
    while j != len(lugares): #loop para enquanto o usuário não escolher um lugar que exista (tbm é usado para percorrer a lista de lugares)
        if destino.lower() in map(str.lower, lugares) or destino in (f"{i}" for i in range(1,len(lugares)+1)): #checa se a entrada do usuário existe dentro da lista de lugares, checando pelo nome dos lugares ou o índice deles na lista
            if destino.lower() == lugares[j].lower() or destino == str(j+1): #checa se a entrada do usuário é igual ao lugar da lista que o loop está percorrendo
                print(f'Você decide caminhar até {lugares[j]}.')
                lugar = lugares[j] #define uma variável que irá armazenar o nome do lugar que o usuário escolheu
                lugar = lugar.replace(' ', '')+'()' #muda a string do lugar para ficar igual o nome das funções dos lugares
                break #sai do loop sem finalizá-lo
            elif destino.lower() != lugares[j].lower() and destino != str(j+1): #checa se a entrada do usuário não é igual ao lugar da lista que o loop está percorrendo
                j+=1 #adiciona valor à variável que restringe o loop para que este passe para o próximo item da lista de lugares
        elif destino.lower() == 's': #checa se o usuário escolheu sair do input e não adicionar uma entrada igual a um lugar válido
            break #sai do loop sem finalizá-lo
        else: #condicional para quando o usuário tiver colocado uma entrada inválida no loop
            print('Decida ir pra algum lugar existente, por favor.')
            time.sleep(2)
            print('Para onde desejas ir, nobre viajante?')
            destino = input('[Digite o nome completo do lugar ou seu índice - S para sair]: ')
    eval(lugar.lower()) #puxa a função de mesmo nome da variável 'lugar', analisando a string como se fosse uma variável.
    time.sleep(1)

def florestadasalmasperdidas():
    global inicio, quest, quest2, primeiro_combate
    print('A floresta tem um ar misterioso. O que deseja fazer, incrível aventureiro? ')
    acao = input('1. Caminhar\n2. Cantar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    i = 0 #variável usada para definir quando o primeiro loop se encerrará
    while i != 1: #primeiro loop para enquanto o usuário não escolher entre as 3 diferentes ações
        if acao.lower() == 'caminhar' or acao == '1': #checagem para ver se o usuário escolheu a ação 1 no primeiro loop.
            if inicio == 1: #checagem para ver se o usuário está no inicio do jogo.
                print('Ao caminhar pelo local, você avista uma moça e uma criança colhendo ervas.')
                time.sleep(1)
                print('Se aproximando delas, seus olhos treinados avistam um duende claramente com inteção de atacá-las.')
                time.sleep(1.5)
                print('O que deseja fazer?')
                acao2 = input('1. Atacar o duende\n2. Deixar acontecer\n[Digite o índice da ação]: ')
                check = 0 #variável usada para definir quando o segundo loop se encerrará
                while check != 1: #loop para enquanto o usuário não escolher entre as opções 1 e 2
                    if acao2.lower() == '1': #checagem para escolha número 1 no segundo loop - roda os códigos relacionados a ela
                        print('Você segura a sua espada de madeira que carregava na cintura esse tempo todo e se joga na frente do duende.')
                        time.sleep(3.5)
                        inimigo.nome = duendes[0] #define o nome do inimigo do combate
                        primeiro_combate = 1 #variável definindo que você está no que deveria ser o primeiro combate do jogo
                        combate()
                        primeiro_combate = 0 #variável definindo que você encerrou o que deveria ser o primeiro combate do jogo
                        time.sleep(0.35)
                        print(narrador+'Você vence seu adversário e consegue garantir a segurança da moça e da criança.')
                        time.sleep(2.5)
                        check += 1 #diz ao segundo loop para se encerrar
                    elif acao2.lower() == '2': #checagem para escolha número 2 no segundo loop - roda os códigos relacionados a ela
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
                        raise SystemExit(0) #finaliza o programa. fim de jogo
                    print('Moça: Obrigada, jovem aventureiro(a), por sua ajuda. Graças a você, minha filha e eu estamos sã e salvas.')
                    time.sleep(4)
                    print('Matilda: Chamo-me Matilda, e essa é a minha filha Flora.')
                    time.sleep(3)
                    print('Matilda: Por favor, se lhe for de seu agrado, visite-nos em nossa vila para que assim eu possa te agradecer propriamente.')
                    time.sleep(6)
                    print('Assim Matilda e Flora recolhem seus pertences e caminham para casa.')
                    time.sleep(3)
                    inicio = 0 #encerra o inicio do jogo.
                    quest = 1 #'inicializa' a primeira parte da missão principal
            else: #condicional para quando o usuário não estiver no início do jogo.
                if randint(1,3) == 1: #condicional para simular probabilidade de 1/3
                    escolher_inimigo_comum() #escolhe o inimigo para o combate
                    combate() #inicia o combate
                    time.sleep(0.35)
                    print(narrador+'Você prossegue na sua jornada.')
                time.sleep(2)
                print('Você caminha e caminha, mas nada encontra. Até parece que alguém esqueceu de colocar algo aqui.')
                time.sleep(4)
        elif acao.lower() == 'cantar' or acao == '2': #checagem para ver se o usuário escolheu a ação 2 no primeiro loop.
            print('O seu magnificamente horrendo canto atrai uma alcateia de lobos que acham que você é um petisco.\nVocê corre e corre até despistá-los.')
            time.sleep(3)
        elif acao.lower() == 'viajar' or acao == '3': #checagem para ver se o usuário escolheu a ação 3 no primeiro loop.
            viagem() #puxa a função viagem
            break #sai do loop sem finalizá-lo
        else: #condicional para quando o usuário tiver colocado uma entrada inválida no primeiro loop
            print('Escolhe alguma coisa logo, porra.')
        print('O que deseja fazer?')
        acao = input('1. Caminhar\n2. Cantar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    
def vilacuruçá():
    global quest, quest2
    print('Você vê as pessoas andando pela vila pacificamente. O que deseja fazer, incrível aventureiro? ')
    acao = input('1. Conversar\n2. Atacar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    i = 0 #variável usada para definir quando o primeiro loop se encerrará
    while i != 1: #lprimeiro loop para enquanto o usuário não escolher entre as 3 diferentes ações
        if acao.lower() == 'conversar' or acao == '1': #checagem para ver se o usuário escolheu a ação 1.
            j=0 #variável usada para definir quando o primeiro loop se encerrará
            if quest == 1: #checa se o usuário está na primeira parte da missão principal
                print('Ao olhar ao redor, você encontra Matilda e Flora. Você se aproxima para conversar.')
                time.sleep(3.5)
                print('Matilda: Oh. Você veio, que bom. Diga-me,',jogador.cor+jogador.nome+narrador+'. Há alguma coisa que eu possa fazer por você como agradecimento?')
                print('O que deseja fazer?')
                acao2 = int(input('1. Perguntar sobre tesouros\n2. Pedir apenas uma refeição quente\n[Digite o índice da ação.]: '))
                while j !=1: #segundo loop para enquanto o usuário não escolher as opções 1 ou 2.
                    if acao2 == 1: #checagem para escolha número 1 no segundo loop - roda os códigos relacionados a ela
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
                        quest = 0 #'finaliza' a primeira parte da missão principal
                        quest2 = 1 #'inicializa' a segunda parte da missão principal
                        j+=1 #diz ao segundo loop para se encerrar
                    elif acao2 == 2: #checagem para escolha número 2 no segundo loop - roda os códigos relacionados a ela
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
                        j+=1 #diz ao segundo loop para se encerrar
                        raise SystemExit(0) #finaliza o programa. fim de jogo.
                    elif acao2 != 1 and acao2 != 2: #checagem para ver se o usuário colocou alguma entrada inválida diferente da escolha 1 ou 2
                        print('Matilda não tem o dia todo. Decida-se.')
                        acao2 = int(input('1. Perguntar sobre tesouros\n2. Pedir apenas uma refeição quente\n[Digite o índice da ação.]: '))
            else: #condicional para quando o usuário não estiver na primeira parte da missão principal.
                time.sleep(0.2)
                print('Ao observar uma moça a caminhar pela vila, provavelmente voltando para casa, você se aproxima dela para conversar.')
                time.sleep(5.5)
                print('O que deseja fazer?')
                acao2 = int(input('1. Perguntar como as coisas vão nessa vila.\n2. Paquerar a jovem moça.\n[Digite o índice da ação.]: '))
                while j !=1: #segundo loop para enquanto o usuário não escolher a opção 1 ou 2.
                    if acao2 == 1: #checagem para escolha número 2 no segundo loop - roda os códigos relacionados a ela
                        print('Você pergunta sobre a vila para a jovem moça, sem esperar muita coisa.')
                        time.sleep(5)
                        print('Jovem moça: Hm... As coisas vão bem, aparentemente. Nada a se preocupar mesmo.')
                        time.sleep(4)
                        print('Ao ouvir da jovem moça que a vila Curuçá está bem, você percebe que não há nada a se fazer ali e decide ir para outro lugar.')
                        time.sleep(5.5)
                        j+=1 #diz ao segundo loop para se encerrar
                        i+=1 #diz ao primeiro loop para se encerrar
                        viagem() #puxa a função viagem
                        break #sai do loop sem finalizá-lo
                    elif acao2 == 2: #checagem para escolha número 2 no segundo loop - roda os códigos relacionados a ela
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
                        raise SystemExit(0) #finaliza o programa. fim de jogo
                    elif acao2 != 1 and acao2 != 2: #checagem para ver se o usuário colocou alguma entrada inválida diferente da escolha 1 ou 2
                        print('O gato comeu a sua língua? Escolhe alguma opção que existe logo, abestado.')
                        acao2 = int(input('1. Perguntar como as coisas vão nessa vila.\n2. Paquerar a jovem moça.\n[Digite o índice da ação.]: '))
        elif acao.lower() == 'atacar' or acao == '2': #checagem para ver se o usuário escolheu a ação 2 no primeiro loop.
            print('Você começa a atacar as pessoas da vila, sem nenhum motivo. Elas entram em pânico.\nAo ouvirem a comoção, os guardas da vila logo chegam no local.')
            time.sleep(4)
            print('Ao avistarem as pessoas feridas, eles não perdem por esperar e te atacam. Você morre sem causar nenhuma vítima, felizmente.')
            time.sleep(4)
            print('Final 2/6')
            time.sleep(3)
            raise SystemExit(0) #finaliza o programa. fim de jogo
        elif acao.lower() == 'viajar' or acao == '3': #checagem para ver se o usuário escolheu a ação 3 no primeiro loop.
            viagem() #puxa a função viagem
            break #sai do loop sem finalizá-lo
        else: #condicional para quando o usuário tiver colocado uma entrada inválida no primeiro loop
            print('Escolhe alguma coisa logo, por favor.')
        print('O que deseja fazer?')
        acao = input('1. Conversar\n2. Atacar\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')

def lagodaságuaspassadas():
    global quest, quest2
    if randint(1,3) == 1: #condicional que simula probabilidade de 1/3
        escolher_inimigo_comum() #escolhe o inimigo para o combate
        combate() #inicia o comabte
        time.sleep(0.35)
        print(narrador+'Você olha ao redor.')
    time.sleep(1)
    print('Observando a linda paisagem do lago, você percebe uma caverna. O que deseja fazer, magnânimo aventureiro(a)?')
    acao = input('1. Lago\n2. Caverna\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')
    i = 0 #variável usada para definir quando o loop se encerrará
    while i != 1: #loop para enquanto o usuário não escolher entre 3 diferentes ações
        if acao.lower() == 'lago' or acao == '1': #checagem para ver se o usuário escolheu a ação 1.
            print('Você vai até a margem do grande lago para apreciá-lo. A água cristalina te chama a atenção.')
            time.sleep(4)
            print('Você fica fitando seu reflexo na água como que hipnotizado.')
            time.sleep(4)
            print('Até que há um eco de uma voz.')
            time.sleep(4)
            print('???:',jogador.cor+jogador.nome+narrador+', estive esperando por você!')
            time.sleep(4)
            print('A voz é misteriosa, mas estranhamente familiar...')
            time.sleep(4)
            print('De repente, você tem essa vontade enorme de encontrar quem ou o que porta a tal voz.')
            time.sleep(5)
            print('???: Venha,',jogador.cor+jogador.nome+narrador+'. Venha me ver novamente!')
            time.sleep(4.5)
            print('Uma voz delicada que te relaxa. Uma voz que te dá certo calor... Ahhh, como você busca estar junto dessa voz.')
            time.sleep(7.5)
            print('???: Vamos logo,',jogador.cor+jogador.nome+narrador+'. O dia já está escurecendo...')
            time.sleep(4.5)
            print('Quanto mais você se aproxima da voz, mais seu corpo fica submerso na água.')
            time.sleep(5)
            print('Você nem percebe quando começa a suavemente afundar no lago.')
            time.sleep(4.5)
            print('???: Qual o problema,',jogador.cor+jogador.nome+narrador+'? Não precisa ter medo!')
            time.sleep(5)
            print('Não há mais ar em seu pulmão, mas de alguma forma você se sente em casa. Tão... relaxado.')
            time.sleep(6)
            print('???: Ahhhh,',jogador.cor+jogador.nome+narrador+'! Como é bom finalmente estar ao seu lado!')
            time.sleep(6)
            print('???: Vamos,',jogador.cor+jogador.nome+narrador+'. Já está tarde... É hora de dormir.')
            time.sleep(7)
            print('???:',jogador.cor+jogador.nome+narrador+', tenha bons sonhos...')
            time.sleep(4)
            print('Final 4/6')
            time.sleep(3)
            raise SystemExit(0) #finaliza o programa. fim de jogo.
        elif acao.lower() == 'caverna' or acao == '2': #checagem para ver se o usuário escolheu a ação 2.
            i+=1 #diz ao loop para se encerrar
            caverna() #puxa a função caverna
        elif acao.lower() == 'viajar' or acao == '3':
            viagem() #puxa a função viagem
            break #sai do loop sem finalizá-lo
        else: #condicional para quando o usuário tiver colocado uma entrada inválida no loop
            print('Escolhe alguma coisa logo, por favor.')
        print('O que deseja fazer?')
        acao = input('1. Lago\n2. Caverna\n3. Viajar\n[Digite o nome da ação ou seu índice]: ')

#acontecimentos da caverna do Lago das Águas Passadas
def caverna():
    global quest2, combate_final
    if quest2 == 1: #checagem para ver se o usuário está na segunda parte da missão principal
        print('Você acende a lamparina que Matilda te deu e adentra a caverna.')
        time.sleep(3)
        print('Poucos passos além da entrada, você nota alguns morcegos agressivamente se aproximando de você.')
        time.sleep(3)
        print('No momento que você se prepara para sacar sua espada, os morcegos te contornam e não te atacam.\nParece que luz os repele.')
        time.sleep(7)
        print('Você continua a explorar a caverna.')
        time.sleep(3)
        print('Há um corredor estreito e extremamente escuro à frente. Por sorte, você consegue exergá-lo o suficiente para não tropeçar com a sua lamparina.')
        time.sleep(6)
        labirinto = [[jogador.nome[0],0,1,1,1],[1,0,1,1,1],[1,0,1,0,'x'],[1,0,0,0,1],[1,1,1,1,1]] #define o caminho a ser percorrido pelo jogador
        percorre_labirinto(labirinto) #puxa a função para percorrer o caminho se utilizando do caminho anteriormente definido
        print('Saindo do corredor, você encontra uma parede com uma escritas claramente não-humanas.')
        time.sleep(5)
        print('Mas você, por algum motivo definitivamente não importante, consegue lê-las fluentemente.')
        time.sleep(5)
        print('Você pronuncia as palavras escritas na parede e uma passagem se abre.')
        time.sleep(5)
        print('É possível sentir uma presença assustadora do outro lado da passagem misteriosa.')
        time.sleep(4)
        print('O que deseja fazer?')
        acao2 = int(input('1. Olhar ao redor\n2. Seguir em frente mesmo assim\n[Digite o índice da ação.]: '))
        check=0 #variável usada para definir quando o loop se encerrará
        while check != 1: #loop para enquanto o usuário não escolher entre as opções 1 e 2.
            if acao2 == 1: #checagem para escolha número 1 - roda os códigos relacionados a ela
                print('Antes de adentrar a passagem, você olha ao redor e percebe uma espada de prata. Você troca a sua espada de madeira por ela. Seu dano aumenta.')
                jogador.dano[0] += 15 #aumenta o dano normal do jogador
                jogador.dano[1] += 15 #aumenta o dano crítica do jogador
                time.sleep(6)
                check += 1 #diz para o loop se encerrar
            elif acao2 == 2: #checagem para escolha número 2 - roda os códigos relacionados a ela
                print('Você acha que está preparado(a) para o que der e vier e adentra a passagem.')
                check += 1 #diz para o loop se encerrar
            elif acao2 != 1 and acao2 != 2: #checagem para ver se o usuário colocou alguma entrada inválida diferente da escolha 1 ou 2
                print('Decida-se, por favor.')
                acao2 = int(input('1. Olhar ao redor\n2. Seguir em frente mesmo assim\n[Digite o índice da ação.]: '))
        print('Uma criatura medonha e sem forma definida aparece diante de você.')
        inimigo.nome = lista_inimigos_especiais[1] #define o nome do inimigo especial
        inimigo.dano = inimigos_especiais_dano[1] #define o dano do inimigo especial
        inimigo.vidaT = inimigos_especiais_vidaT[1] #define a vida total do inimigo especial
        combate_final = 1 #variável definindo que você está no combate final do jogo
        combate()
        combate_final = 0 #variável definindo que você encerrou o combate final do jogo
        print(narrador+'Ao derrotar a criatura, um baú se materializa. Dentro dele você acha uma carta.')
        time.sleep(3)
        print('Nela está escrito:')
        time.sleep(2)
        print('"Parabéns,',jogador.cor+jogador.nome+narrador+', por chegar até aqui. Deve ter sido um saco."')
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
        print('"O que deseja fazer, verdadeiro(a) aventureiro(a)?"')
        time.sleep(3)
        print('Final 6/6')
        raise SystemExit(0) #finaliza o programa. fim de jogo
    else: #condicional para quando o jogador não estiver na segunda parte da missão principal
        print('A caverna é bem escura, mas você consegue enxergar o suficiente para não tropeçar em nada.')
        time.sleep(5)
        print('Ao adentrar mais fundo na caverna você percebe seres voando em sua direção.')
        time.sleep(5)
        print('São morcegos gigantes e acho que eles não gostaram de você ter invadido o território deles.')
        inimigo.nome = lista_inimigos_especiais[0] #define o nome do inimigo especial
        inimigo.dano = inimigos_especiais_dano[0] #define o dano do inimigo especial
        inimigo.vidaT = inimigos_especiais_vidaT[0] #define a vida total do inimigo especial
        combate() #inicializa o combate
        time.sleep(0.35)
        print(narrador+'Você segue em frente.')
        time.sleep(4)
        print('Quanto mais fundo, menos você consegue enxergar.')
        time.sleep(4)
        print('Parece que você encontra um caminho apertado, mas com a falta de luz você tropeça, tromba com as paredes e não sai do lugar.')
        time.sleep(6)
        print('Talvez se com a ajuda duma lamparina, você conseguiria desbravar o que há pela frente...')
        time.sleep(4)
        print('Você retraça seus paços e sai da caverna.')

#usada para imprimir a matriz usada como labirinto  
def mostra_matriz(matriz):
    for linha in matriz:
        print(*linha)

#sistema para o jogador andar pelo labirinto
def percorre_labirinto(matriz):
    mostra_matriz(matriz) #mostra o labirinto no estado inicial pro usuário
    P = jogador.nome[0] #variável que atribui a P a primeira letra do nome do jogador, q sinalizará a sua posição
    while matriz[2][4] != P: #primeiro loop para enquanto o jogador não chegar na saída já definida
        print('Você quer andar:')
        coluna = input('Para esquerda ou para direita (0 para nenhum): ')
        i = 0 #variável usada para definir quando o segundo loop se encerrará
        while i != 1: #segundo loop para enquanto o usuário não escolher entre as opções dadas
            if coluna.lower() == 'esquerda':
                coluna = '-1' #define um número que representará a movimentação para a esquerda pelas colunas da matriz
                i=1 #diz ao segundo loop para se encerrar
            elif coluna.lower() == 'direita':
                coluna = '1' #define um número que representará a movimentação para a direita pelas colunas da matriz
                i=1 #diz ao segundo loop para se encerrar
            elif coluna == '0':
                i=1 #diz ao segundo loop para se encerrar
            elif (coluna.lower() != 'esquerda' and coluna.lower() != 'direita' and coluna != '0'): #checagem para ver se o usuário colocou alguma entrada inválida para a movimentação pelas colunas da matriz
                print('Entrada inválida. Digite novamente para onde quer ir.')
                coluna = input('Para esquerda ou para direita (0 para nenhum): ')
        
        linha = input('Para cima ou para baixo (0 para nenhum): ')
        i = 0 #variável usada para definir quando o terceiro loop se encerrará
        while i != 1: #terceiro loop para enquanto o usuário não escolher entre as opções dadas
            if linha.lower() == 'cima':
                linha = '-1' #define um número que representará a movimentação para cima pelas linhas da matriz
                i=1 #diz ao terceiro loop para se encerrar
            elif linha.lower() == 'baixo': 
                linha = '1' #define um número que representará a movimentação para baixo pelas linhas da matriz
                i=1 #diz ao terceiro loop para se encerrar
            elif linha == '0':
                i=1 #diz ao terceiro loop para se encerrar
            elif (linha.lower() != 'cima' and linha.lower() != 'baixo' and linha != '0'): #checagem para ver se o usuário colocou alguma entrada inválida para a movimentação pelas linhas da matriz
                print('Entrada inválida. Digite novamente para onde quer ir.')
                linha = input('Para cima ou para baixo (0 para nenhum): ')  

        for n_lin in range(len(matriz)): #loop que roda pelas linhas da matriz para mudar a posição do jogador no labirinto
            if P in matriz[n_lin]: #checa se o jogador está na linha em que o loop está passando
                Px = matriz[n_lin].index(P) #define Px como a posição do jogador na linha em que está da matriz
                Py = matriz.index(matriz[n_lin]) #define Py como a posição do jogador na coluna em que está da matriz
        if matriz[Py+int(linha)][Px+int(coluna)] != 1: #checa se a movimentação do jogador pelo labirinto não é impedida por uma parede (1)
            matriz[Py][Px] = 0 #apaga as posições antigas do jogador e as troca por um caminho livre (0)
            matriz[Py+int(linha)][Px+int(coluna)] = P #adiciona as entradas do usuário à posição do jogador, fazendo-o se movimentar pelo labirinto
        else: #condicional para quando o movimento do jogador pelo labirinto é impedido por uma parede
            print('Você se depara com uma parede.')
        mostra_matriz(matriz) #mostra o labirinto com a posição do jogador atualizada


#função de causar dano, pode ser usada com dois objetos/personagens ou uma int (agressor) e um objeto que recebe o dano (vítima)
def causar_dano(agressor, vitima):
    if type(agressor) == int: #checa se o agressor é um número inteiro
        dano_causado = agressor #define o dano q o agressor causará como o próprio agressor, já q é um número inteiro
    else:
        dano_causado = int(choices(agressor.dano, agressor.prob)[0]) #define o dano q o agressor causará com um sorteio entre o dano normal e crítico de quem for o agressor
        print(agressor.fala_agressao) #printa a fala de ataque do agressor

    vitima.vida -= dano_causado #reduz a vida da vítima com o dano q o agressor causará
    print(vitima.cor + f'{vitima.nome} - vida: {vitima.vida}', inimigo.cor + f'(-{dano_causado})') #printa quem é a vítima, a sua vida atual, e o dano causado pelo agressor
    if vitima.vida<=0: #checa se a vida da vítima é menor ou igual a zero, ou seja, se está morta
        if type(agressor) != int: #checa se o agressor não é um número inteiro
            print(agressor.cor + agressor.fala_finalizacao) #printa a fala de vitória do agressor
        elif type(agressor) == int and vitima != jogador: #checa se o agressor é um número inteiro e se a vítima não é o jogador
            print(jogador.cor + jogador.fala_finalizacao) #printa a fala de vitória do jogador

#função simples de combate entre o jogador e um inimigo.
def combate():
    global inicio, quest2, primeiro_combate, combate_final
    inimigo.vida = inimigo.vidaT #define a vida "líquida" do inimigo sendo igual a vida total dele. Está resetando a vida do inimigo para que haja diferentes combates no jogo
    jogador.vida = jogador.vidaT #define a vida "líquida" do jogador sendo igual a vida total dele. Está resetando a vida do jogador para que não seja necessário curá-lo entre diferentes combates
    print(f'Você se depara com um {inimigo.cor + inimigo.nome + narrador} selvagem') #printa mensagem com nome do inimigo que o jogador enfrentará
    while jogador.vida>0 and inimigo.vida>0: #loop para enquanto o jogador e o inimigo ainda tiverem vida maior que 0, ou seja, para enquanto estiverem vivos
        print(narrador + 'O que você deseja fazer?')
        acao = input('1. Atacar\n2. Fugir\n3. Conversar\n[Digite o nome da ação ou seu índice]: ')
        if acao.lower() == 'atacar' or int(acao) == 1: #checagem para escolha número 1
            causar_dano(jogador, inimigo) #puxa a função causar dano, com o jogador como agressor e o inimigo como a vítima
            if inimigo.vida>0: #checa se o inimigo tem vida maior que 0, ou seja, se está vivo
                print(inimigo.cor + 'O inimigo decidiu atacar!')
                causar_dano(inimigo, jogador) #puxa a função causar dano, com o inimigo como agressor e o jogador como a vítima
            else:
                break #sai do loop sem finalizá-lo
        elif acao.lower() == 'fugir' or int(acao) == 2: #checagem para escolha número 2
            if inicio == 1 and primeiro_combate == 1: #checa se o jogador está no início do jogo e se está no que deveria ser o primeiro combate do jogo
                print('Sua mente te diz para fugir, mas seu coração super valente te faz manter a sua decisão de proteger as duas pessoas indefesas.')
            elif quest2 == 1 and combate_final == 1: #checa se o jogador está na segunda parte da missão principal e se está no combate final do jogo
                print('A presença desse monstro te dá uma única certeza. Não tem como fugir. Você precisa lutar.')
            else: #condicional para caso nenhum das outras condições sejam satisfeitas 
                print('Você vira suas costas ao seu adversário e sai correndo com o rabo entre as pernas.')
                time.sleep(1)
                break #sai do loop sem finalizá-lo
        elif acao.lower() == 'conversar' or int(acao) == 3: #checagem para escolha número 3
            print(narrador + 'Você não achou mesmo que conversar com um monstro iria adiantar alguma coisa né, kkkk?!')
            causar_dano(12, jogador) #puxa a função causar dano, com um número inteiro como agressor e o jogador como a vítima
            print(narrador + 'Recebeu dano só pra parar de ficar bobeando aí.')
        else: #condicional para quando o usuário tiver colocado uma entrada inválida no loop
            print('Escolha logo!!! Você tá no meio de uma batalha!!!')

#função que define qual será o inimigo que o jogador irá enfrentar em combate, excluindo os inimigos especiais.
def escolher_inimigo_comum():
    x = randint(0, 1) #sorteia número inteiro entre 0 e 1 (índices possíveis da lista de inimigos comuns)
    inimigo_escolhido = lista_inimigos_comuns[x] #define inimigo_escolhido como o item (lista do inimigo específico) da lista de inimigos comuns que tem índice igual a x
    if len(inimigo_escolhido[0]) < 3: #checa se a lista do inimigo específico tem tamanho menor que 3, ou seja, o inimigo específico tem menos de 3 variações
        i = randint(0, 1) #sorteia número inteiro entre 0 e 1 (índices possíveis da lista do inimigo específico de tamanho menor que 3)
    else:
        i = randint(0, 2) #sorteia número inteiro entre 0 e 1 (índices possíveis da lista do inimigo específico de tamanho maior ou igual que 3)
    inimigo.nome = inimigo_escolhido[0][i] #define o nome do inimigo específico
    inimigo.vidaT = inimigo_escolhido[1][i] #define a vida total do inimigo específico
    inimigo.dano = inimigo_escolhido[2][i] #define o dano do inimigo específico

def main():
    intro() #puxa a função intro para inicializar o jogo

main()
