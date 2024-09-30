#inicializacao de Variaveis
num = ""
numBackup = ""
continue_ = True
controlador = False
numTotal = 0.0
numTotalBackup = 0.0
verificador = False
while (controlador == False):
  nome = input("digite seu nome:")
  if (nome != "") and (nome != False):
    controlador = True
  else:
    print("Você Precisa Digitar um nome válido.")
else:
  #instrucoes para os usuarios
  print("Olá", nome,"! Seja Bem-Vindo à calculadora.")
  print("Digite um número entre -99999 e 99999 para começarmos:")
  while True:
    try:
        num_inicial = float(input(""))
        if not -99999 <= num_inicial <= 99999:
            raise ValueError("Número está fora do alcance")
    except ValueError as e:
        print("Valor inválido: ", e)
    else:
      numTotal +=num_inicial
      num += str(num_inicial)
      break
  print("Agora digite a Operação que deseja realizar, as operações incluem: \n para somar : + \n para subtrair: - \n para multiplicar: x \n para dividir: / \n para elevar: ^ \n para porcentagem: % \n \n A qualquer momento: \n Para limpar o número anterior digite: C \n para apagar tudo: digite AC \n para fechar digite: SAIR.")
  while True:
    try:
        op = input("")
        if (op==False) or (op==""):
            raise ValueError("Operação vazia.")
    except ValueError as e:
        print("Valor inválido: ", e)
    else:
      if(op == "SAIR"):
        continue_ = False
      break
  print("O último passo é digitar o próximo número da equação e estamos prontos! Se divirta. Após cada operação ou número, digite enter.")
  while continue_ == True:
    while True:
      try:
          num_ = input("")
          if ((num_== False) or (num_=="")):
            verificador = False
            raise ValueError("Operação vazia.")
      except ValueError as e:
          print("Valor inválido: ", e)
      else:

        if num_.isdigit():
          numBackup = num
          numTotalBackup = numTotal
          match op:
            case "+":
              numTotal += float(num_)
              num += str(op)+str(float(num_))
              print(num,"=",numTotal)
              break
            case "-":
              numTotal -= float(num_)
              num += str(op)+str(float(num_))
              print(num,"=",numTotal)
              break
            case "x":
              numTotal *= float(num_)
              num += str(op)+str(float(num_))
              print(num,"=",numTotal)
              break
            case "/":
              numTotal /= float(num_)
              num += str(op)+str(float(num_))
              print(num,"=",numTotal)
              break
            case "^":
              numTotal **= float(num_)
              num += str(op)+str(float(num_))
              print(num,"=",numTotal)
              break
            case "%":
              numTotal *= float(num_)/100
              num += 'x'+str(float(num_))+str(op)
              print(num,"=",numTotal)
              break
            case _:
              numTotal -= float(num_)
              num += str(op)+str(float(num_))
              print(num,"=",numTotal)
              break
        else:
          op = num_
          match op:
            case "SAIR":
              continue_ = False
              break
            case "C":
              num = numBackup
              numTotal = numTotalBackup
              print(num)
              break
            case "AC":
              op = "+"
              num = ""
              numTotal = 0.0
              print("________________________________________________________________________")

        break
print("Sessão Encerrada.")
