'''classes'''
from random import choices,randint
from colorama import Fore, Back, Style
import time

class personagem:
  def __init__(self, nome, vida, dano, prob, cor, fala_agressao, fala_finalizacao):
      self.nome = nome #nome do personagem
      self.vida = vida #vida total do personagem
      self.dano = dano #dano de ataque
      self.prob = prob #probabilidade de dano normal e dano crítico
      self.cor = cor #cor do texto associado ao personagem
      self.fala_agressao = fala_agressao #fala ao atacar
      self.fala_finalizacao = fala_finalizacao #fala ao finalizar

jogador = personagem("place_holder", 100, [7,9], [15,2],Fore.BLUE, "atacando", "gg ez")

inimigo = personagem("my enemy", 25, [18,21], [15,2],Fore.RED, "cutucada", "tu eh ruim em, perdeu no tutorial besta")

narrador = Fore.RESET #redefinindo a cor do texto de quando é o "narrador" falando