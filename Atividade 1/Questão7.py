def idade_para_votar():
  idade = int(input("Informe sua idade: "))
  if 18<=idade>=65:
    return "Voto obrigatório"
  elif 16 <= idade <= 17:
    return "Voto opcional"
  else:
    return "Sem direito a voto"
print(idade_para_votar())