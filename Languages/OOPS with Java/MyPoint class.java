// Question 4: A class called MyPoint, which models a 2D point with x and y coordinates.

class MyPoint {
    private int x;
    private int y;

    // Default constructor
    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }

    // Overloaded constructor
    public MyPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // Set x and y values
    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // Get x and y values
    public int[] getXY() {
        return new int[]{x, y};
    }

    // Calculate distance from another point (x, y)
    public double distance(int x, int y) {
        return Math.sqrt((this.x - x) * (this.x - x) + (this.y - y) * (this.y - y));
    }

    // Calculate distance from another MyPoint
    public double distance(MyPoint another) {
        return Math.sqrt((this.x - another.x) * (this.x - another.x) + (this.y - another.y) * (this.y - another.y));
    }

    // Calculate distance from the origin (0, 0)
    public double distance() {
        return Math.sqrt(x * x + y * y);
    }

    // Override toString() method
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

public class TestMyPoint {
    public static void main(String[] args) {
        MyPoint p1 = new MyPoint(3, 4);
        MyPoint p2 = new MyPoint(6, 8);

        System.out.println("Point 1: " + p1);
        System.out.println("Point 2: " + p2);

        System.out.println("Distance from p1 to p2: " + p1.distance(p2));
        System.out.println("Distance from p1 to origin: " + p1.distance());
    }
}
