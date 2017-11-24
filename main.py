from random import randint 
#Maldito pancho
#pancho pancho hishishishishisihsi
# aaaa el push
#asdasdasdasdasds
def main():
	#Cantidad de dimensiones
	d=2	
	#d=3
	#Cantidad de Puntos
	n=randint(1,19)	
	#n=15
	generarData(d,n)
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
#	print("DATASET")
#	print(dataset)
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
	print("d: %d" %(d))
	print("n: %d" %(n))
	print("X")
	print(dataset1)
	print("Y")
	print(dataset2)

	if(d==2):
		noDominados1 = puntos2D(d,n,dataset1)
		noDominados2 = puntos2D(d,n,dataset2)
		print("Puntos no dominados de X")
		print(noDominados1)
		print("Puntos no dominados de Y")
		print(noDominados2)
		nadirX = nadir2D(noDominados1)
		nadirY = nadir2D(noDominados2)
		print("Punto nadir de X: (%d,%d)" %(nadirX[0],nadirX[1]))
		print("Punto nadir de Y: (%d,%d)" %(nadirY[0],nadirY[1]))
	if(d==3):
		puntos3D(d,n,dataset1)


def puntos2D(d,n,dataset1):
	noDominadosDS1 = []
	noDominadosDS1 = dominated2D(n,d,dataset1)
	#print("Puntos no Dominados en 2D:")
	return noDominadosDS1
	

def puntos3D(d,n,dataset1):
	print("3D")
	noDominadosDS1 = []
	noDominadosDS1 = dominated3D(n,d,dataset1)
	print("Puntos no Dominados en 3D:")
	print(noDominadosDS1)

def nadir2D(noDominados):
	ideal = []
	min  = 99999
	max = 0
	minPunto = []
	maxPunto = []
	for i in range(0,len(noDominados)):
		if(noDominados[i][0] <= min):
			min = noDominados[i][0]
			if(minPunto == []):
				minPunto.append(noDominados[i][0])
				minPunto.append(noDominados[i][1])
			else:
				minPunto = []
				minPunto.append(noDominados[i][0])
				minPunto.append(noDominados[i][1])
		if(noDominados[i][1] >= max):
			max = noDominados[i][1]
			if(maxPunto == []):
				maxPunto.append(noDominados[i][0])
				maxPunto.append(noDominados[i][1])
			else:
				maxPunto = []
				maxPunto.append(noDominados[i][0])
				maxPunto.append(noDominados[i][1])
	ideal = [maxPunto[0],minPunto[1]]
	nadir = [minPunto[0],maxPunto[1]]
	return nadir	

def dominated2D(n,d,data):
	xDominado = []
	if(d==2):
		n = len(data)
		#print(n)
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

def dominated3D(n,d,data):
	xDominado = []
	if(d==3):
		n = len(data)
		#print(n)
		for i in range(0,n):
			flag = 0
			for j in range(0,n):
				if(data[i][0] >= data[j][0] or data[i][1] <= data[j][1] or data[i][2] <= data[j][2]):
					flag = flag +1
				if(data[i][0] == data[j][0] and data[i][1] > data[j][1] and data[i][2] > data[j][2]):
					flag = flag - 1
				if(data[i][0] < data[j][0] and data[i][1] == data[j][1] and data[i][2] == data[j][2]):
					flag = flag -1
			if(flag == n):
				flag2 = 0
				for k in range(0,len(xDominado)):
					if(data[i][0] == data[k][0] and data[i][1] == data[k][1] and data[i][2] == data[k][2]):
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
