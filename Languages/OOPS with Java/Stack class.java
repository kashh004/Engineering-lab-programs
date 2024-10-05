// Question 2: Develop a stack class to hold a maximum of 10 integers with suitable methods. Develop a JAVA main method to illustrate Stack operations.

class Stack {
    private int[] stack = new int[10];
    private int top = -1;

    // Push method
    public void push(int value) {
        if (top == 9) {
            System.out.println("Stack is full");
        } else {
            stack[++top] = value;
        }
    }

    // Pop method
    public int pop() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            return stack[top--];
        }
    }

    // Peek method
    public int peek() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            return stack[top];
        }
    }

    // Display method
    public void display() {
        if (top == -1) {
            System.out.println("Stack is empty");
        } else {
            for (int i = 0; i <= top; i++) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }
    }
}

public class StackDemo {
    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(5);
        stack.push(10);
        stack.push(20);
        
        System.out.println("Stack after pushes:");
        stack.display();
        
        System.out.println("Peek element: " + stack.peek());
        
        stack.pop();
        System.out.println("Stack after pop:");
        stack.display();
    }
}
