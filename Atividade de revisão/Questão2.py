def vogal_consoante(letra):
  letra_minuscula = letra.lower()
  vogais = "aeiou"
  if letra_minuscula in vogais:
    return f"A letra '{letra}' é uma vogal.".upper()
  if len(letra_minuscula) == 1 and letra_minuscula.isalpha():
    return f"A letra '{letra}'é uma consoante."
  else:
    return f"A entrada '{letra}' não é uma letra válida.".upper()
letra_digitada = input("Digite uma letra: ")
resultado = vogal_consoante(letra_digitada)
print(resultado)