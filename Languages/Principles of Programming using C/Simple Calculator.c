// Question 1: Simulation of a Simple Calculator.

#include <stdio.h>

int main() {
    char operator;
    double firstNumber, secondNumber;
    
    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);
    
    printf("Enter two numbers: ");
    scanf("%lf %lf", &firstNumber, &secondNumber);
    
    switch (operator) {
        case '+':
            printf("%.1lf + %.1lf = %.1lf", firstNumber, secondNumber, firstNumber + secondNumber);
            break;
        case '-':
            printf("%.1lf - %.1lf = %.1lf", firstNumber, secondNumber, firstNumber - secondNumber);
            break;
        case '*':
            printf("%.1lf * %.1lf = %.1lf", firstNumber, secondNumber, firstNumber * secondNumber);
            break;
        case '/':
            if (secondNumber != 0)
                printf("%.1lf / %.1lf = %.1lf", firstNumber, secondNumber, firstNumber / secondNumber);
            else
                printf("Division by zero is not allowed.");
            break;
        default:
            printf("Invalid operator.");
    }
    
    return 0;
}
