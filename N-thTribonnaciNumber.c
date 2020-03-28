int tribonacci(int n){
    int dp[4] = {0, 1, 1, 0};
    for(int i=3;i<n+1;++i)
       dp[i%4] = dp[(i-3)%4] + dp[(i-2)%4] + dp[(i-1)%4];
    return dp[n%4];
}
