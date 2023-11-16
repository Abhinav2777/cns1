#include<stdio.h>
void main() {
char str[] = "Hello world";
printf("Input string: %s \n", str);
char *c = str;
while (*c != '\0') {
*c = *c ^ 0;
c++;
}
printf("After XOR with 0: %s \n", str);
}
