#O RPG DO MAL, por enquanto só sistema de combate

from rpgclasses import*

def intro():
    print(narrador + 'Você acorda no meio do nada, apenas com um desejo insaciável de se aventurar.')
    jogador.nome = input('Qual o seu nome grande aventureiro? ')
    print(f'''Ahh, então você é {jogador.nome}...
Que nome bobo. Enfim, sua jornada começa agora...
Kkkk, {jogador.nome}. Aiai, esses jovens de hoje em dia, senhor.''')

def causar_dano(agressor, vitima):
    if type(agressor) == int:
        dano_causado = agressor
    else:
        dano_causado = int(choices(agressor.dano, agressor.prob)[0])
    vitima.vida = vitima.vida - dano_causado
    if vitima.vida>0:
        print(vitima.cor + f'Oh não, perdi {dano_causado} de vida. Tenho apenas {vitima.vida} de vida agora.')
    else:
        print(vitima.cor + f"""OH!!! Recebi {dano_causado} de dano e minha vida chegou ao fim. Um golpe extremamente fatal. Estou vendo minha vida passar diante de meus olhos.
OH! Se ao menos o Chapolim Colorado tivesse vindo ao meu resgate!!! AHH, que vida mais injusta! Maldito seja você, ó mundo cruel!!!! Fim de minha jornada magnífica""")
'''def dano_no_enemy(dano):
    inimigo.vida = inimigo.vida-dano
    if inimigo.vida>0:
        print(jogador.cor + f'Dei {dano} de dano. O cara está com {inimigo.vida} de vida. ATACAR!!!!!!')
    else:
        print(jogador.cor + f"DANDO {dano} DE DANO EU ME TORNO O EXTERMINADOR DE TODO MAU!!! MORRA, CRIA DO DIABO, POIS EU SOU O ARAUTO DE TODOS OS PODERES DIVINOS!!! MUAHAHAHAHA.")
'''
'''def combate():
    while jogador.vida>0:
        print(narrador + 'O que você quer fazer?')
        acao = input('Atacar, fugir, ou conversar? ')
        if acao.lower() == 'atacar' and jogador.vida>0:
            dano_no_enemy(int(choices(jogador.dano, jogador.prob)[0]))
            if inimigo.vida>0:
                print(inimigo.cor + 'O inimigo decidiu atacar!')
                dano_no_player(int(choices(inimigo.dano, inimigo.prob)[0]))
            else:
                break
        elif acao.lower() == 'fugir':
            print('Ao tentar fugir, você tropeça.', inimigo.cor + 'O inimigo aproveita sua incompetência e ataca!')
            dano_no_player(int(choices(inimigo.dano, inimigo.prob)[0]))
            combate()
            break
        elif acao.lower() == 'conversar':
            print(narrador + 'TÁ ACHANDO QUE AQUI É NARUTO PRA VOCÊ CONVERSAR COM OS SEUS INIMIGOS?!!!')
            dano_no_player(12)
            print(narrador + 'KKKK Recebeu dano só pra deixar de ser otário.')
        else:
            print('TÁ BOBEANDO PORRA? ESCOLHE ALGUMA COISA KRL!!')
            combate()
            break'''

def combate():
    while jogador.vida>0:
        print(narrador + 'O que você quer fazer?')
        acao = input('Atacar, fugir, ou conversar? ')
        if acao.lower() == 'atacar' and jogador.vida>0:
            causar_dano(jogador, inimigo)
            if inimigo.vida>0:
                print(inimigo.cor + 'O inimigo decidiu atacar!')
                causar_dano(inimigo, jogador)
            else:
                break
        elif acao.lower() == 'fugir':
            print('Ao tentar fugir, você tropeça.', inimigo.cor + 'O inimigo aproveita sua incompetência e ataca!')
            causar_dano(inimigo, jogador)
            combate()
            break
        elif acao.lower() == 'conversar':
            print(narrador + 'TÁ ACHANDO QUE AQUI É NARUTO PRA VOCÊ CONVERSAR COM OS SEUS INIMIGOS?!!!')
            causar_dano(12, jogador)
            print(narrador + 'KKKK Recebeu dano só pra deixar de ser otário.')
        else:
            print('TÁ BOBEANDO PORRA? ESCOLHE ALGUMA COISA KRL!!')
            combate()
            break

def main():
    intro()
    combate()

main()
