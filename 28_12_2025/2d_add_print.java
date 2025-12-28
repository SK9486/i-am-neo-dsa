import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        ArrayList<ArrayList<Integer>> matx = new ArrayList<>();
        ArrayList<Integer> row;
        for(int i =0;i<rows;i++){
            row = new ArrayList<>();
            for(int j = 0;j<cols;j++){
                row.add(sc.nextInt());
            }
            matx.add(row);
        }
        int sum = 0;
        for(ArrayList<Integer> mat : matx){
            sum = 0;
            for(int a : mat){
                sum+=a;
                System.out.print(a+" ");
            }
            System.out.println("SUM :"+sum);
        }
    }

};
