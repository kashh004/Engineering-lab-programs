// Question 12: Develop a program to create a class MyThread. In this class, create a constructor, call the base class constructor using super,
// and start the thread. The run method of the class starts after this. It can be observed that both main thread and created child thread
// are executed concurrently.

class MyThread extends Thread {
    public MyThread(String name) {
        super(name);
    }

    @Override
    public void run() {
        System.out.println(getName() + " is running");
    }
}

public class MyThreadDemo {
    public static void main(String[] args) {
        MyThread thread = new MyThread("Child Thread");
        thread.start();

        System.out.println("Main thread is running");
    }
}
