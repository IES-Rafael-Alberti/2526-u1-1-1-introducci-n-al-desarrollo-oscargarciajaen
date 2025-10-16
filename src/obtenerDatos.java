import java.util.Scanner;

public class obtenerDatos {

    private static Scanner entrada = new Scanner(System.in);

    public static String solicitarNombre() {
        System.out.print("Introduce tu nombre: ");
        String nombre = entrada.nextLine();
        return nombre;
    }

    public static int solicitarAñoNacimiento() {
        System.out.print("Introduce el año en que naciste: ");
        int añoNacimiento = entrada.nextInt();
        return añoNacimiento;
    }

    public static int obtenerNumeroAños(int añoNacimiento) {
        int numAños = 2025- añoNacimiento;
        return numAños;
    }

    public static void mostrarMensaje(String nombre, int edad) {
        System.out.println("Hola " + nombre + ", tienes " + edad + " años.");    }

    public static void main(String[] args) {
        String nombre = solicitarNombre();
        int añoNacimiento = solicitarAñoNacimiento();
        int edad = obtenerNumeroAños(añoNacimiento);
        mostrarMensaje(nombre, edad);

        entrada.close();
    }
}
