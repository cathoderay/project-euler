/*
 * File: 9.c
 * Description: http://projecteuler.net/problem=9
 */

#include<stdio.h>

int main() {
    int i, j, a, b, c;
    for(i = 1; i < 1000; i++)
        for(j = i + 1; j < 1000; j++) {
            a = i;
            b = j - i;
            c = 1000 - (b + a);
            if (c*c == a*a + b*b) {
                printf("%d\n", a*b*c);
                return 0;
            }
        }
}
