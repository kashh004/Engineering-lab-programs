// Question 12: Write a C program to copy a text file to another, read both the input file name and target file name.

#include <stdio.h>

int main() {
    char sourceFile[100], targetFile[100];
    FILE *source, *target;
    char ch;

    printf("Enter name of source file: ");
    scanf("%s", sourceFile);

    printf("Enter name of target file: ");
    scanf("%s", targetFile);

    source = fopen(sourceFile, "r");
    if (source == NULL) {
        printf("Error opening source file.\n");
        return 1;
    }

    target = fopen(targetFile, "w");
    if (target == NULL) {
        fclose(source);
        printf("Error opening target file.\n");
        return 1;
    }

    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, target);
    }

    printf("File copied successfully.\n");

    fclose(source);
    fclose(target);

    return 0;
}
