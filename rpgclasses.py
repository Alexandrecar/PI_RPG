from random import choices
import colorama
from colorama import Fore, Back, Style

class personagem:
  def __init__(self, nome, vida, dano, prob, cor):
      self.nome = nome #nome do personagem
      self.vida = vida #vida total do personagem
      self.dano = dano #dano de ataque
      self.prob = prob #probabilidade de dano normal e dano crítico
      self.cor = cor #cor do texto associado ao personagem

jogador = personagem("place_holder", 100, [7,9], [10,2],Fore.BLUE)

inimigo = personagem("place_holder", 25, [18,21], [10,2],Fore.RED)

narrador = Fore.RESET #redefinindo a cor do texto de quando é o "narrador" falando