// Question 10: Implement structures to read, write and compute average marks of the students, 
// list the students scoring above and below the average marks for a class of N students.

#include <stdio.h>

struct Student {
    char name[50];
    int marks;
};

int main() {
    int n, total = 0;
    printf("Enter the number of students: ");
    scanf("%d", &n);
    
    struct Student students[n];
    
    // Input student data
    for (int i = 0; i < n; i++) {
        printf("Enter name and marks of student %d: ", i + 1);
        scanf("%s %d", students[i].name, &students[i].marks);
        total += students[i].marks;
    }
    
    float average = total / (float)n;
    printf("Class average marks: %.2f\n", average);
    
    printf("Students scoring above average:\n");
    for (int i = 0; i < n; i++) {
        if (students[i].marks > average)
            printf("%s\n", students[i].name);
    }
    
    printf("Students scoring below average:\n");
    for (int i = 0; i < n; i++) {
        if (students[i].marks < average)
            printf("%s\n", students[i].name);
    }
    
    return 0;
}
