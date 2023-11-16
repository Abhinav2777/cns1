#include <stdio.h>

int main() {
    FILE *input_file;
    FILE *output_file;

    // Define the input and output file paths
    const char *input_file_path = "./input.txt";
    const char *output_file_path = "./output.txt";

    // Open the input file for reading
    input_file = fopen(input_file_path, "r");
    if (input_file == NULL) {
        printf("Error opening input file.\n");
        return 1;
    }

    // Open the output file for writing
    output_file = fopen(output_file_path, "w");
    if (output_file == NULL) {
        printf("Error opening output file.\n");
        fclose(input_file);
        return 1;
    }

    // Read characters from input file, perform XOR with 0, and write to output file
    int ch;
    while ((ch = fgetc(input_file)) != EOF) {
        char result = ch ^ 0;
        fputc(result, output_file);
    }

    // Close the files
    fclose(input_file);
    fclose(output_file);

    printf("XOR operation completed. Output written to %s\n", output_file_path);

    return 0;
}

