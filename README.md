# Brute-Force

Scripts desenvolvidos para resolução de um desafio de brute force proposto pela página @geek2code. Consistia em tentar quebrar a senha de 3 arquivos rar, onde para cada um deles tinha um nível de dificuldade diferente. Até o momento só consegui desenvolver 2 dos 3, mas não consegui de fato quebrar a senha do 2 arquivo (médio), são muitas combinações e acaba por demorar muito.

## Níveis de dificuldade

### Fácil:

Consiste em quebrar uma senha de 4 digitos formado apenas por números [0, 9999]. 
Para quebrar essa senha, eu fiz uso de uma lib chamada string, passei para uma variável todos os digitos e depois preenchi uma lista com todas as combinações de dois números. Depois disso eu coloquei dois fors para percorrer a mesma lista e irem concatenando as combinações.

```
digits = string.digits # Pega todos os digitos de 0 - 9
	combinacoes = digits

	combinacoes = [x+y for x in combinacoes for y in digits] # Cria uma lista com combinações de dois numeros, ex: 00,29,09,42

	contador = 0

	for i in combinacoes:
		for j in combinacoes:
			if TryOpen(str(i)+str(j)):
```

A saída esperada após o script finalizar é essa:
```
Força Bruta Completa !!!
A senha é  7149
Tempo necessario para quebrar a senha: 0:00:07.935454
Foram testadas 7149 combinações até sua senha ser quebrada
```

### Médio:

Consiste em quebrar uma senha de 8 digitos formado por letras maiúsculas, minúsculas e números. 
Para quebrar essa senha, eu fiz uso de uma lib chamada string, passei para uma variável todas as letras e digitos, depois preenchi uma lista com todas as combinações de dois números. Por fim, coloquei 4 fors para percorrer a mesma lista, concatenando as variáveis para assim formar a "senha". Tentei fazer dessa forma, pois pensei na tatica de dividir para conquista, mas mesmo fazendo isso, leva muito tempo para finalmente quebrar, visto que temos 64^8 combinações de 8 digitos.

```
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
```

## Executando Localmente: 

> Caso você não tenha um ambiente virtual configurado para o projeto, como um VirtualEnv ou Anaconda, recomendo configurar um para que todos os passos funcionem sem erros.

1. Clone o repositório no seu ambiente local
```
$ git clone https://github.com/Raffae2679/Brute-Force.git
```
2. Acesse o diretório que foi criado/clonado
```
$ cd Brute-Force
```

3. Instale a lib necessária para abrir arquivos .rar
```
$ pip install zipfile37
```

4. Agora você deve criar o banco de dados e realizar as migrações para que o DB esteja pronto para conexão e uso pelo Django
```
$ python Easy_BruteForce.py 
ou 
$ python Medium_BruteForce.py
```


