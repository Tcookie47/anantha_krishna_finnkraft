def longest_common(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest, end = 0, 0
    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1] > longest:
                    longest = dp[i+1][j+1]
                    end = i
    return str1[end - longest + 1: end + 1]

print(longest_common("qwertyuiosbaksdbvaskfvlsdnfvolisdfvlnds", "qwer"))