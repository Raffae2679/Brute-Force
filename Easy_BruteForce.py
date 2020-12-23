from zipfile import ZipFile
from datetime import datetime
import string



def BruteForce():

	digits = string.digits # Pega todos os digitos de 0 - 9
	combinacoes = digits

	combinacoes = [x+y for x in combinacoes for y in digits] # Cria uma lista com combinações de dois numeros, ex: 00,29,09,42

	contador = 0

	for i in combinacoes:
		for j in combinacoes:
			if TryOpen(str(i)+str(j)):
				end_time = datetime.now()
				print("A senha é ", str(i)+str(j))
				print('Tempo necessario para quebrar a senha: {}'.format(end_time - start_time))
				print("Foram testadas "+ str(contador)+" combinações até sua senha ser quebrada")
			else:
				contador +=1
				

				


def TryOpen(password):
	zip_file = 'facil.zip'

	try:
		with ZipFile(zip_file) as zf:
			zf.extractall(pwd=bytes(password,'utf-8'))
			print("Força Bruta Completa !!!")
			return True
	except:
		return False
		



start_time = datetime.now()
BruteForce()