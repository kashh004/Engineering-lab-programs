// Question 11: Write a program to illustrate creation of threads using the Runnable class. Start each newly created thread. Inside the run method,
// there is sleep() to suspend the thread for 500 milliseconds.

class MyRunnable implements Runnable {
    @Override
    public void run() {
        try {
            System.out.println(Thread.currentThread().getName() + " is running");
            Thread.sleep(500); // Suspend thread for 500 milliseconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new MyRunnable(), "Thread-1");
        Thread thread2 = new Thread(new MyRunnable(), "Thread-2");
        
        thread1.start();
        thread2.start();
    }
}
