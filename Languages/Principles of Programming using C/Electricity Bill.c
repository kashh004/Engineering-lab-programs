// Question 3: An electricity board charges the following rates for the use of electricity: for the first 200 units 80 paise per unit; 
// for the next 100 units 90 paise per unit; beyond 300 units Rs 1 per unit. All users are charged a minimum of Rs. 100 as meter charge. 
// If the total amount is more than Rs 400, then an additional surcharge of 15% of the total amount is charged. 
// Write a program to read the name of the user, number of units consumed and print out the charges.

#include <stdio.h>

int main() {
    char name[50];
    double units, charge = 100, total;

    printf("Enter name of user: ");
    scanf("%s", name);
    printf("Enter number of units consumed: ");
    scanf("%lf", &units);

    if (units <= 200) {
        charge += units * 0.80;
    } else if (units <= 300) {
        charge += 200 * 0.80 + (units - 200) * 0.90;
    } else {
        charge += 200 * 0.80 + 100 * 0.90 + (units - 300) * 1.00;
    }

    if (charge > 400) {
        total = charge + (0.15 * charge);
    } else {
        total = charge;
    }

    printf("Total charge for %s is: Rs %.2lf\n", name, total);
    
    return 0;
}
