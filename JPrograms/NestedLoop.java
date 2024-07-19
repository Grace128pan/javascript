/*
 use nested loop to find factors of numbers between 2 and 100
 */

 package JPrograms;
 
 public class NestedLoop {
    public static void main(String[] args) {
        for(int i=2; i<=100; i++) {
            System.out.print("Factor of " + i + ": ");
            for(int j=2; j<i; j++) 
                if(i%j == 0) System.out.print(j + " ");
            System.out.println();
            
        }
    }
 }