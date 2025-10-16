'''
Deberá escribirse un programa por cada uno de los tres lenguajes elegidos que:

    Pregunte el nombre del usuario.
    Pregunte el año de nacimiento. Y obtenga la edad del usuario.
    Muestre un mensaje que diga: "Hola [nombre del usuario], tienes [x] años. Este programa está hecho en el lenguaje de programación: [lenguaje]".
'''

def solicitarNombre() -> str:
    nombre = None 
    while nombre == None:
        nombre = input("Introduce su nombre: ")
        if nombre.isdigit():
            print("El nombre no puede ser un dígito")
            nombre = None
        else:
            return nombre
        
def solicitarAñoNacimiento() -> int:
    añoNacimiento = None
    while añoNacimiento == None:
        try:
            añoNacimiento = int(input("Introduce el año en que naciste: "))
            if añoNacimiento < 1925:
                print("No creo que siguieses vivo si hubieses nacido en ese año")
                añoNacimiento = None
            elif añoNacimiento > 2025: 
                print("No has nacido todavia")
                añoNacimiento = None
            else:
                return añoNacimiento
        except ValueError:
            print("El año no puede contener caracteres alfabéticos ni especiales")

def calcularEdad(añoNacimiento: int) -> int: 
    edad = 2025 - añoNacimiento
    return edad

def main():
    nombre = solicitarNombre()
    añoNacimiento = solicitarAñoNacimiento()
    edad = calcularEdad(añoNacimiento)
    print(f"Hola {nombre}, tienes {edad} años.")

if __name__ == "__main__":
    main()

