#include <iostream>
#include <vector> // +pair
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <queue>

using namespace std;


// [] fast input
// [v] pair, vector, queue, stack, set, map, priority queue
// [] when to use * and & operator
// [] h1ow to use pq?



int main() {
    // PAIR
    // .first, .second
    // make_pair(v_type1, v_type2)

    pair<string, int> pair;
    pair.first = "first";
    pair.second = 1;
    printf("%d \n", pair.second);
    pair = make_pair("sec", 2);
    printf("%d \n", pair.second);

    // --------------------------
    // Vector
    // front()
    // back()
    // begin()
    // end()
    // push_back()
    // pop_back()
    // size()
    // clear()

    vector<int> v1 = {1, 2, 3};
    printf("v1: %d \n", v1[0]);
    vector<::pair<int, char> > v2;
    int a, b;
    char c, d;

    v1.push_back(1);
    v1.push_back(2);
    for (int i=0; i<v1.size(); i++) {
        printf("%d ", v1[i]);
    }
    printf("\n");

    a = v1.front();
    b = v1.back();
    
    v1.pop_back();

    v2.push_back(make_pair(1, 'a'));

    printf("%d %c", v2.front().first, v2.front().second);
    
    // --------------------------
    // Queue
    // push()
    // pop()
    // front()
    // back()
    // size()
    // empty()

    queue<int> q1;
    queue<::pair<int, char>> q2;

    q1.push(1);
    q1.front();
    q1.back();
    q1.size();

    q2.push(make_pair(1, 'a'));

    // --------------------------
    // Stack
    // push()
    // pop()
    // top()
    // size()
    // empty()

    stack<int> s1;

    // --------------------------
    // Set
    // insert(n)
    // begin()
    // end()
    // find(n)
    // size()
    // empty()

    set<int> set1;
    set1.insert(1);
    set1.insert(2);
    set<int>::iterator it;
    for (it = set1.begin(); it!=set1.end(); it++) {
        printf("%d ", *it);
    }

    // ----------------
    // Map
    // insert(make_pair(k, v))
    // erase(k)
    // begin()
    // end()
    // find(k)
    // size()
    // empty()

    map<char, int> m1;
    m1.insert(make_pair('a', 1));
    m1['b'] = 2;

    map<char, int>::iterator it2;
    for (it2=m1.begin(); it2!=m1.end(); it2++) {
        printf("%c %d ", (*it2).first, (*it2).second);
    }

    // ----------------
    // Priority queue
    // push()
    // pop()
    // top()
    // size()
    // empty()

    priority_queue<int, vector<int>, less<int>> q;
    q.push(1);
    printf("\n q: %d \n", q.top());
}