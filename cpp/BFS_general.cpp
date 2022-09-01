#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

vector<bool> bfs(int start, int n, map<int, vector<int>> G) {
    queue<int> q;
    q.push(start);
    vector<bool> visited(n, false);
    visited[start] = true;
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        for (int neigh : G[curr]) {
            if (visited[neigh]) {
                continue;
            }

            q.push(neigh);
            visited[neigh] = true;
        }
    }
    return visited;
}

int main() {
    int n;
    cin >> n;
    map<int, vector<int>> G;

    for (int i=0; i<n; i++) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    vector<bool> visited = bfs(0, n, G);
    for (bool v: visited) {
        cout << v << " ";
    }

    return 0;
}