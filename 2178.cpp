#include <iostream>
#include <queue>
#include <stack>
using namespace std;

int N, M;

void bfs(int** maze, int** distance)
{
    queue<pair<int, int>> visit;
    pair<int, int> start = make_pair(0, 0);
    distance[start.first][start.second] = 1;

    visit.push(start);

    while (!visit.empty())
    {
        pair<int, int> current = visit.front();
        visit.pop();
        if (current.first == N - 1 && current.second == M - 1)
        {
            break;
        }

        for (int i = -1; i <= 1; i += 2)
        {
            int new_x = current.first + i;
            int new_y = current.second + i;
            if (new_x >= 0 && new_x <= N - 1 && maze[new_x][current.second] == 1 && distance[new_x][current.second] == -1)
            {
                visit.push(make_pair(new_x, current.second));
                distance[current.first + i][current.second] = distance[current.first][current.second] + 1;
            }
            if (new_y >= 0 && new_y <= M - 1 && maze[current.first][new_y] == 1 && distance[current.first][new_y] == -1)
            {
                visit.push(make_pair(current.first, new_y));
                distance[current.first][new_y] = distance[current.first][current.second] + 1;
            }
        }
    }
}

int main()
{
    cin >> N >> M;

    // init
    int** maze = new int*[N];
    int** distance = new int*[N];  // if distance[i][j] = -1, not visited (i, j) node. else, the shortest distance to (i, j) node.
    queue<pair<int, int>> visit;

    for (int i = 0; i < N; i++)
    {
        maze[i] = new int[M];
        distance[i] = new int[M];

        char* line = new char[M];
        cin >> line;
        for (int j = 0; j < M; j++)
        {
            maze[i][j] = line[j] - '0';
            distance[i][j] = -1;
        }
    }
    // bfs.
    bfs(maze, distance);

    // print distance.
    cout << distance[N - 1][M - 1];
}
