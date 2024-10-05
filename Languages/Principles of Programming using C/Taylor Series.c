// Question 7: Compute sin(x)/cos(x) using Taylor series approximation. 
// Compare your result with the built-in library function. Print both the results with appropriate inferences.

#include <stdio.h>
#include <math.h>

double taylor_sin(double x, int n) {
    double term = x, sum = x;
    for (int i = 1; i < n; i++) {
        term = -term * x * x / (2 * i * (2 * i + 1));
        sum += term;
    }
    return sum;
}

double taylor_cos(double x, int n) {
    double term = 1, sum = 1;
    for (int i = 1; i < n; i++) {
        term = -term * x * x / (2 * i * (2 * i - 1));
        sum += term;
    }
    return sum;
}

int main() {
    double x;
    int n;
    
    printf("Enter the value of x in radians: ");
    scanf("%lf", &x);
    
    printf("Enter the number of terms for Taylor series approximation: ");
    scanf("%d", &n);

    double sin_approx = taylor_sin(x, n);
    double cos_approx = taylor_cos(x, n);
    double sinx_div_cosx = sin_approx / cos_approx;
    
    printf("Taylor series approximation of sin(x)/cos(x) = %lf\n", sinx_div_cosx);
    printf("Built-in sin(x)/cos(x) = %lf\n", sin(x) / cos(x));

    return 0;
}
