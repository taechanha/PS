#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    int si = 1;
    while (si * si < n)
    {
        si += 1;
    }

    if (si * si > m)
    {
        cout << -1;
        return 0;
    }

    int ei = si;
    while (ei * ei < m)
    {
        ei += 1;
    }
    if (ei * ei > m) {
        ei -= 1;
    } 

    int sum = 0;
    for (int i = si; i <= ei; i++)
    {
        sum += i * i;
    }

    cout << sum << "\n"
         << si * si;
}