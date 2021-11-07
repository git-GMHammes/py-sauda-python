#  '12345'.isdigit() verdadeiro para numero
#  '1234.5'.isdigit() falso para numero
#  '12345abc'.isdigit() falso para numero
#  '12345abc'.isalnum() verdadeiro para alphanumerico
def fornecer1():
    var2: str = input(
        '\n Digite a hora, sem os minutos, com um número inteiro: ')
    if verificaDigito(var2):
        verHora(var2)
    else:
        print()
        print(f'\n ERRO: Você não digitou um número inteiro')
        fornecer2()


#
def fornecer2():
    var3: str = input(
        '\n Digite a hora, sem os minutos, com um número inteiro: ')
    if verificaDigito(var3):
        verHora(var3)
    else:
        print()
        print(f'\n ERRO: Você não digitou um número inteiro')
        fornecer1()


#
def verificaDigito(var3):
    return var3.isdigit()
#


def verHora(var1=0):
    variavel = int(var1)
    print()
    print(f'\n Você digitou: {variavel}')
    if 0 <= variavel < 12:
        print(f'\n Hora {variavel}: BOM DIA')
    elif 12 <= variavel < 18:
        print(f'\n Hora {variavel}: BOA TARDE')
    elif 18 <= variavel < 24:
        print(f'\n Hora {variavel}: BOA NOITE')
    else:
        print(f'\n Hora {variavel} Não Corresponde ao que foi solicitado')
    return exit('\n Fim do programa')


#
fornecer1()
