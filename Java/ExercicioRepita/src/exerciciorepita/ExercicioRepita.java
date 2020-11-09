/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exerciciorepita;

import javax.swing.JOptionPane;
/**
 *
 * @author André
 */
public class ExercicioRepita {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //JOptionPane.showMessageDialog(null, "Olá Mundo!", "Boas Vindas", JOptionPane.INFORMATION_MESSAGE);
        int n, t = 0, tp = 0, ti = 0, a = 0, m = 0;
        do {
            n = Integer.parseInt(JOptionPane.showInputDialog(null, 
                    "<html>Informe um número: <em>(valor 0 interrompe)</em></html>"));
            if(n !=0){
                t++;
                if(n % 2 == 0){
                    tp ++;
                } else {
                    ti ++;
                }
                if (n > 100){
                    a++;
                }
                m += n;
            }
        } while(n != 0);
        m = m/t;
        JOptionPane.showMessageDialog(null, "<html>Resultados: <hr>" +
                "Total de Valores: "+ t 
                + "<br>Total de Pares: " + tp
                + "<br>Total de Ímpares: " + ti
                + "<br>Acima de 100: " + a
                + "<br>Média dos valores: " + m
                + "</html>");
        
        //JOptionPane.showMessageDialog(null, "Você digitou o valor " + n);
    }
    
}
