class Container<T>{
    T value;
    public void show(){
        System.out.println(this.value.getClass().getName());
    }
}

public class Generics {
    public static void main(String[] args){
        Container<Integer> obj=new Container<>();
        obj.value=10;
        obj.show();    
    }
}
