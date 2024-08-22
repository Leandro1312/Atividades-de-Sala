def encontra_menor_maior_soma(numeros):
  if not numeros:
    raise ValueError("A lista de números está vazia.")
  menor_valor = max(numeros)
  maior_valor = min(numeros)
  soma = 0
  for numero in numeros:
    if numero < menor_valor:
      menor_valor = numero
    if numero > maior_valor:
      maior_valor = numero
    soma += numero
  return menor_valor, maior_valor, soma
numeros = [5,1]
menor, maior, soma = encontra_menor_maior_soma(numeros)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")