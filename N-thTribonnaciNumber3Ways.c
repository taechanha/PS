int tribonacci(int n){
    int dp[4] = {0, 1, 1, 0};
    for(int i=3;i<n+1;++i)
       dp[i%4] = dp[(i-3)%4] + dp[(i-2)%4] + dp[(i-1)%4];
    return dp[n%4];
}


int tribonacci(int n){
    int dp[100000] = {0, 1, 1, 0};

    for(int i=3;i<n+1;++i){
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
    }
    return dp[n];
}


int dp[50] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};

int tribonacci(int n){

    if(dp[n] != -1)
        return dp[n];

    if(n == 0)
        return 0;
    else if(n == 1)
        return 1;
    else if(n == 2)
        return 1;

    return dp[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
}
