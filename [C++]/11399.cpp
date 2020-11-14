#include <iostream>
#include <queue>
using namespace std;

int count = 0;

int main()
{
    int N;
    cin >> N;

    priority_queue<int, vector<int>, greater<int>> pi;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        pi.push(temp);
    }

    while (!pi.empty())
    {
        count += pi.top() * N;
        pi.pop();
        N--;
    }

    cout << count << endl;
}