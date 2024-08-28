'''
Crie um programa de câmbio. Nesse programa adicione funções que
realizem conversões de real para dólar, real para euro e real para peso
argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
1,00 real = 0,18 dólar para Estados Unidos;
1,00 real = 0,16 euro para Portugal;
1,00 real = 0,0061 peso para Argentina;

'''
def real_para_dolar(valor_real): 
  cotacao_dolar = 0.18  
  valor_dolar = valor_real * cotacao_dolar
  return valor_dolar
def real_para_euro(valor_real):
  cotacao_euro = 0.16 
  valor_euro = valor_real * cotacao_euro
  return valor_euro
def real_para_peso_argentino(valor_real):
  cotacao_peso_argentino = 0.0061 
  valor_peso_argentino = valor_real * cotacao_peso_argentino
  return valor_peso_argentino
def main():
  while True:
    pais = input("Digite o país para qual deseja converter (EUA, Portugal, Argentina): ").upper()
    if pais not in ["EUA", "PORTUGAL", "ARGENTINA"]:
       valor_real = float(input("Digite o valor em real a ser convertido: "))
    if pais == "EUA":
      valor_convertido = real_para_dolar(valor_real)
      moeda = "dólar"
    elif pais == "PORTUGAL":
      valor_convertido = real_para_euro(valor_real)
      moeda = "euro"
    else:
      valor_convertido = real_para_peso_argentino(valor_real)
      moeda = "peso argentino"
    print(f"{valor_real:.2f} reais equivale a {valor_convertido:.2f} {moeda}.")
if __name__ == "__main__":
  main()
