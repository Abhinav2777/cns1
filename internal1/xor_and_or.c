#include <stdio.h>
#include <string.h>
void main() {
char str[] = "Hello world";
char *str1 = strdup(str);
char *str2 = strdup(str);
char *c = str;
char *c1 = str1;
char *c2 = str2;
while (*c != '\0') {
*c = *c ^ 127;
*c1 = *c1 & 127;
*c2 = *c2 | 127;
c++; c1++; c2++; }
printf("XOR output: %s \n", str);
printf("AND output: %s \n", str1);
printf("OR output: %s \n", str2);
}
