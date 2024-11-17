# # Exemplo que causa TypeError
# try:
#     resultado = len("teste")
#     print(f"{resultado}")
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro


# numero = "teste"
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")



# numero_inteiro = 5
# numero_flutuante = 2.5
# # Converte o inteiro para flutuante e realiza a soma
# # soma = float(numero_inteiro) + numero_flutuante
# soma = int(numero_inteiro) + numero_flutuante
# print(soma)  # Resultado: 7.5


try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")