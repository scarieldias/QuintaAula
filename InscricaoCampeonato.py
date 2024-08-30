dia = int(input("Qual o dia da inscricao? "))
pedidoIdade = int(input("Qual idade? "))
#pedidoLista = input("Esta na lista de espera? (Sim/Nao) ")



# Declarando Variaveis

diaMaximo = 28
#diaExtendido = 31
idadeMinima = 14
idadeMaxima = 17
emEspera = False
pedidoIndicacao = True

#if diaMaximo == dia:
#    print("Dia limite de inscrição!")
#elif:
#    print("Inscrição efetuada com antecedencia!")


if dia <= diaMaximo or pedidoIndicacao:
    print("Inscricao liberada para ser realizada")
    if (pedidoIdade >= idadeMinima and pedidoIdade <= idadeMaxima):
        print("Idade atende a criterio de inscricao!")
    else:
        print("Idade Incorreta para inscrição!")

