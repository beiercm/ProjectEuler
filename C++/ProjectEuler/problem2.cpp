#include "problem2.h"
#include <iostream>

Problem2::Problem2(int l)
{
    limit = l;
    sum = 0;
    evenFib();
}

void Problem2::evenFib()
{
    int n1 = 1, n2 = 1, n3 = 2;

    while(n3 < limit)
    {
        n3 = n1 + n2;
        n1 = n2;
        n2 = n3;

        if(n3 % 2 == 0)
            sum += n3;
    }

    std::cout << sum << std::endl;
}
