conversao_f = lambda temp_c: (temp_c * 9/5) + 32

temp_c = float(input("Insira uma temperatura em Celsius: "))


print(f"A temperatura equivalente em Fahrenheit e: {conversao_f(temp_c)} °F")
