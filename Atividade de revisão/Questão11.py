def gerar_numeros_intervalo(limite_inferior, limite_superior):
  if limite_superior < limite_inferior:
    print("O limite superior deve ser maior que o limite inferior.")
    return
  for numero in range(limite_inferior, limite_superior):
    print(numero)
limite_inferior = int(input("Digite o limite inferior do intervalo: "))
limite_superior = int(input("Digite o limite superior do intervalo: "))
gerar_numeros_intervalo(limite_inferior, limite_superior)