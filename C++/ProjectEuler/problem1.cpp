#include "problem1.h"
#include "iostream"

Problem1::Problem1(int l)
{
    limit = l;
    sum = 0;
    findSum3And5();
}

void Problem1::findSum3And5()
{
    for(int i = 0; i < limit; i++)
        if(i % 3 == 0 || i % 5 == 0)
            sum += i;

    std::cout << sum << std::endl;
}
