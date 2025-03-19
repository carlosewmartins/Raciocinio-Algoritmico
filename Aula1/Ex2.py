locacao = lambda dias: dias * 100

diaria = int(input('Por quantos dias deseja locar um carro? '))
diaria = float(diaria)
print(f"O valor final de sua locacao sera: R$ {locacao(diaria):.2f}")