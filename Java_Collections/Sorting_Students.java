import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Comparator;
public class Sorting_Students {
    public static void main(String[] args){
        List<Student> s=new ArrayList<Student>();
        s.add(new Student(1,90));
        s.add(new Student(2,80));
        s.add(new Student(3,70));
        s.add(new Student(4,99));
        s.add(new Student(5,89));
        Collections.sort(s,new Comparator<Student>() {
            public int compare(Student s1,Student s2){
                int result=0;
                if(s1.marks>s2.marks){
                    result=1;
                }else if(s2.marks>s1.marks){
                    result=-1;
                }
                return result;
            }
        });
        for (Student obj:s){
            System.out.println(obj.roll_no+" "+obj.marks);
        }
    }
}
class Student{
    int roll_no;
    int marks;
    public Student(int roll_no,int marks){
        this.roll_no=roll_no;
        this.marks=marks;
    }
}
