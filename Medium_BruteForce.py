import string
import time
from datetime import datetime


def BruteForce():

	digitos = string.ascii_letters + string.digits

	combinacoes = digitos

	for i in range(0,1):
		combinacoes = [a+b for a in combinacoes for b in digitos]

	
	for i in combinacoes:
		for j in combinacoes:
			for k in combinacoes:
				for l in combinacoes:
					senha = i+j+k+l
					if TryOpen(senha):
						end_time = datetime.now()
						print("A senha é ", senha)
						print('Tempo necessario para quebrar a senha: {}'.format(end_time - start_time))
						return

def TryOpen(password):
	zip_file = 'medio.zip'

	try:
		with ZipFile(zip_file) as zf:
			zf.extractall(pwd=bytes(password,'utf-8'))
			print("Tu conseguiu, partner!")
			return True
	except:
		print("Senha negada: "+password)
		return False


start_time = datetime.now()
BruteForce()
print("GG")