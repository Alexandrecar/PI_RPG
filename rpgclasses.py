'''classes'''
from random import choices,randint
from colorama import Fore, Back, Style
import time

class personagem:
  def __init__(self, nome, vida, vidaT, dano, prob, cor, fala_agressao, fala_finalizacao):
      self.nome = nome #nome do personagem
      self.vida = vida #vida líquida do personagem
      self.vidaT = vidaT #vida total do personagem
      self.dano = dano #dano de ataque
      self.prob = prob #probabilidade de dano normal e dano crítico
      self.cor = cor #cor do texto associado ao personagem
      self.fala_agressao = fala_agressao #fala ao atacar
      self.fala_finalizacao = fala_finalizacao #fala ao finalizar

narrador = Fore.RESET #redefinindo a cor do texto de quando é o "narrador" falando

jogador = personagem("place_holder", 100, 100, [7,9], [15,2],Fore.BLUE, "Atacando", "Inimigo derrotado com sucesso!")

inimigo = personagem("my enemy", 25, 25, [14,17], [15,2],Fore.RED, "Ataque", "Game over. Você perdeu.")

duendes = ['Duende Comum','Duende Guerreiro', 'Duende Rei']
aranhas = ['Aranha Gigante', 'Grupo de Aranhas Gigantes']

duendes_dano = [[inimigo.dano[0],inimigo.dano[1]],[inimigo.dano[0]+3,inimigo.dano[1]+3],[inimigo.dano[0]+5,inimigo.dano[1]+5]]
duendes_vidaT = [inimigo.vidaT, inimigo.vidaT+3, inimigo.vidaT+5]
aranhas_dano = [[inimigo.dano[0]+4,inimigo.dano[1]+4],[inimigo.dano[0]+8,inimigo.dano[1]+8]]
aranhas_vidaT = [inimigo.vidaT-2,inimigo.vidaT+3]
lista_inimigos_comuns = [[duendes, duendes_vidaT, duendes_dano], [aranhas, aranhas_vidaT, aranhas_dano]]

lista_inimigos_especiais = ['Grupo de Morcegos Gigantes','Devorador de Histórias']
inimigos_especiais_dano = [[inimigo.dano[0]+6,inimigo.dano[1]+6],[inimigo.dano[0]+10,inimigo.dano[1]+10]]
inimigos_especiais_vidaT = [32,90]