// Question 9: Write functions to implement string operations such as compare, concatenate, and find string length. 
// Use the parameter passing techniques.

#include <stdio.h>
#include <string.h>

int compareStrings(char str1[], char str2[]) {
    return strcmp(str1, str2);
}

void concatenateStrings(char str1[], char str2[]) {
    strcat(str1, str2);
}

int stringLength(char str[]) {
    return strlen(str);
}

int main() {
    char str1[100], str2[100];
    
    printf("Enter the first string: ");
    scanf("%s", str1);
    
    printf("Enter the second string: ");
    scanf("%s", str2);

    int cmpResult = compareStrings(str1, str2);
    printf("String comparison result: %d\n", cmpResult);

    concatenateStrings(str1, str2);
    printf("Concatenated string: %s\n", str1);

    printf("Length of first string: %d\n", stringLength(str1));
    printf("Length of second string: %d\n", stringLength(str2));

    return 0;
}
