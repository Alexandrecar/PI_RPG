'''#O RPG DO MAL'''

#importando as classes e objetos criados (variaveis dos personagens)
from rpgclasses import*

def intro():
    print(narrador + 'Você acorda no meio do nada, apenas com um desejo insaciável de se aventurar.')
    jogador.nome = input('Qual o seu nome grande aventureiro? ')
    print(f'''Ahh, então você é {jogador.nome}...
Que nome bobo. Enfim, sua jornada começa agora...
Kkkk, {jogador.nome}. Aiai, esses jovens de hoje em dia, senhor.''')

#função para escolher para onde o player irá dentre os lugares na lista
def viagem():
    global lugar
    lugar='0'
    lugares = ['Floresta das Almas Perdidas', 'Vila Curuçá', 'Lago das Águas Passadas', 'Caverna dos Românticos Inconsequentes']
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
    eval(lugar.lower())

def florestadasalmasperdidas():
    print('A floresta tem um ar misterioso. O que quer fazer, incrível aventureiro? ')
    acao = input('Caminhar, cantar, ou voltar? ')
    i = 0
    while i != 1:
        if acao.lower() == 'caminhar':
                if randint(1,3) == 1:
                    combate()
                    time.sleep(0.35)
                    print(narrador+'Você vence seu adversário e prossegue na sua jornada.')
                time.sleep(0.2)
                print('Você caminha e caminha, mas nada encontra. Parece que os devs esqueceram de colocar alguma coisa aqui.')
                i+=1
        elif acao.lower() == 'voltar':
                i+=1
                viagem()
        elif acao.lower() == 'cantar':
                print('O seu magnificamente horrendo canto atrai uma alcateia de lobos que te atacam.\nVocê não tem chance de se defender.\nGame over, filhão.')
                time.sleep(1)
                i+=1
                main()
        else:
            print('Escolhe alguma coisa logo, porra.')
            acao = input('Caminhar, voltar, ou cantar? ')
    
def vilacuruçá():
    print('Você vê as pessoas andando pela vila pacificamente. O que quer fazer, incrível aventureiro? ')
    acao = input('Conversar, atacar, ou voltar? ')
    i = 0
    while i != 1:
        if acao.lower() == 'conversar':
                j=0
                time.sleep(0.2)
                print('Ao observar uma moça a caminhar pela vila, provavelmente voltando para casa, você se aproxima dela para conversar.')
                time.sleep(0.3)
                print('O que você faz? ')
                acao2 = int(input('1. Pergunta como as coisas vão nessa vila.\n2. Paquera a jovem moça.\n[Escolha apenas o índice.]: '))
                while j !=1:
                    if acao2 == 1:
                        print('Jovem moça: Hm... As coisas vão bem, aparentemente. Nada a se preocupar mesmo.')
                        time.sleep(0.25)
                        print('Ao ouvir da jovem moça que a vila Curuçá está bem, você percebe que não há nada a se fazer ali e decide ir para outro lugar.')
                        time.sleep(0.5)
                        i+=1
                        j+=1
                        viagem()
                    if acao2 == 2:
                        print('Jovem moça: Eu sou casada, seu pervertido.')
                        time.sleep(0.2)
                        print('Após seu cortejo dar errado, alguns guardas se aproximam de você.')
                        time.sleep(0.2)
                        print('Guarda: Não toleramos assédio nessas redondezas, escória. Você está preso.')
                        time.sleep(0.2)
                        print('Game over. Você deveria ter vergonha de você. Agora você apodrecerá na prisão.')
                        time.sleep(1)
                        i+=1
                        j+=1
                        main()
                while acao2 != 1 and acao2 != 2:
                    print('O gato comeu a sua língua? Escolhe alguma opção que existe logo, abestado.')
                    acao2 = int(input('1. Pergunta como as coisas vão nessa vila.\n2. Paquera a jovem moça. '))
        elif acao.lower() == 'voltar':
                i+=1
                viagem()
        elif acao.lower() == 'atacar':
                print('Você começa a atacar as pessoas da vila, sem nenhum motivo. Elas entram em pânico.\nAo ouvirem a comoção, os guardas da vila logo chegam no local.')
                time.sleep(0.2)
                print('Ao avistarem o seu massacre, eles não perdem por esperar e te atacam. Você morre sem causar nenhuma vítima, felizmente.')
                time.sleep(0.2)
                print('Game over. Seu otário.')
                time.sleep(1)
                i+=1
                main()
        else:
            print('Escolhe alguma coisa logo, porra.')
            acao = input('Conversar, atacar, ou voltar? ')

def lagodaságuaspassadas():
     if randint(1,3) == 1:
          combate()
          time.sleep(0.35)
          print('Você vence o seu inimigo... E olha ao redor.')
     print('Observando a paisagem você percebe uma coisa esplêndida... Não tem nada aqui ainda...')

def cavernadosromânticosinconsequentes():
    print('Você adentra a caverna ao ouvir alguns sons estranhos.')
    time.sleep(3)
    print('Uma figura misteriosa se aproxima agressivamente. Você não consegue ver direito, pois está muito escuro.')
    time.sleep(4)
    print('A figura tenta te atacar, mas você é mais rápido.')
    time.sleep(3)
    causar_dano(25,inimigo)
    time.sleep(3.5)
    print(narrador+'Ao ver seu inimigo no chão, você percebe que é um homem... pelado')
    time.sleep(4)
    print('Você continua a caminhar pela caverna, indo na direção que os sons ficam mais altos.')
    time.sleep(5)
    print('Quanto mais perto você chega, mais os sons se parecem com vozes humanas... e outras coisas.')
    time.sleep(5.5)
    print(f'Finalmente você consegue chegar na origem dos sons. E eu tenho certeza que você do outro lado da tela já tem ideia do que {jogador.nome} presencia.')
    time.sleep(7)
    print('Você pensa no que fazer após assistir tal cena. E decide -redacted-.')
    time.sleep(4.5)
    print('Game over. No dia seguinte, você estava com dores em todo o corpo. Mas com certeza se lembra de ter se divertido muito.')
    time.sleep(6)
    print('Na verdade você se divertiu tanto que decidiu ficar por lá... Adeus, carreira de aventureiro.')


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

def combate():
    print(f'Você se depara com um {inimigo.cor + inimigo.nome + narrador} selvagem')
    while jogador.vida>0 and inimigo.vida>0:
        print(narrador + 'O que você quer fazer?')
        acao = input('Atacar, fugir, ou conversar? ')
        if acao.lower() == 'atacar':
            causar_dano(jogador, inimigo)
            if inimigo.vida>0:
                print(inimigo.cor + 'O inimigo decidiu atacar!')
                causar_dano(inimigo, jogador)
            else:
                break
        elif acao.lower() == 'fugir':
            print('Ao tentar fugir, você tropeça.', inimigo.cor + 'O inimigo aproveita sua incompetência e ataca!')
            causar_dano(inimigo, jogador)
        elif acao.lower() == 'conversar':
            print(narrador + 'TÁ ACHANDO QUE AQUI É NARUTO PRA VOCÊ CONVERSAR COM OS SEUS INIMIGOS?!!!')
            causar_dano(12, jogador)
            print(narrador + 'KKKK Recebeu dano só pra deixar de ser otário.')
        else:
            print('TÁ BOBEANDO PORRA? ESCOLHE ALGUMA COISA KRL!!')

def main():
    intro()
    viagem()

main()
