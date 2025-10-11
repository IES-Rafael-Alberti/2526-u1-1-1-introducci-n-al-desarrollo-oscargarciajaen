#include <stdio.h> // Para funciones de entrada/salida

void obtenerNombre(char nombre[], int tam) {
    printf("Ingrese su nombre: ");
    fgets(nombre, tam, stdin);
}

int obtenerAno() {
    int anoNacimiento;
    printf("Ingrese el año de tu nacimiento: ");
    scanf("%d", &anoNacimiento);
    return anoNacimiento;
}

int main(void) {
    char nombre[25];
    int anoNacimiento;
    int edad;

    obtenerNombre(nombre, 25);   // se pasa el array y su tamaño
    anoNacimiento = obtenerAno(); // Se almacena el año

    edad = 2025 - anoNacimiento; // Calculo la edad

    printf("Hola %s, tienes %d años.\n", nombre, edad); // Muestro por pantalla el saludo y la edad

    return 0;
}
