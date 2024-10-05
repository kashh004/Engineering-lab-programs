// Question 7: Develop a JAVA program to create an interface Resizable with methods resizeWidth(int width) and resizeHeight(int height)
// that allow an object to be resized. Create a class Rectangle that implements the Resizable interface and implements the resize methods.

interface Resizable {
    void resizeWidth(int width);
    void resizeHeight(int height);
}

class Rectangle implements Resizable {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public void resizeWidth(int width) {
        this.width = width;
    }

    @Override
    public void resizeHeight(int height) {
        this.height = height;
    }

    public void displayDimensions() {
        System.out.println("Rectangle width: " + width + ", height: " + height);
    }
}

public class ResizableDemo {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(10, 20);
        rect.displayDimensions();
        
        rect.resizeWidth(30);
        rect.resizeHeight(40);
        
        rect.displayDimensions();
    }
}
