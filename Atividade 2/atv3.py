def calculadora(num1, num2):
  soma = num1 + num2
  subtracao = num1 - num2
  resultado = {'soma': soma, 'subtracao': subtracao}
  return resultado
numero1 = 10
numero2 = 9
resultado_calculadora = calculadora(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é: {resultado_calculadora['soma']}")
print(f"A diferença entre {numero1} e {numero2} é: {resultado_calculadora['subtracao']}")