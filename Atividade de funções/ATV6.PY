'''
Faça um programa que converta da notação de 24 horas para a notação de 12
horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para personalizar a saída.
'''

hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))
def converter_hora(hora):
    return (hora -12)
def imprime_hora(hora,minuto):
    if(hora <= 12):
        print(hora,minuto,"AM")
    else:
        print(converter_hora(hora), minuto, "PM")
imprime_hora(hora, minuto)