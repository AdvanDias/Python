print("SEJA BEM-VINDO(A) AO VALIDADOR DE CPF!")
cpf = input("PARA INICIAR, DIGITE O SEU CPF: ")
cpf = cpf.replace(".","") # Retirando os "." caso for digitado com mascara o cpf
cpf = cpf.replace("-","") # Retirando os "-" caso for digitado com mascara o cpf
if len(cpf) == 11:  # Verificando se o cpf tem apenas 11 digitos, caso contrario ele vai no else cpf inválido
  if (cpf) == "00000000000" or (cpf) == "11111111111" or (cpf) == "22222222222" or (cpf) == "333333333333" or (cpf) == "44444444444" or (cpf) == "55555555555" or (cpf) == "66666666666" or (cpf) == "77777777777" or (cpf) == "88888888888" or (cpf) == "99999999999": 
    print("CPF INVÁLIDO!") # caso o cpf for igual a um desses criterios ele finaliza também, caso não segue o fluxo
  else: 
    contador = 0
    GuardaDigito = 0
    resultado = 0
    total = 0
    valida = 0
    num = 10
    for contar in cpf:  # o for para percorrer os 11 caracteres da variável cpf
      GuardaDigito = int(cpf[contador]) # guardar o valor que está na posição da variável cpf
      contador = contador + 1 # o contador serve para mudar a posição da variável cpf e assim pegar o proximo valor
      if (num >= 2):  # o if para fazer a validação aritimética dos dois ultimos números do cpf. a variável "num" começa com 10 e vai decrementanto -1 ate chegar em 2
        resultado = GuardaDigito * num # GuardaDigito que tem o valor da posição do cpf multiplicado por "num" que é 10
        total = total + resultado # o total vai ser a soma da variável "resultado" + total
        num = num - 1  # decrementando a variável "num" para ser 9 na proxima execução
    valida = total * 10 % 11 # calculo do resto da divisão e finaliza o for.
    if (valida == 10):  
      valida = 0
    if (valida == int(cpf[9])): # validando se o resto da divisão é igual ao 10º digito do cpf. caso atenda vai para o validação do 11º digito. usei o mesmo script de antes mudando apenas a variável "num" para 11
      contador = 0
      GuardaDigito = 0
      resultado = 0
      total = 0
      valida = 0
      num = 11 # alterado para validação aritimética 
      for contar in cpf:  
        GuardaDigito = int(cpf[contador])
        contador = contador + 1
        if (num >= 2):  
          resultado = GuardaDigito * num
          total = total + resultado
          num = num - 1 
      valida = total * 10 % 11
      if(valida == 10): 
        valida = 0
      if (valida == int(cpf[10])):  
        print("CPF É VÁLIDO") # caso tudo estiver ok o cpf é válido
      else: 
        print("CPF INVÁLIDO") # caso a validação do resto da divisão não for igual ao 11º digito do cpf
    else: # caso a validação do resto da divisão não for igual ao 10º digito do cpf
      print("CPF INVÁLIDO")
else: 
  print("CPF INVÁLIDO!") # caso cpf for diferente 11 caracteres