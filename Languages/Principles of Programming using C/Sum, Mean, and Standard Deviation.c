// Question 11: Develop a program using pointers to compute the sum, mean, and standard deviation of all elements 
// stored in an array of N real numbers.

#include <stdio.h>
#include <math.h>

void calculateStats(float *arr, int n, float *sum, float *mean, float *stdDev) {
    *sum = 0;
    for (int i = 0; i < n; i++) {
        *sum += arr[i];
    }
    
    *mean = *sum / n;
    
    *stdDev = 0;
    for (int i = 0; i < n; i++) {
        *stdDev += pow(arr[i] - *mean, 2);
    }
    *stdDev = sqrt(*stdDev / n);
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    float arr[n];
    printf("Enter %d real numbers: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%f", &arr[i]);
    }

    float sum, mean, stdDev;
    calculateStats(arr, n, &sum, &mean, &stdDev);
    
    printf("Sum: %.2f\n", sum);
    printf("Mean: %.2f\n", mean);
    printf("Standard Deviation: %.2f\n", stdDev);

    return 0;
}
