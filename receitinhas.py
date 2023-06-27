def checa_receita(receita, despensa):
  ingrediente1 = list(receita)[0]
  ingrediente2 = list(receita)[1]
  ingrediente3 = list(receita)[2]
  quociente1 = despensa[ingrediente1]//receita[ingrediente1]
  quociente2 = despensa[ingrediente2]//receita[ingrediente2]
  quociente3 = despensa[ingrediente3]//receita[ingrediente3]
  
  val = (min(quociente1, quociente2, quociente3))
  if val < 0:
      return(0)
  else:
      return(val)

def receita_feita(receita,despensa):
  ingrediente1 = list(receita)[0]
  ingrediente2 = list(receita)[1]
  ingrediente3 = list(receita)[2]
  despensaFake = despensa
  
  if despensaFake[ingrediente1] >= receita[ingrediente1] and despensaFake[ingrediente2] >= receita[ingrediente2] and despensaFake[ingrediente3] >= receita[ingrediente3]:
      despensaFake[ingrediente1] -= receita[ingrediente1]
      despensaFake[ingrediente2] -= receita[ingrediente2]
      despensaFake[ingrediente3] -= receita[ingrediente3]
  

  
def quant_des(despensa):
  despensa['linhaca'] = int(input('Quantas gramas de linhaça têm na despensa? '))
  despensa['aveia'] = int(input('Quantas gramas de aveia têm na despensa? '))
  despensa['acucar'] = int(input('Quantas gramas de açúcar têm na despensa? '))
  despensa['cacau'] = int(input('Quantas gramas de cacau têm na despensa? '))

def main():
  pudim = {'linhaca': 15, 'aveia': 50, 'acucar': 120}
  bolo = {'aveia': 30, 'acucar': 10, 'cacau': 15}
  despensa = {'linhaca': 0, 'aveia': 0, 'acucar': 0, 'cacau': 0}
  quant_des(despensa)
  receita = (input('Quer fazer bolo ou pudim? (S para sair)'))
  while receita.lower() != 's':
      if receita.lower() == 'bolo':
        print(f'Você pode fazer {receita} {checa_receita(bolo, despensa)} vez(es).')
        receita_feita(bolo,despensa)
        print(f'''Com os ingredientes que sobraram dá pra fazer bolo de novo mais {checa_receita(bolo, despensa)} vez(es).
  É possível fazer pudim {checa_receita(pudim, despensa)} vez(es)''')
      elif receita.lower() == 'pudim':
        print(f'Você pode fazer {receita} {checa_receita(pudim, despensa)} vez(es)')
        receita_feita(pudim,despensa)
        print(f'''Com os ingredientes que sobraram dá pra fazer pudim de novo mais {checa_receita(pudim, despensa)} vez(es).
  É possível fazer bolo {checa_receita(bolo, despensa)} vez(es)''')
      else:
        print('Entrada inválida.')
      if checa_receita(pudim, despensa) <= 0 and checa_receita(bolo, despensa) <= 0:
        break
      receita = input('Quer fazer bolo ou pudim? (S para sair) ')

main()

 #despensa = {'linhaca': 50, 'aveia': 200, 'acucar': 500, 'cacau': 100}
#checa_receita(pao, despensa)