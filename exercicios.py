# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# valor1 = int(input("Entre com um número inteiro: "))
# valor2 = int(input("Entre com outro número inteiro: "))

# resultado = valor1 // valor2

# print(f"A divisão do {valor1} com o {valor2} é igual a {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# try:
#     num1 = float(input("Entre com um número inteiro: "))
#     num2 = float(input("Entre com outro número inteiro: "))

#     media = num1 / num2

#     print(f"A media dos números digitados é igual a: {media} ")

# except:
#     print("Voce não digitou um número inteiro")



# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# import math

# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    
texto = input("  Digite um texto qualquer: ").upper().replace(" ","")

print(f"{texto}")
#print(f"{texto.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Entre com uma data no seguinte formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data.split("/")

# print(f"O dia digitado foi {lista_dia_mes_ano[0]}")
# print(f"O mês digitado foi {lista_dia_mes_ano[1]}")
# print(f"O ano digitado foi {lista_dia_mes_ano[2]}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.



# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura



# try:
#     temperatura = float(input("qual a temperatura em celsius? "))
#     fahrenheit = (temperatura * 9/5) + 32
#     print(f"{temperatura}°C é igual a {fahrenheit}°F.")
# except:
#     print("Favor entrar com um valor númerico")


# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
