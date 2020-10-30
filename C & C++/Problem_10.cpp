#include <iostream>
using namespace std;

int isPrime(int num) {
    int x = 2;
    int s = 0;
    while (x <= num) {
        if (num % x == 0) {
            num = num / x;
            x = 1;
            s += 1;
        }
        x += 1;
    }
    return s;
}

int sumPrimes(int num) {
    int x = 3;
    int s = 2;
    while (x < num) {
        if (isPrime(x) == 1) {
            s += x;
        }
        x += 2;
    }
    return s;
}

int main(int argc, char const *argv[])
{
    cout << sumPrimes(2000000);
    return 0;
}
