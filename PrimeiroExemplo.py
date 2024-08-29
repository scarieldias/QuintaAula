dia = int(input("Qual o dia de hoje? "))
pedidoPizza = int(input("Quantas pizza comprou? "))
pedidoBebida = int(input("Quantas bebida comprou? "))
pedidoBolo = int(input("Quantos Bolos comprou? "))
pedidoDoce = int(input("Quantos Doces comprou? "))


# Declarando Variaveis

diaFesta = 26
pedidoMinimoPizza = 10
pedidoMinimoBebida = 12
pedidoMinimoBolo = 5
pedidoMinimoDoce = 600

if diaFesta == dia:
    print("Ana esta fazendo as compras no dia da festa!")
else:
    print("Ana esta fazendo compra adiantada!")

if (pedidoMinimoPizza <= pedidoPizza):
    print("Ana comprou pizzas Suficientes!")
else:
    print("Ana comprou pizzas insuficientes!")

if (pedidoMinimoBebida < pedidoBebida):
    print("Ana comprou mais bebida que o necessario!")
else:
    print("Ana comprou bebidas insuficientes!")

if (pedidoMinimoBolo <= pedidoBolo):
    print("Ana excedeu a compra de bolo!")
else:
    print("Ana comprou bolo insuficiente!")

if (pedidoMinimoDoce < pedidoDoce):
    print("Ana nao comprou doces suficientes!")
else:
    print("Ana comprou doces insuficientes!")




