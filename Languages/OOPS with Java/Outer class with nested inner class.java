// Question 8: Develop a JAVA program to create an outer class with a function display. Create another class inside the outer class named inner
// with a function called display and call the two functions in the main class.

class OuterClass {
    void display() {
        System.out.println("Outer class display method");
    }

    class InnerClass {
        void display() {
            System.out.println("Inner class display method");
        }
    }
}

public class OuterInnerDemo {
    public static void main(String[] args) {
        OuterClass outer = new OuterClass();
        outer.display();

        OuterClass.InnerClass inner = outer.new InnerClass();
        inner.display();
    }
}
