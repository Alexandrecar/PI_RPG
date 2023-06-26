'''#O RPG DO MAL, por enquanto só sistema de combate'''

#importando as calsses e objetos criados (variaveis dos personagens)
from rpgclasses import*

def intro():
    print(narrador + 'Você acorda no meio do nada, apenas com um desejo insaciável de se aventurar.')
    jogador.nome = input('Qual o seu nome grande aventureiro? ')
    print(f'''Ahh, então você é {jogador.nome}...
Que nome bobo. Enfim, sua jornada começa agora...
Kkkk, {jogador.nome}. Aiai, esses jovens de hoje em dia, senhor.''')

#função para escolher para onde o player irá dentre os lugares na
def viagem(): 
    lugares = ['Floresta das Almas Perdidas', 'Vila Curuçá', 'Lago das Águas Passadas', 'Caverna dos Românticos Inconsequentes']
    print(narrador+"Há uma placa com os seguintes lugares.")
    for i in range(len(lugares)):
        print("    ",lugares[i])
    j=0
    destino = input('Para onde desejas ir, nobre viajante? (s para sair) ')
    while j != len(lugares):
        if destino.lower() in map(str.lower, lugares):
            if destino.lower() == lugares[j].lower():
                print(f'Você decide caminhar até {lugares[j]}')
                break
            elif destino.lower() != lugares[j].lower():
                j+=1
        elif destino.lower() == 's':
            break
        else:
            print('Aprenda a ler e decida ir pra algum lugar existente, por favor.')
            destino = input('Para onde desejas ir, nobre viajante? (s para sair) ')
            
#função de causar dano, pode ser usada com dois objetos-personagens ou uma int e um objeto que recebe o dano
def causar_dano(agressor, vitima):
    if type(agressor) == int:
        dano_causado = agressor
    else:
        dano_causado = int(choices(agressor.dano, agressor.prob)[0])
        print(agressor.fala_agressao)

    vitima.vida -= dano_causado
    print(vitima.cor + f'{vitima.nome} - vida: {vitima.vida}', inimigo.cor + f'(-{dano_causado})')
    if vitima.vida<=0:
        print(agressor.cor + agressor.fala_finalizacao)

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
    combate()
    viagem()

main()
