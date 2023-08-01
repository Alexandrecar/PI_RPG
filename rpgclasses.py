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

jogador = personagem("place_holder", 100, 100, [7,9], [15,2],Fore.BLUE, "Atacando", "Inimigo derrotado com sucesso!")

inimigo = personagem("my enemy", 25, 25, [18,21], [15,2],Fore.RED, "Ataque", "Game over. Você perdeu.")

narrador = Fore.RESET #redefinindo a cor do texto de quando é o "narrador" falando