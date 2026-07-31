# Conversor de Monedas
cantidad = float(input("Ingrese la cantidad en MXN: "))
print ("Monedas, Usd 1, Eur 2, Thb 3, Jpy 4, Krw 5,Aud 6, Pen 7, Cad 8, Vez 9, Ars 10")
opcion = int(input("Seleccione la moneda: "))
match opcion:
    case 1:
        resultado = cantidad / 16.5
        manera = "Usd"
    case 2:
        resultado = cantidad / 18
        manera = "Eur"
    case 3:
        resultado = cantidad / 0.45
        manera = "Thb"
    case 4:
        resultado = cantidad / 0.12
        manera = "Jpy"
    case 5:
        resultado = cantidad / 0.013
        manera = "Krw"
    case 6:
        resultado = cantidad / 11.5
        manera = "Aud"
    case 7:
        resultado = cantidad / 2.8
        manera = "Pen"
    case 8:
        resultado = cantidad / 8.2
        manera = "Cad"
    case 9:
        resultado = cantidad / 0.0023
        manera = "Vez"
    case 10:
        resultado = cantidad / 0.046
        manera = "Ars"
    case _:
        print ("Opcion invalida.")
print ("Resultado:", resultado, manera)