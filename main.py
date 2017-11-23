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
	print(dataset)
	for i in range(0,n):
		for j in range(0,2*d):
			if(j < d):
				aux1.append(dataset[i][j])
				#print(dataset[i][j])
			else:
				aux2.append(dataset[i][j])
				#print(dataset[i][j])
		dataset1.append(aux1)
		dataset2.append(aux2)
		print(dataset1)
		aux1.clear()
		aux2.clear()
	#print(dataset1)		
	#print("\n\n\n")
	#print(dataset2)


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
