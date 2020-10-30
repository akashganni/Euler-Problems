#include <iostream>
using namespace std;

int largestPrime(long long num, int x = 2) {
    if (num % x == 0) {
        if(num / x == 1) {
            return x;
        }
        return largestPrime((num / x));
    }
    return largestPrime(num, (x + 1));
}

int main(int argc, char const *argv[])
{
    cout << largestPrime(600851475143);
    return 0;
}
