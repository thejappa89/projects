## Algoritmo: Calculadora de Salario IBGE
## Author: Henrique Lima (Jappa)
## GitHub: https://github.com/thejappa89
## Linkedin: https://www.linkedin.com/in/thejappa89/

## BASE DE CÁLCULO -- FAIXA 2
#Questionários realizados
B_BASE_QUESTIONARIO = 1.45 #Básico
A_BASE_QUESTIONARIO = 1.70 #Amostra
U_BASE_COORDENADAS = 0.61 #Unidades

#Pessoas Recenseadas
B_BASE_PESSOAS = 1.09 #Básico
A_BASE_PESSOAS = 1.81 #Amostra

#INICIO
ressenciador = input("Antes de começar, preciso que digite o seu nome: ")
print("-" * 40)
print(" " * 8, "IBGE - CENSO 2022")
print("-" * 40)
print(f"Seja bem vindo(a) {ressenciador}!")
print("Antes de comerçar, gostaria de informar que esta calculadora de ganhos NÃO É OFICIAL.")
print("")
print("Primeiro, preciso que digite as informações sobre os QUESTIONÁRIOS.")
b_questionario = int(input("- Questionário Básico: ")) #QUESTIONÁRIO BÁSICO
a_questionario = int(input("- Questionário de Amostra: ")) #QUESTIONÁRIO DE AMOSTRA
u_coordenadas = int(input("- Coordenadas obtidas: ")) #UNIDADES VISITADAS
print("")
print(f"Ótimo {ressenciador}, agora as informações das PESSOAS RECENSEADAS.")
b_pessoas = int(input("- no questionário Básico: "))
a_pessoas = int(input("- no questionário de Amostra: "))
print("")
print(f"Perfeito {ressenciador}, agora vou gerar seu relatório.")

#CALCULO DE VALORES
b_res_pessoas = float(b_pessoas * B_BASE_PESSOAS)
a_res_pessoas = float(a_pessoas * A_BASE_PESSOAS)
b_res_questionario = float(b_questionario * B_BASE_QUESTIONARIO)
a_res_questionario = float(a_questionario * A_BASE_QUESTIONARIO)
u_res_coordenadas = float(u_coordenadas * U_BASE_COORDENADAS)
sub_res_pessoas = float(b_res_pessoas + a_res_pessoas)
sub_res_questionarios = float(b_res_questionario + a_res_questionario + u_res_coordenadas)
res = float(sub_res_questionarios + sub_res_pessoas)

print("")
print("-" * 40)
print("RELATÓRIO DO RECENSEAMENTO")
print("-" * 40)
print("")
print(f"RECENSEADOR(A): {ressenciador}")
print("SETOR: 00000000000000")
print("")
print("")
print("-" * 5, "QUESTIONÁRIOS")
print(f"- Básico: {b_questionario}x R${B_BASE_QUESTIONARIO:5.2f} = R${b_res_questionario:5.2f}")
print(f"- Amostra: {a_questionario}x R${A_BASE_QUESTIONARIO:5.2f} = R${a_res_questionario:5.2f}")
print(f"- Unidades visitadas: {u_coordenadas}x R${U_BASE_COORDENADAS:5.2f} = R${u_res_coordenadas:5.2f}")
print("")
print("")
print("-" * 5, "PESSOAS RECENSEADAS")
print(f"- Básico: {b_pessoas}x R${B_BASE_PESSOAS:5.2f} = R${b_res_pessoas:5.2f}")
print(f"- Amostra: {a_pessoas}x R${A_BASE_PESSOAS:5.2f} = R${a_res_pessoas:5.2f}")
print("")
print("")
print(f"{ressenciador}, a estimativa do seu salário é: R${res:5.2f}.")