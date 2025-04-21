def main():

    lista = list(map(int, input("Ingrese los números ENTEROS a evaluar, separados por espacios\n").split( )))
    lista_s = []
 
    for i , e in enumerate(lista) :

        if i == len(lista)-1 : continue

        lista_s.append(e + lista[i+1])


    print("La suma mas grande entre dos numeros consecutivos es:",max(lista_s))

main()