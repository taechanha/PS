let T = Int(readLine()!)!
var dp = Array(repeating:Array(repeating:0,count:10),count:1001)
var can = [[7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]]
for i in 0..<10 {
    dp[1][i] = 1
}
for k in 2...1000 {
    for n in (0...9) {
        dp[k][n] = can[n].reduce(into: 0, {$0 = (($0 % 1234567)+(dp[k-1][$1] % 1234567)) % 1234567})
    }
}
for _ in 0..<T {
    let N = Int(readLine()!)!
    print(dp[N].reduce(into: 0, {$0 = (($0 % 1234567)+($1 % 1234567)) % 1234567}))
}