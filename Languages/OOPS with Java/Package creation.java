// Question 10: Develop a JAVA program to create a package named `mypack` and import & implement it in a suitable class.

// File: mypack/MyClass.java
package mypack;

public class MyClass {
    public void display() {
        System.out.println("Hello from MyClass in mypack");
    }
}

// File: MainClass.java
import mypack.MyClass;

public class MainClass {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj.display();
    }
}
