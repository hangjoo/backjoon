#include <iostream>
#include <queue>
using namespace std;

int count = 0;
int coin_count = 0;

int main()
{
    int n, k;
    cin >> n >> k;

    priority_queue<int> coin;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        coin.push(temp);
    }

    while (!coin.empty())
    {
        while (coin_count < k)
        {
            coin_count += coin.top();
            count++;
        }
        if (coin_count == k)
        {
            cout << count << endl;
            break;
        }
        else
        {
            coin_count -= coin.top();
            count--;
            coin.pop();
        }
    }
}