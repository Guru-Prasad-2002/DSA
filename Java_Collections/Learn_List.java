// import java.util.List;
import java.util.*;

public class Learn_List{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        // ArrayList<String> arr=new ArrayList<String>();
        // arr.add("Prasad");
        // arr.add(0,"Guru");
        // System.out.println(arr);
        List<Integer> list = new ArrayList<Integer>();
        list.add(2);
        System.out.println(list);
        list.add(0,-1);
        System.out.println(list);
        sc.close();
    }
}