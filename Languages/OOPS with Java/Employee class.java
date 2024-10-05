// Question 3: A class called Employee, which models an employee with an ID, name and salary. The method raiseSalary (percent) increases the salary by the given percentage.

class Employee {
    private int id;
    private String name;
    private double salary;

    // Constructor
    public Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    // Method to raise salary by a percentage
    public void raiseSalary(double percent) {
        salary += salary * (percent / 100);
    }

    // Display employee details
    public void display() {
        System.out.println("Employee ID: " + id);
        System.out.println("Employee Name: " + name);
        System.out.println("Employee Salary: " + salary);
    }
}

public class EmployeeDemo {
    public static void main(String[] args) {
        Employee emp = new Employee(1, "John Doe", 50000);
        emp.display();

        System.out.println("Raising salary by 10%");
        emp.raiseSalary(10);
        emp.display();
    }
}
