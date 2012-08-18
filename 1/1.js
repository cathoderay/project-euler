/*
 * File: 1.js
 * Description: http://projecteuler.net/problem=1
 */

var sum = 0;
for(i = 3; i < 1000; i++) 
    if (!(i % 3) || !(i % 5))
        sum += i;
print(sum)

