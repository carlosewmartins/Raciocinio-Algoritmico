
# Valor KG - Tomate
valor_kg_tomate = 11.98
peso_tomate = 3.5
# def calcular_valor(quantidade,valor_kg):
#     total = quantidade * valor_kg
#     return total

calcular_valor = lambda quantidade, valor_kg: quantidade * valor_kg

print(f"Total da compra: R${calcular_valor(peso_tomate,valor_kg_tomate):.2f}")