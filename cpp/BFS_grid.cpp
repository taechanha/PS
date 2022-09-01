#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    
    vector<tuple<int, int, int>> vt = {{1, 2, 3}};
    // q.push_back(make_tuple(1, 2, 3));
    vt.push_back({21, 22, 23});
    
    int res = get<1>(vt[1]);
    cout << "vt: " << res << "\n";

    vector<pair<int, int>> vp = {{1, 2}};
    cout << "vp: " << vp[0].first << "\n";
    return 0;
}

// int n;
// char board[101][101];
// int dr[4] = {-1, 1, 0, 0};
// int dc[4] = {0, 0, -1, 1};

// void bfs(int r, int c) {
//     queue<pair<int, int>> q;
//     q.push(make_pair(r, c));
//     bool visited[101][101] = {false, };

// }