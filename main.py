from random import randint 

def main():
	#Cantidad de dimensiones
	d=2
	#Cantidad de Puntos
	n=15
	#generarData(d,n)
	data = open('initialData.txt','r')
	dataset1 = []
	dataset2 = []
	dataset = []
	line = data.readline()
	for i in range(0,n):
		line = data.readline()
		line = line.split("\t")
		for i in range(0,2*d):
			line[i] = line[i].strip()
			line[i] = int(line[i])
		dataset.append(line)

	aux1 = []
	aux2 = []

	for i in range(0,n):
		for j in range(0,2*d):
			if(j < d):
				aux1.append(dataset[i][j])
			else:
				aux2.append(dataset[i][j])
		dataset1.append(aux1)
		dataset2.append(aux2)
		aux1 = []
		aux2 = []
	noDominadosDS1 = []
	noDominadosDS1 = dominated2D(n,d,dataset1)
	print(noDominadosDS1)

def dominated2D(n,d,data):
	xDominado = []
	if(d==2):
		n = len(data)
		print(n)
		for i in range(0,n):
			flag = 0
			for j in range(0,n):
				if(data[i][0] <= data[j][0] or data[i][1] >= data[j][1]):
					flag = flag +1
				if(data[i][0] == data[j][0] and data[i][1] < data[j][1]):
					flag = flag - 1
				if(data[i][0] > data[j][0] and data[i][1] == data[j][1]):
					flag = flag -1
			if(flag == n):
				flag2 = 0
				for k in range(0,len(xDominado)):
					if(data[i][0] == data[k][0] and data[i][1] == data[k][1]):
						flag2 = 1
				if(flag2==0):
					xDominado.append(data[i])
				if(flag2 == 1):
					flag2 = 0
		notDominated = []
		for i in xDominado:
			if i not in notDominated:
				notDominated.append(i)
	return notDominated


def generarData(d,n):
	text_file = open("initialData.txt","w")
	print("%d\t%d" % (d,n),file = text_file)
	for i in range(0,n):
		for i in range(0,2*d):
			if(i!= (2*d-1)):
				print("%d" % (randint(0,100)), end ="\t",file = text_file)
			else:
				print("%d" % (randint(0,100)), end ="",file = text_file)			
		print("\n", end = "" , file= text_file)



main()
