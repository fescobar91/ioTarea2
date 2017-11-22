from random import randint 

def main():
	#Cantidad de dimensiones
	d=2
	#Cantidad de Puntos
	n=15
	generarData(d,n)

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