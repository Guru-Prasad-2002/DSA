import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Comparator;
public class Comparator_Example {
    public static void main(String[] args){
    // List<Integer> l=new ArrayList<Integer>();
    // Random r=new Random();
    // for(int i=0;i<25;i++){
    //     l.add(r.nextInt(100));
    // }
    // Comparator compare_obj=new Comparator_class();
    // Collections.sort(l,compare_obj);
    // for(Integer x:l){
    //     System.out.print(x+"\t");
    // }
    // System.out.println();

    // Comparator example without external class
    List<Integer> l=new ArrayList<Integer>();
    Random r=new Random();
    for(int i=0;i<25;i++){
        l.add(r.nextInt(100));
    }
    Collections.sort(l,(Integer i1,Integer i2)->{
        int result=0;
        if(i1%10>i2%10){
            result =1;
        }else if(i1%10<i2%10){
            result = -1;
        }
        return result;
    });
    for(Integer x:l){
        System.out.print(x+"\t");
    }
    System.out.println();
    }
}
class Comparator_class implements Comparator<Integer>{
    public int compare(Integer i1,Integer i2){
        int result=0;
        if(i1%10>i2%10){
            result =1;
        }else if(i1%10<i2%10){
            result = -1;
        }
        return result;
    }
}
