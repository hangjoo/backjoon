#include <iostream>
using namespace std;

int cases[11];

int plus123(const int num)
{
    if (num <= 0)
        return cases[0];
    else if (num == 1)
        return cases[num] = plus123(num - 1);
    else if (num == 2)
        return cases[num] = plus123(num - 1) + plus123(num - 2);
    else
        return cases[num] = plus123(num - 1) + plus123(num - 2) + plus123(num - 3);
}

int main()
{
    cases[0] = 1;

    int count;
    cin >> count;
    for (int i = 0; i < count; i++)
    {
        int num;
        cin >> num;

        cout << plus123(num) << endl;
    }
}