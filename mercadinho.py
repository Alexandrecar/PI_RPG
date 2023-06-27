
'''Apresentar um menu com 3 opções:
  1. Listar produtos e preços
  2. Fazer uma compra
    - Permitir que o usuário digite nomes dos produtos até terminar a compra
    - Calcular o valor final
  3. Sair'''

def mostrar_produtos(catalago):
  for produto in catalago:
    print(f'{produto}: R${catalago[produto]}')

def compra(catalago,carrinho):
  total = 0
  produto = input('Nome do produto(s para sair): ')
  while produto != 's':
    quantidade = int(input(f'Quantas unidades de {produto}? '))
    total += quantidade * catalago[produto]
    carrinho[produto] = carrinho[produto]+quantidade
    produto = input('Nome do produto(s para sair):')
  print(f'O valor total da sua foi R${total}')
  print(carrinho)

def prodmaisvendido(carrinho):
  prod_max = max(carrinho, key=carrinho.get)
  i = 0
  j = list(carrinho)[i]
  print(list(carrinho))
  while j != list(carrinho)[2]:
    j = list(carrinho)[i]
    if all(value == carrinho[prod_max] for value in carrinho.values()):
      print('Não há produto mais vendido.')
      break
    elif carrinho[prod_max] == carrinho[j] and prod_max != list(carrinho)[i]:
      print(f'{prod_max} e {j} são os produtos mais vendidos com {carrinho[prod_max]} unidades.')
    else:
      print(f'{prod_max} é o produto mais vendido com {carrinho[prod_max]} unidades')
      break
    i+=1


def main():
  catalago = {'pao': 8, 'tapioca': 5, 'ades': 6}
  carrinho = {'pao': 0,'tapioca': 0, 'ades': 0}
  opcao = int(input('1 - Listar produtos, 2 - Relizar uma compra, 3 - Produto mais vendido, 4 - Sair: '))
  while opcao != 4:
    if opcao == 1:
      mostrar_produtos(catalago)
    elif opcao == 2:
      compra(catalago,carrinho)
    elif opcao == 3:
      prodmaisvendido(carrinho)
    else:
      print('Esta opção não existe')
    opcao = int(input('1 - Listar produtos, 2 - Relizar uma compra, 3 - Produto mais vendido, 4 - Sair: '))

  print('\nObrigada por comprar conosco, volte sempre')
main()