/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package operadoresaritmeticos;

/**
 *
 * @author André
 */
public class OperadoresAritmeticos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*int n1 = 3;
        int n2 = 5;
        float m = (n1 + n2)/2;
        System.out.println("A média é igual a "+ m);*/
        
        /*int numero = 5;
        numero++;
        System.out.println(numero);
        numero--;
        System.out.println(numero);*/
        /*int valor = 5 + numero++;
        System.out.println(valor);
        
        Quando o "++" esta no final o nº que está recebendo não vai contar ele.
        
        int valor2 = 5 + ++numero;
        System.out.println(valor2);*/
        
        /*int numero = 10;
        int valor = 4 + numero--;
        System.out.println(valor);
        System.out.println(numero);*/
        
        /*int x = 4;
        x *= 2;
        System.out.println(x);*/
        
        /*float v = 8.5f;
        int ar = (int) Math.round(v);
        System.out.println(ar);*/
        
        double ale = Math.random();  //número entre 0.0 e 1.0
        int n = (int) (15 + ale * (50-15));
        System.out.println(n);
    }
    
}
