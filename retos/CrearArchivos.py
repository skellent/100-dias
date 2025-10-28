# Script de creacion automatica de archivos markdown para cada reto

for i in range(1,101):
	with open(f'reto-{i}.md', 'w') as archivo:
		archivo.write(f'# Reto Nro. "{i}"')
		archivo.close()
