'''
Escreva um programa que possa cadastrar clientes ou funcionários para uma
loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
Utilize comandos de manipulação de string para personalizar a saída.
'''
def cliente(tipo):
  nome = input('digite seu nome: ')
  endereco = input('Digte seu endereco: ')
  cpf = input('digite seu cpf: ')
  print("Cliente cadastrado com sucesso.") 
  
def funcionario(tipo):
  nome = input('Digite seu nome: ')
  salario = float(input('Digite o salário: '))
  cargo = input('Digite o cargo: ')
  cpf = input('Digite o CPF: ')
  print("Funcionario cadastrado com sucesso!") 

tipo = input('Deseja cadastrar um cliente ou funcionário? (cliente/funcionario):')
if tipo == 'cliente':
  cliente(tipo)
if tipo == 'funcionario':
  funcionario(tipo)
print("Obrigado por usar o nosso programa de cadastro!") 