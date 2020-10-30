#include <iostream>
using namespace std;

int sumFibonacci(int num, int start = 1, int next = 2, int sum = 1) {
    if (next >= num) {
        return sum;
    }
    return sumFibonacci(num, next, (start + next) , (sum + next));
}

int main(int argc, char const *argv[])
{
    cout << sumFibonacci(4000000);
    return 0;
}
