#include <iostream>
using namespace std;

bool hanNum(int Num)
{
    if (Num >= 1000)
    {
        int A, B, C, D;
        D = Num % 10;
        C = (Num / 10) % 10;
        B = (Num / 100) % 10;
        A = (Num / 1000) % 10;
        if (A - B == B - C && B - C == C - D)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else if (Num >= 100)
    {
        int A, B, C;
        C = Num % 10;
        B = (Num / 10) % 10;
        A = (Num / 100) % 10;
        if (A - B == B - C)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return true;
    }
}

int main()
{
    int N;
    cin >> N;
    int count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (hanNum(i))
            count++;
    }
    cout << count << endl;
}