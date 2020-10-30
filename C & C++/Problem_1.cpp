#include <iostream>
#include <string.h>
using namespace std;

int func(int num)
{
    int sum = 0;
    num -= 1;
    while (num > 0)
    {
        if (num % 3 == 0 || num % 5 == 0)
        {
            sum += num;
        }
        num -= 1;
    }
    return sum;
}

int main(int argc, char const *argv[])
{
    int num;
    cout << "Enter: ";
    cin >> num;
    cout << "Ans: " << func(num);
    return 0;
}