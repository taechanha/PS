#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
// STL: pair, vector, queue, stack, set, map, priority queue

using namespace std;

int main()
{
    // 자주 하는 실수
    // 1. 산술 오버/언더 플로
    // 2. 배열 범위 밖 원소 접근
    // 3. off-by-one; 특히 <, <= 연산자 사용 시
    // 4. float: 유효숫자 6자리까지, double: 15자리까지 -> float은 상대 오차 10^(-6)까지 안전
    // 5. 실수끼리는 == 비교 X; a==b가 아니라 abs(a-b) < 1e-12인지 확인
    // 6. double(유효숫자 최대 15자리)에 long long(유효숫자 최대 19) 범위의 정수를 함부로 담으면 안 됨




    // 기본: signed
    // unsigned: -128~127 -> 0~255 (1 바이트 기준);
    char a;      // 1 byte    %c
    short a;     // 2 bytes
    int a;       // 4 bytes   %d
    float a;     // 4 bytes   %f
    long a;      // 4 bytes   %ld
    long long a; // 8 bytes   %lld
    bool a;      // 1 byte
    double a;    // 8 bytes   %f
                 // %s: string

    // 입출력
    ios_base::sync_with_stdio(false); // c와 c++의 표준 입출력 스트림을 동기화하지 않음 -> C/C++ 입출력 혼용X
    cin.tie(nullptr);                 // cin 사용 시 출력 버퍼를 비우지 않는다.

    // endl(출력 버퍼까지 비움) 대신 "\n" 사용하기

    // first, second로 접근
    pair<int, char> p;
    p.first = 1;
    p.second = 'a';
    p = make_pair(3, 'b');

    vector<int> v1;
    v1.push_back(1);
    v1.pop_back();
    v1.clear();
    v1.push_back(1);
    v1.size();

    for (vector<int>::iterator it = v1.begin(); it != v1.end(); ++it)
    {
        cout << *it << ' ';
    }

    queue<int> q1;
    q1.push(1);
    q1.pop();
    q1.front();
    q1.back();
    q1.size();
    q1.empty();

    // 균형 이진 트리로 구현; 정렬
    stack<string> s1;
    s1.push("1");
    s1.top();
    s1.pop();
    s1.size();
    s1.empty();

    set<int> set;
    set.insert(2);
    set.begin();
    set.end();
    set.find(2);
    set.size();
    set.empty();

    map<string, int> map;
    string k = "someKey";
    int v = 1;
    map.insert(make_pair(k, v));
    map.erase(k);
    map.begin(); // iter
    map.end();   // iter
    map.find(k); // iter
    map.size();
    map.empty();

    priority_queue<int, vector<int>, less<int> > q;
    int n;
    q.push(3);
    q.top();
    printf("%d ", q.top());
    q.size();
    q.pop();

    // list

    // deque
}

void dfs(int x)
{
    if (visited[x])
    {
        return;
    }
    visited[x] = true;
    cout << x << "";
    for (int i = 0; i < G[x].size(); i++)
    {
        int neighbor = a[x][i];
        difs(neighbor);
    }
}

void bfs(int x)
{
    queue<int> q;
    q.push(x);
    visited[x] = true;

    while (!q.empty())
    {
        int curr = q.pop();
        cout << curr << " ";
        for (int i = 0; i < a[curr].size; i++)
        {
            int neighbor = a[curr][i];
            if (!visited[neighbor])
            {
                q.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}