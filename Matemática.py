from time import sleep
from random import randint



print("Victor ©")
print("=" *40)
print("ESCOLA DJALMA MATHEUS SANTANA")
print("=" *40)

aluno = input("Qual Seu Nome Aluno ?: ")

if aluno == "victor":
	print("Ah Sim Meu Criador")
elif aluno == "Victor":
	print("Ah Sim Meu Criador")
else:
	print(f" {aluno} ,Seja Bem Vindo")
sleep(1)
print("Script De Matematica")
sleep(1)
print("**" *20)
print("\033[4;31mVOCÊ TEM QUE TER 10 ACERTOS\033[0;0m")
print("**" *20)
sleep(1)
print('''
1- Começar
2 - Sair''')
c = int(input("Vamos Começar ? [1/2] :"))
if c == 1:
	print("Okay Vamos Iniciar")
else:
	exit()
	

for c in range(0,2):
	print("=" *20)
	print("\033[4;32mCARREGANDO\033[0;0m")
	print("=" *20)
	sleep(1)
erros = 0
resultado = 0
chances = 5
while resultado < 10:
	randint(1,10)
	primer = randint(1,10)
	primer2 = randint(1,10)
	print("=" *20)
	pergunta = int(input(f"Quanto E  {primer} x {primer2} = ? : "))
	print("=" *20)
	result = primer * primer2
	if(pergunta == result):
		print("\033[4;33;0mAcertou\033[0;0;0m")
		resultado +=1
		print("Parabéns")
		print("*****")				
	else:
		print("Errou")
		chances -=1
		erros +=1
		print(f"Chances {chances}")
		print(f"A Resposta Certa Seria : {result}")
		if(chances == 0):			
			print("Game Over")
			print(f"Erros : {erros}")
			print(f"Acertos: {resultado}")
			exit()
if resultado == 10:
	print(f"VOCÊ ACERTOU: {resultado}")
	print(f"VOCÊ ERROU : {erros}")
	input()