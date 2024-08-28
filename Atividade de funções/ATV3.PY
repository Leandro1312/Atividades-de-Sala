'''
Faça um programa que receba três números do usuário, e identifique o maior
através de uma função e o menor número através de outra função.
'''
def encontrar_maior(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
     maior = n1
    if n2 >= n1 and n2 >= n3:
     maior = n2
    else:
     maior = n3
    return maior
def encontrar_menor(n1,n2,n3):
    if n1<= n2 and n1<= n3:
        menor = n1
    if n2<= n1 and n2<= n3:
        menor = n2
    else:
      menor = n3
    return menor
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
maior = encontrar_maior(n1, n2, n3)
menor = encontrar_menor(n1, n2, n3)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
        
        