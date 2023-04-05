valor_compras = float(input('Digite o valor das compras R$ '))
desconto = float(input('Digite o valor do desconto R$ '))
quantidade_itens = int(input('Digite a quantidade de itens: '))

print(f'O valor final das compras será R${valor_compras-desconto}, já considerando o valor do desconto de R${desconto}')
print(f'O custo médio de cada item é R${(valor_compras-desconto)/quantidade_itens}')