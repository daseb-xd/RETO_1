def es_palindromo(palabra) -> str:

    # Se pasa la palabra a minúsculas para evitar bugs
    palabra = palabra.lower()
    palabra_inv = ""
    # Se invierte la palabra recorriéndola desde el final hasta el inicio
    for i in range(len(palabra)-1, -1, -1):
        palabra_inv += palabra[i]
    
    # Se usa match-case para comparar la palabra original con su versión invertida
    match palabra:
        case palabra if palabra == palabra_inv:
            return "La palabra ES un palíndromo"
        case _:
            return "La palabra NO es un palíndromo"
        
if __name__ == "__main__":

    palabra = input("Ingrese una palabra: ")
    print(es_palindromo(palabra))