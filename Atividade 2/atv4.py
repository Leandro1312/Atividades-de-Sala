def calculadora(num1, num2):
  soma = num1 + num2
  subtracao = num1 - num2
  try:
    multiplicacao = num1 * num2
  except ZeroDivisionError:
    multiplicacao = "Divisão por zero!"
  try:
    divisao = num1 / num2
  except ZeroDivisionError:
    divisao = "Divisão por zero!"
  resultado = {
      'soma': soma,
      'subtracao': subtracao,
      'multiplicacao': multiplicacao,
      'divisao': divisao
  }
  return resultado


numero1 = 10
numero2 = 5

resultado_calculadora = calculadora(numero1, numero2)

print(f"A soma de {numero1} e {numero2} é: {resultado_calculadora['soma']}")
print(f"A diferença entre {numero1} e {numero2} é: {resultado_calculadora['subtracao']}")
print(f"A multiplicação de {numero1} e {numero2} é: {resultado_calculadora['multiplicacao']}")
print(f"A divisão de {numero1} por {numero2} é: {resultado_calculadora['divisao']}")

numero1 = 10
numero2 = 5

resultado_calculadora = calculadora(numero1, numero2)

print(f"A soma de {numero1} e {numero2} é: {resultado_calculadora['soma']}")
print(f"A diferença entre {numero1} e {numero2} é: {resultado_calculadora['subtracao']}")
print(f"A multiplicação de {numero1} e {numero2} é: {resultado_calculadora['multiplicacao']}")
print(f"A divisão de {numero1} por {numero2} é: {resultado_calculadora['divisao']}")