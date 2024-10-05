// Question 2: Compute the roots of a quadratic equation by accepting the coefficients. Print appropriate messages.

#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
    
    printf("Enter coefficients a, b and c: ");
    scanf("%lf %lf %lf", &a, &b, &c);
    
    discriminant = b * b - 4 * a * c;
    
    // Condition for real and different roots
    if (discriminant > 0) {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("Root 1 = %.2lf\nRoot 2 = %.2lf", root1, root2);
    }
    // Condition for real and equal roots
    else if (discriminant == 0) {
        root1 = root2 = -b / (2 * a);
        printf("Root 1 = Root 2 = %.2lf", root1);
    }
    // If roots are not real
    else {
        realPart = -b / (2 * a);
        imaginaryPart = sqrt(-discriminant) / (2 * a);
        printf("Root 1 = %.2lf + %.2lfi\n", realPart, imaginaryPart);
        printf("Root 2 = %.2lf - %.2lfi", realPart, imaginaryPart);
    }
    
    return 0;
}
