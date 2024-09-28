import re
import sys

cpf_digitado = input("Digite seu CPF: ")
cpf_apenasnum = re.sub(r"[^0-9]", "", cpf_digitado)

repetidos = cpf_apenasnum == cpf_apenasnum[0]*len(cpf_apenasnum)
if repetidos:
     print("Você digitou dados sequenciais.")
     sys.exit()

if len(cpf_apenasnum) == 11:
    index_cpf = list(cpf_apenasnum[:9])
    contador_multiplicação = 10
    soma_digit = 0
    index_soma = 0
    for i in index_cpf:
            soma_digit += int(index_cpf[index_soma])*(contador_multiplicação)
            contador_multiplicação -= 1
            index_soma +=1
    conta_verificacao = (soma_digit*10)%11
    if conta_verificacao > 9:
         dig1_verificado = 0
    else:
         dig1_verificado = conta_verificacao
    if int(cpf_apenasnum[-2]) == dig1_verificado:
        index_cpf = list(cpf_apenasnum[:10])
        contador_multiplicação = 11
        soma_digit = 0
        index_soma = 0
        for i in index_cpf:
            soma_digit += int(index_cpf[index_soma])*(contador_multiplicação)
            contador_multiplicação -= 1
            index_soma +=1
        conta_verificacao = (soma_digit*10)%11
        if conta_verificacao > 9:
            dig1_verificado = 0
        else:
            dig1_verificado = conta_verificacao
        if int(cpf_apenasnum[-1]) == dig1_verificado:
             print("O CPF é válido.")
        else:
             print("Os dois dígitos do CPF não são válidos.")
    else:
         print("O primeiro digito do CPF não é válido.")
else:
    print("Por favor entre com um CPF válido.")
