from random import randint 

def main():
	#Cantidad de dimensiones
	d=2
	#Cantidad de Puntos
	n=15
	#generarData(d,n)
	data = open('initialData.txt','r')
	dataset = []
	line = data.readline()
	for i in range(0,n):
		line = data.readline()
		line = line.split("\t")
		for i in range(0,2*d):
			line[i] = line[i].strip()
			line[i] = int(line[i])
		dataset.append(line)


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
