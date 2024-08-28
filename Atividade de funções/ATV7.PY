'''
Crie uma função que receba um número indeterminado de valores inteiros e
depois apresente a soma deles na tela. Use: def nome_da_funcao (* parametro):
'''
def soma_valores(*numeros):
  if not numeros:
    print("Por favor, informe pelo menos um número inteiro para somar.")
    return
  soma = 0
  for numero in numeros:
    if not isinstance(numero, int):
      print(f"Erro: O valor {numero} não é um número inteiro.")
      continue
    soma += numero
  print(f"A soma dos valores informados é: {soma}")
soma_valores(1, 2, 3, 4, 5) 
soma_valores(10, 20, 30, -5)  
soma_valores(23,34,56,45,78)  
soma_valores(5, 10) 