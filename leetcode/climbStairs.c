int climbStairs(int n){
    
    if(dp[n] != -1)
        return dp[n];                // return it if it's already calculated (so it's no more '-1')
    else if(n == 0)
        return 1;
    else if(n == 1)
        return 1;
    
    return dp[n] = climbStairs(n-1) + climbStairs(n-2);    // Because the pattern follows fibonacci
}
