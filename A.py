def calculadora(x,y,o) -> float:
    x, y, o = float(x), float(y), str(o)
    match o:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y
        case _:
            print("Operación inválida")

if __name__ == "__main__":
    x = input("Ingrese el primer número: ")
    y = input("Ingrese el segundo número: ")
    o = input("Ingrese la operación deseada:\n\n + (suma)\n - (resta)\n * (multiplicación)\n / (división)\n ")
    print(calculadora(x, y, o))










