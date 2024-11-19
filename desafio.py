nome_usuario = input("Entre com o seu nome: ")

if nome_usuario.isdigit():
    print("Por favor, verique o seu nome. Número identificado")

elif len(nome_usuario) == 0:
    print("Vc não digitou nada")

elif nome_usuario.isspace():
    print("Vc digitou apenas espaço")
    