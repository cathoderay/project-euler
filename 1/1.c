/*
 * File: 1.c
 * Description: http://projecteuler.net/problem=1
 */

#include<stdio.h>

void main() {
    int i, sum = 0;
    for(i = 3; i < 1000; i++)
        if (!((i % 5) && (i % 3)))
            sum += i;
    printf("%d\n", sum);
}
