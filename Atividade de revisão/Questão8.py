def fila_prioridade():
  situacao = input("Informe sua situação (idoso, gestante, PCD ou nenhum): ").lower()
  if situacao in ["idoso", "gestante", "pcd"]:
    return "Sim"
  else:
    return "Não"
print(fila_prioridade())
