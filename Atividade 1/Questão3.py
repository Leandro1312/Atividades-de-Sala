def turno_estudo(turno):
  if turno.upper() == "M":
    return "Bom Dia!"
  elif turno.upper() == "V":
    return "Boa Tarde!"
  elif turno.upper() == "N":
    return "Boa Noite!"
  else:
    return "Valor Inválido!"
turno_digitado = input("Digite seu turno de estudo (M-matutino, V-Vespertino ou N-Noturno): ")
saudação = turno_estudo(turno_digitado)
print(saudação)