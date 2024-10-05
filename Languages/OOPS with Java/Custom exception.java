// Question 9: Develop a JAVA program to raise a custom exception (user-defined exception) for DivisionByZero using try, catch, throw, and finally.

class DivisionByZeroException extends Exception {
    public DivisionByZeroException(String message) {
        super(message);
    }
}

public class CustomExceptionDemo {
    public static void main(String[] args) {
        try {
            divide(10, 0);
        } catch (DivisionByZeroException e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("This block is always executed");
        }
    }

    public static void divide(int a, int b) throws DivisionByZeroException {
        if (b == 0) {
            throw new DivisionByZeroException("Division by zero is not allowed!");
        } else {
            System.out.println("Result: " + a / b);
        }
    }
}
