# -*- coding: utf-8 -*-
"""RPGpt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OrYtNh6pa8GJvJkNivJYGy2yAodcZxOq
"""

#O RPG DO MAL, por enquanto só sistema de combate

from random import choices
import colorama
from colorama import Fore, Back, Style
nome = ()
vida = 100
vidaE = 25
danoE = [18,21]
Eprob = [10,2]
danoP = [7,9]
Pprob = [10,2]

def intro():
  global nome
  print('Você acorda no meio do nada, apenas com um desejo insaciável de se aventurar.')
  nome = input('Qual o seu nome grande aventureiro? ')
  print(f'''Ahh, então você é {nome}...
Que nome bobo. Enfim, sua jornada começa agora...
Kkkk, {nome}. Aiai, esses jovens de hoje em dia, senhor.''')

def dano_no_player(dano):
  global vida
  vida-=dano
  if vida>0:
    print(Fore.BLUE + f'Oh não, perdi {dano} de vida. Tenho apenas {vida} de vida agora.')
  else:
    print(Fore.BLUE + f"""OH!!! Recebi {dano} de dano e minha vida chegou ao fim. Um golpe extremamente fatal. Estou vendo minha vida passar diante de meus olhos.
OH! Se ao menos o Chapolim Colorado tivesse vindo ao meu resgate!!! AHH, que vida mais injusta! Maldito seja você, ó mundo cruel!!!! Fim de minha jornada magnífica""")

def dano_no_enemy(dano):
  global vidaE
  vidaE-=dano
  if vidaE>0:
    print(Fore.BLUE + f'Dei {dano} de dano. O cara está com {vidaE} de vida. ATACAR!!!!!!')
  else:
    print(Fore.BLUE + f"DANDO {dano} DE DANO EU ME TORNO O EXTERMINADOR DE TODO MAU!!! MORRA, CRIA DO DIABO, POIS EU SOU O ARAUTO DE TODOS OS PODERES DIVINOS!!! MUAHAHAHAHA.")

def combate():
  global vida
  global vidaE
  while vida>0:
    print(Fore.RESET + 'O que você quer fazer?')
    acao = input('Atacar, fugir, ou conversar? ')
    if acao.lower() == 'atacar' and vida>0:
      dano_no_enemy(int(choices(danoP, Pprob)[0]))
      if vidaE>0:
        print(Fore.RED + 'O inimigo decidiu atacar!')
        dano_no_player(int(choices(danoE, Eprob)[0]))
      else:
        break
    elif acao.lower() == 'fugir':
      print('Ao tentar fugir, você tropeça.', Fore.RED + 'O inimigo aproveita sua incompetência e ataca!')
      dano_no_player(int(choices(danoE, Eprob)[0]))
      combate()
      break
    elif acao.lower() == 'conversar':
      print('TÁ ACHANDO QUE AQUI É NARUTO PRA VOCÊ CONVERSAR COM OS SEUS INIMIGOS?!!!')
      dano_no_player(12)
      print(Fore.RESET + 'KKKK Recebeu dano só pra deixar de ser otário.')
    else:
      print('TÁ BOBEANDO PORRA? ESCOLHE ALGUMA COISA KRL!!')
      combate()
      break

def main():
  intro()
  combate()

main()
