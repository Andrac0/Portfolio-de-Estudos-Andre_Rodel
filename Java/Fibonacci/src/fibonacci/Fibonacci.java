/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fibonacci;

/**
 *
 * @author André
 */
public class Fibonacci {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int[] fib;
        fib = new int[31];
        for(int n = 0; n<=30; n++){
            if(n == 0 || n == 1 || n == 2){
                if(n == 2){
                    fib[n] = n-1;
                    System.out.println(fib[n]);
                }else{
                    fib[n] = n;
                    System.out.println(fib[n]);
                }
            } else{
                fib[n] = fib[n-1] + fib[n-2];
                    System.out.println(fib[n]);
            }
        
        }
    }
    
}
